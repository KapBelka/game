import pygame


WIDTH, HEIGHT = SCREEN_SIZE = (640, 640)
FOLDER_OF_SPRITE = 'sprites'
FPS = 30
LEVEL_ID = 0
MAX_LEVEL = 3
IS_GAME_OVER = False
GAME_RUNNING = True
SCREEN = pygame.display.set_mode(SCREEN_SIZE)
CLOCK = pygame.time.Clock()
NOTHING = '-'
BRICK = 'b'
WATER = 'w'
GRASS = 'g'
