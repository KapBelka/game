import pygame
import classes
import levels
import sprites
from global_perms import *


def generate_level(level_id, player):
    data_of_level = levels.levels[level_id]
    level = data_of_level[:40]
    enemy_spawners_pos, player_pos, base_pos = data_of_level[-3:]
    player_pos = player_pos[0] * 32, player_pos[1] * 32
    player.rect.topleft = player_pos
    all_sprites = pygame.sprite.Group()
    walls = pygame.sprite.Group()
    bricks = pygame.sprite.Group()
    all_sprites.add(player)
    base = None  # ДОРАБОТАТЬ!!!
    for y in range(len(level)):
        for x in range(len(level[y])):
            pos_x, pos_y = x * 16, y * 16
            if level[y][x] == levels.BRICK:
                elem = classes.Brick(pos_x, pos_y)
                all_sprites.add(elem)
                walls.add(elem)
                bricks.add(elem)
            elif level[y][x] == levels.GRASS:
                all_sprites.add(classes.Grass(pos_x, pos_y))
            elif level[y][x] == levels.WATER:
                elem = classes.Water(pos_x, pos_y)
                all_sprites.add(elem)
                walls.add(elem)
    return all_sprites, enemy_spawners_pos, base, walls, bricks


fps = 30
screen = pygame.display.set_mode(SCREEN_SIZE)
running = True
player = classes.Player(0, 0)
all_sprites, enemy_spawners_pos, base, walls, bricks = generate_level(0, player)
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            player.action = event.key
        if event.type == pygame.KEYUP:
            if event.key == player.action:
                player.action = None
    if player.bullet:
        all_sprites.add(player.bullet)
        player.bullet.check_collided(bricks)
    all_sprites.update(walls)
    screen.fill(pygame.Color('black'))
    all_sprites.draw(screen)
    clock.tick(fps)
    pygame.display.flip()
