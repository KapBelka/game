import pygame
import sys
import classes
import global_perms


def terminate():
    """Завершение работы процесса игры"""
    pygame.quit()
    sys.exit()


def init_music():
    """Инициализирует музыку, играющую на протяжении всей игры"""
    pygame.mixer.init()
    pygame.mixer.music.load("sound\\tank.mp3")
    pygame.mixer.music.play()


def clear_game_data():
    """Очищает глобальные переменные для начала новой игры"""
    global_perms.LEVEL_ID = 0
    global_perms.IS_GAME_OVER = False
    global_perms.GAME_RUNNING = True


def clear_level_data():
    """Очищает группы спрайтов, дабы загрузить новый уровень"""
    global_perms.ALL_SPRITES = pygame.sprite.Group()
    global_perms.DESTROY_WALLS = pygame.sprite.Group()
    global_perms.WALLS = pygame.sprite.Group()
    global_perms.PLAYER_GROUP = pygame.sprite.Group()
    global_perms.ENEMY_GROUP = pygame.sprite.Group()
    global_perms.ALL_SPRITES.add(global_perms.PLAYER)
    global_perms.PLAYER_GROUP.add(global_perms.PLAYER)


def load_level(level_number):
    """Загружает данные из файла с уровнем"""
    filename = "levels/level_{}.txt".format(level_number)
    with open(filename) as file:
        data = [line.strip() for line in file]
    return data


def get_level_data(level_number):
    """Полуает разложеные по перменным данные из файла с уровнем"""
    data_of_level = load_level(level_number)
    map_data = data_of_level[:-4]
    count_enemy = int(data_of_level[-4])
    enemy_spawners_pos = list(map(lambda elem: tuple(map(int, elem.split())),
                                  data_of_level[-3].split(';')))
    player_pos = tuple(map(int, data_of_level[-2].split()))
    player_pos = player_pos[0] * 32, player_pos[1] * 32
    base_pos = tuple(map(int, data_of_level[-1].split()))
    base_pos = base_pos[0] * 32, base_pos[1] * 32
    return map_data, enemy_spawners_pos, player_pos, base_pos, count_enemy


def launch_level():
    """Создаёт спрайты и вносит их в группы"""
    clear_level_data()
    map_data, enemy_pos, player_pos, base_pos, count_enemy = get_level_data(global_perms.LEVEL_ID)
    global_perms.PLAYER.rect.topleft = player_pos
    global_perms.PLAYER.start_pos = player_pos
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
    return enemy_pos, base, count_enemy


def draw_texts(count_enemy):
    """Отрисовывает кол-во жизней, танков и уровень"""
    font = pygame.font.Font(None, 30)
    text = font.render("LIFES: " + str(global_perms.PLAYER.get_lifes()), 1, (255, 255, 255))
    text_x, text_y = 0, 0
    global_perms.SCREEN.blit(text, (text_x, text_y))
    #
    text = font.render("LEVEL: " + str(global_perms.LEVEL_ID + 1), 1, (255, 255, 255))
    text_x, text_y = global_perms.WIDTH // 2 - text.get_width() // 2, 0
    global_perms.SCREEN.blit(text, (text_x, text_y))
    #
    text = font.render("TANKS: " + str(count_enemy + len(global_perms.ENEMY_GROUP)), 1,
                       (255, 255, 255))
    text_x, text_y = global_perms.WIDTH - text.get_width(), 0
    global_perms.SCREEN.blit(text, (text_x, text_y))


def update_and_draw_screen():
    """Отвечает за обновление и отрисовывание объектов"""
    global_perms.ALL_SPRITES.update()
    global_perms.SCREEN.fill(pygame.Color('black'))
    global_perms.ALL_SPRITES.draw(global_perms.SCREEN)


def complete_game_screen():
    """Конец игры(выиграть)"""
    wait = True
    font = pygame.font.Font(None, 50)
    texts = ["GAME COMPLETE", "PRESS <SPACE> TO RESTART", "PRESS <ESC> TO EXIT"]
    for i in range(3):
        text = font.render(texts[i], 1, (0, 255, 0))
        text_x = global_perms.WIDTH // 2 - text.get_width() // 2
        text_y = global_perms.HEIGHT // 2 - text.get_height() // 2 + text.get_height() * i
        global_perms.SCREEN.blit(text, (text_x, text_y))
    start_new_game = False
    while wait:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start_new_game = True
                    wait = False
                elif event.key == pygame.K_ESCAPE:
                    wait = False
        pygame.display.flip()
        global_perms.CLOCK.tick(global_perms.FPS)
    if start_new_game:
        clear_game_data()
        return 1
    return 0


