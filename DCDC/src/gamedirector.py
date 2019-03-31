import pygame
from pygame.locals import *

class GameDirector(object):
    def __init__(self, title, window_size, fps):
        #self.screen = pygame.display.set_mode((window_size[0], window_size[1]),RESIZABLE)
        self.screen = pygame.display.set_mode((window_size[0], window_size[1]))
        pygame.display.set_caption(title)
        self.fps = fps
        self.scene = None
        self.scenelist = {}
        self.quit_flag = False
        self.clock = pygame.time.Clock()
        self.frame = 0
        self.timesincestart = 0