import pygame
from settings import *
import math

class Tower(pygame.sprite.Sprite):
    def __init__(self, health, damage):
        super(Tower, self).__init__()
        self.health = health
        self.damage = damage
        self.tower_surface = pygame.transform.scale(
            pygame.image.load('assets/graphics/tower/tower.png').convert_alpha(), (TOWER_WIDTH, TOWER_HEIGHT)
        )
        # 以下两行只能名字叫做image和rect, 这是pygame定义的draw函数中规定的
        self.image = self.tower_surface
        self.rect = self.image.get_rect(center=(200, 600))

    def update(self):
        pass