import pygame


FOLDER_OF_SPRITE = 'sprites'


def create_sprite(sprite):
    return pygame.image.load('{}\\{}'.format(FOLDER_OF_SPRITE, sprite))


player_w = create_sprite('tank_w.png')
player_a = create_sprite('tank_a.png')
player_s = create_sprite('tank_s.png')
player_d = create_sprite('tank_d.png')
bullet = create_sprite('bullet.png')
grass = create_sprite('grass.png')
brick = create_sprite('brick.png')
water = create_sprite('water.png')