def end_game_screen():
    """Конец игры(проиграть)"""
    wait = True
    font = pygame.font.Font(None, 50)
    texts = ["GAME END", "PRESS <SPACE> TO RESTART", "PRESS <ESC> TO EXIT"]
    for i in range(3):
        text = font.render(texts[i], 1, (255, 0, 0))
        text_x = global_perms.WIDTH // 2 - text.get_width() // 2
        text_y = global_perms.HEIGHT // 2 - text.get_height() // 2 + text.get_height() * i
        global_perms.SCREEN.blit(text, (text_x, text_y))
    start_new_game = False
    while wait:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start_new_game = True
                    wait = False
                elif event.key == pygame.K_ESCAPE:
                    wait = False
        pygame.display.flip()
        global_perms.CLOCK.tick(global_perms.FPS)
    if start_new_game:
        clear_game_data()
        return 1
    return 0


def end_level_screen():
    """Конец уровня"""
    wait = True
    font = pygame.font.Font(None, 50)
    text = font.render("LEVEL COMPLETE", 1, (255, 0, 0))
    text_x = global_perms.WIDTH // 2 - text.get_width() // 2
    text_y = global_perms.HEIGHT // 2 - text.get_height() // 2
    global_perms.SCREEN.blit(text, (text_x, text_y))
    while wait:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                wait = False
        pygame.display.flip()
        global_perms.CLOCK.tick(global_perms.FPS)


def pause_game():
    """Пауза игры"""
    pause = True
    font = pygame.font.Font(None, 50)
    text = font.render("PAUSE", 1, (255, 0, 0))
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


def start_game():
    """Основной цикл игры"""
    music_repeat = pygame.USEREVENT + 1
    time_spawn_enemy = pygame.USEREVENT + 2
    level_end_timer = pygame.USEREVENT + 3
    can_end_level = True
    init_music()
    pygame.time.set_timer(music_repeat, 42736)
    pygame.time.set_timer(time_spawn_enemy, 10000)
    global_perms.PLAYER = classes.Player(0, 0)
    enemy_pos, base, count_enemy = launch_level()
    while global_perms.GAME_RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause_game()
                else:
                    global_perms.PLAYER.action = event.key
            elif event.type == pygame.KEYUP:
                if event.key == global_perms.PLAYER.action:
                    global_perms.PLAYER.action = None
            elif event.type == level_end_timer:
                pygame.time.set_timer(level_end_timer, 0)
                global_perms.LEVEL_ID += 1
                if global_perms.LEVEL_ID == global_perms.MAX_LEVEL:
                    global_perms.GAME_RUNNING = False
                else:
                    end_level_screen()
                    can_end_level = True
                    enemy_pos, base, count_enemy = launch_level()
            elif event.type == time_spawn_enemy:
                i = len(enemy_pos) if len(enemy_pos) < count_enemy else count_enemy
                for j in range(i):
                    pos = enemy_pos[j]
                    classes.Enemy(pos[0] * 32, pos[1] * 32, global_perms.ALL_SPRITES,
                                  global_perms.ENEMY_GROUP)
                    count_enemy -= 1
            elif event.type == music_repeat:
                pygame.mixer.music.play()
        if len(global_perms.ENEMY_GROUP) == count_enemy == 0 and can_end_level:
            pygame.time.set_timer(level_end_timer, 5000)
            can_end_level = False
        update_and_draw_screen()
        draw_texts(count_enemy)
        pygame.display.flip()
        global_perms.CLOCK.tick(global_perms.FPS)
    if global_perms.IS_GAME_OVER:
        return 1
    else:
        return 0


pygame.init()
game = True
while game:
    result_code = start_game()
    if result_code == 1:
        ext_code = end_game_screen()
    else:
        ext_code = complete_game_screen()
    if ext_code == 0:
        game = False
