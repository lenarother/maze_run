# MR review on 26.02.2016
# I like that itis short and can be well understood only base on reading
# Does not run: pygame.error: Couldn't open tiles.xpm
# Order of imports changed as in PEP8 (with isort)
# pylint complains about variable names
# .gitignore and requirements.pip could be added to the repo 
import pygame
from pygame import Rect

from draw_map import draw_map, level
from event_loop import event_loop
from load_tiles import load_tiles
from moves import move

pygame.init()
pygame.display.set_mode((640, 400))
display = pygame.display.get_surface()


DIRECTIONS = {
    276: 'LEFT', 275: 'RIGHT',
    273: 'UP', 274: 'DOWN'
}


def game(key):
    """Handles key events in the game"""
    move(level, DIRECTIONS.get(key, 0))
    map_img = draw_map(level, tile_img, tiles)
    display.blit(map_img, Rect((0, 0, 224, 224)), Rect((0, 0, 224, 224)))
    pygame.display.update()


if __name__ == '__main__':
    tile_img, tiles = load_tiles()
    map_img = draw_map(level, tile_img, tiles)
    display.blit(map_img, Rect((0, 0, 224, 224)), Rect((0, 0, 224, 224)))
    pygame.display.update()
    event_loop(game)
