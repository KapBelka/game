import pygame
import images
import global_perms
import random


class Tank(pygame.sprite.Sprite):
    def __init__(self, x, y, image_name, *args):
        pygame.sprite.Sprite.__init__(self, args)
        self.image_name = image_name
        self.image = images.images[image_name + '_w']
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.health = 1
        self.speed = 4
        self.action = None
        self.bullet = None

    def update(self):
        collided = self.check_collided(global_perms.WALLS)
        if self.action == pygame.K_SPACE:
            self.do_shot()
        elif self.action == pygame.K_a:
            if pygame.K_a not in collided:
                self.rect.x -= self.speed
            self.image = images.images[self.image_name + '_a']
        elif self.action == pygame.K_d:
            if pygame.K_d not in collided:
                self.rect.x += self.speed
            self.image = images.images[self.image_name + '_d']
        elif self.action == pygame.K_w:
            if pygame.K_w not in collided:
                self.rect.y -= self.speed
            self.image = images.images[self.image_name + '_w']
        elif self.action == pygame.K_s:
            if pygame.K_s not in collided:
                self.rect.y += self.speed
            self.image = images.images[self.image_name + '_s']

    def do_shot(self):
        if not self.bullet:
            x, y = self.rect.center
            naprav_x, naprav_y = 0, 0
            if self.image == images.images[self.image_name + '_w']:
                naprav_y = -1
            elif self.image == images.images[self.image_name + '_a']:
                naprav_x = -1
            elif self.image == images.images[self.image_name + '_s']:
                naprav_y = 1
            elif self.image == images.images[self.image_name + '_d']:
                naprav_x = 1
            self.bullet = Bullet(x, y, naprav_x, naprav_y, self, global_perms.ALL_SPRITES)

    def be_attacked(self):
        self.health -= 1
        if self.health == 0:
            self.kill()

    def check_collided(self, group_sprites):
        collided_sides = set()
        for sprite2 in group_sprites:
            if (-1 < self.rect.left - sprite2.rect.right < 1 and
                    -20 <= self.rect.center[1] - sprite2.rect.center[1] <= 20 or
                    self.rect.left <= 0):
                collided_sides.add(pygame.K_a)
            if (-1 < self.rect.right - sprite2.rect.left < 1 and
                    -20 <= self.rect.center[1] - sprite2.rect.center[1] <= 20 or
                    self.rect.right >= global_perms.SCREEN_SIZE[0]):
                collided_sides.add(pygame.K_d)
            if (-1 < self.rect.top - sprite2.rect.bottom < 1 and
                    -20 <= self.rect.center[0] - sprite2.rect.center[0] <= 20 or
                    self.rect.top <= 0):
                collided_sides.add(pygame.K_w)
            if (-1 < self.rect.bottom - sprite2.rect.top < 1 and
                    -20 <= self.rect.center[0] - sprite2.rect.center[0] <= 20 or
                    self.rect.bottom >= global_perms.SCREEN_SIZE[1]):
                collided_sides.add(pygame.K_s)
        return collided_sides


class Player(Tank):
    def __init__(self, x, y, *args):
        super().__init__(x, y, 'player', args)
        self.start_pos = (x, y)
        self.life = 3

    def be_attacked(self):
        self.health -= 1
        if self.health == 0:
            if self.life > 0:
                self.life -= 1
                self.rect.topleft = self.start_pos
            else:
                global_perms.IS_GAME_OVER = True


class Enemy(Tank):
    def __init__(self, x, y, *args):
        super().__init__(x, y, 'enemy', args)
        self.step = 0

    def update(self):
        super().update()
        collided = self.check_collided(global_perms.WALLS)
        if self.step == 0:
            event = random.choice([pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_SPACE])
            if event not in collided:
                if event != pygame.K_SPACE:
                    count_step = random.randrange(5)
                    self.step = 4 * count_step
                self.action = event
        else:
            self.step -= 1


class Base(pygame.sprite.Sprite):
    def __init__(self, x, y, *args):
        pygame.sprite.Sprite.__init__(self, *args)
        self.image = images.images["base"]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.health = 5

    def be_attacked(self):
        self.health -= 1
        if self.health == 0:
            self.image = images.images["destroyed_base"]
            global_perms.IS_GAME_OVER = True


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, naprav_x, naprav_y, player, *args):
        pygame.sprite.Sprite.__init__(self, args)
        self.image = images.images["bullet"]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 8
        self.player = player
        self.naprav_x, self.naprav_y = naprav_x, naprav_y

    def update(self, *args):
        self.rect.x += self.speed * self.naprav_x
        self.rect.y += self.speed * self.naprav_y
        self.check_collided(global_perms.DESTROY_WALLS)
        if isinstance(self.player, Player):
            self.check_collided(global_perms.ENEMY_GROUP)
        else:
            self.check_collided(global_perms.PLAYER_GROUP)

    def destroy(self):
        self.player.bullet = None
        self.kill()

    def check_collided(self, group_sprites):
        hits = pygame.sprite.spritecollide(self, group_sprites, False)
        if hits:
            for elem in hits:
                elem.be_attacked()
            self.destroy()
        elif (not (0 <= self.rect.center[0] <= global_perms.SCREEN_SIZE[0]) or
              not (0 <= self.rect.center[1] <= global_perms.SCREEN_SIZE[1])):
            self.destroy()


class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, image_name, *args):
        pygame.sprite.Sprite.__init__(self, args)
        self.image = images.images[image_name]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


class Brick(Object):
    def __init__(self, x, y, *args):
        super().__init__(x, y, "brick", args)
        self.health = 1

    def be_attacked(self):
        self.health -= 1
        if self.health == 0:
            self.kill()


class Water(Object):
    def __init__(self, x, y, *args):
        super().__init__(x, y, "water", args)


class Grass(Object):
    def __init__(self, x, y, *args):
        super().__init__(x, y, "grass", args)
