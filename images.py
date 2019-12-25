import pygame
from global_perms import FOLDER_OF_SPRITE


def add_image(image_name, file_name):
    images[image_name] = pygame.image.load('{}\\{}'.format(FOLDER_OF_SPRITE, file_name))


images = {}
add_image('player_w', 'tank_w.png')
add_image('player_a', 'tank_a.png')
add_image('player_s', 'tank_s.png')
add_image('player_d', 'tank_d.png')
add_image('enemy_w', 'enemy_w.png')
add_image('enemy_a', 'enemy_a.png')
add_image('enemy_s', 'enemy_s.png')
add_image('enemy_d', 'enemy_d.png')
add_image('bullet', 'bullet.png')
add_image('grass', 'grass.png')
add_image('brick', 'brick.png')
add_image('water', 'water.png')
add_image('base', 'base.png')
add_image('destroyed_base', 'destroyed_base.png')
