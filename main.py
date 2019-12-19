import pygame
import sys
import classes
import global_perms


def terminate():
    """Завершение работы процесса игры"""
    pygame.quit()
    sys.exit()


def init_music(MUSIC_REPEAT):
    """Инициализирует музыку, играющую на протяжении всей игры"""
    pygame.mixer.init()
    pygame.mixer.music.load("sound\\tank.mp3")
    pygame.mixer.music.play()
    pygame.time.set_timer(MUSIC_REPEAT, 42736)


def clear_level_data():
    """Очищает группы спрайтов, дабы загрузить новый уровень"""
    global_perms.ALL_SPRITES = pygame.sprite.Group()
    global_perms.DESTROY_WALLS = pygame.sprite.Group()
    global_perms.WALLS = pygame.sprite.Group()
    global_perms.ALL_SPRITES.add(global_perms.PLAYER)


def load_level(level_number):
    """Загружает данные из файла с уровнем"""
    filename = "levels/level_{}.txt".format(level_number)
    with open(filename) as file:
        data = [line.strip() for line in file]
    return data


def get_data_of_level(level_number):
    """Полуает разложеные по перменным данные из файла с уровнем"""
    data_of_level = load_level(level_number)
    map_data = data_of_level[:-3]
    enemy_spawners_pos = list(map(lambda elem: tuple(map(int, elem.split())),
                                  data_of_level[-3].split(';')))
    player_pos = tuple(map(int, data_of_level[-2].split()))
    player_pos = player_pos[0] * 32, player_pos[1] * 32
    base_pos = tuple(map(int, data_of_level[-1].split()))
    base_pos = base_pos[0] * 32, base_pos[1] * 32
    return map_data, enemy_spawners_pos, player_pos, base_pos


def launch_level():
    """Создаёт спрайты и вносит их в группы"""
    clear_level_data()
    map_data, enemy_spawners_pos, player_pos, base_pos = get_data_of_level(global_perms.LEVEL_ID)
    global_perms.PLAYER.rect.topleft = player_pos
    base = classes.Base(*base_pos, global_perms.ALL_SPRITES, global_perms.WALLS,
                        global_perms.DESTROY_WALLS)
    for y in range(len(map_data)):
        for x in range(len(map_data[y])):
            if map_data[y][x] != '-':
                pos_x, pos_y = x * 16, y * 16
                if map_data[y][x] == global_perms.BRICK:
                    classes.Brick(pos_x, pos_y, global_perms.ALL_SPRITES, global_perms.WALLS,
                                  global_perms.DESTROY_WALLS)
                elif map_data[y][x] == global_perms.GRASS:
                    classes.Grass(pos_x, pos_y, global_perms.ALL_SPRITES)
                elif map_data[y][x] == global_perms.WATER:
                    classes.Water(pos_x, pos_y, global_perms.ALL_SPRITES, global_perms.WALLS)
    return enemy_spawners_pos, base


def start_game():
    """Основной цикл игры"""
    MUSIC_REPEAT = 30
    init_music(MUSIC_REPEAT)
    global_perms.PLAYER = classes.Player(0, 0)
    enemy_spawners_pos, base = launch_level()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause_screen()
                else:
                    global_perms.PLAYER.action = event.key
            elif event.type == pygame.KEYUP:
                if event.key == global_perms.PLAYER.action:
                    global_perms.PLAYER.action = None
            elif event.type == MUSIC_REPEAT:
                pygame.mixer.music.play()
        global_perms.ALL_SPRITES.update()
        global_perms.SCREEN.fill(pygame.Color('black'))
        global_perms.ALL_SPRITES.draw(global_perms.SCREEN)
        pygame.display.flip()
        global_perms.CLOCK.tick(global_perms.FPS)


def pause_screen():
    """Пауза игры"""
    pause = True
    font = pygame.font.Font(None, 50)
    text = font.render("PAUSE", 1, (100, 255, 100))
    text_x = global_perms.WIDTH // 2 - text.get_width() // 2
    text_y = global_perms.HEIGHT // 2 - text.get_height() // 2
    global_perms.SCREEN.blit(text, (text_x, text_y))
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause = False
        pygame.display.flip()
        global_perms.CLOCK.tick(global_perms.FPS)


pygame.init()
start_game()
