import pygame
import math
from settings import *

class Hero(pygame.sprite.Sprite):
    def __init__(self, name, health, movement_speed, damage, forswing, backswing, flag_moving):
        super(Hero, self).__init__()
        self.name = name
        self.health = health
        self.movement_speed = movement_speed
        self.damage = damage
        self.foreswing = forswing
        self.backswing = backswing
        self.flag_moving = flag_moving

        self.hero_surface = pygame.transform.scale(
            pygame.image.load('heroes/hero 1.png').convert_alpha(), (HERO_HEIGHT, HERO_WIDTH)
        )
        # 以下两行只能名字叫做image和rect, 这是pygame定义的draw函数中规定的
        self.image = self.hero_surface
        self.rect = self.image.get_rect(center=(250, 400))

    def movement(self):
        # 每帧移动0.1秒, 更新后又重新定位为原来的位置, 所以一定要数值比1 大(能否为比1大的小数呢)
        # self.rect.y += 1
        # self.rect.x += 1
        mouse_click = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        global target_pos

        if mouse_click[2] and mouse_pos != self.rect.midbottom:
            target_pos = mouse_pos
            self.flag_moving = 1
        elif mouse_click[2] and mouse_pos == self.rect.midbottom:
            self.flag_moving = 0

        if self.flag_moving:
            y_distance = self.rect.midbottom[1] - target_pos[1]
            x_distance = self.rect.midbottom[0] - target_pos[0]

            y_speed = int(math.sqrt(
                math.pow(self.movement_speed, 2) / (math.pow((x_distance/y_distance),2)+1)
            )) if y_distance != 0 else 0
            x_speed = int(math.sqrt(
                math.pow(self.movement_speed, 2) / (math.pow((y_distance/x_distance),2)+1)
            )) if x_distance != 0 else 0

            if y_distance < 0:
                self.rect.y += y_speed
            elif y_distance > 0:
                self.rect.y -= y_speed
            if x_distance < 0:
                self.rect.x += x_speed
            elif x_distance > 0:
                self.rect.x -= x_speed
            # if abs(self.rect.x-target_pos[0]) < x_speed or \
            #         abs(self.rect.y-target_pos[1]) < y_speed:
            if math.sqrt(math.pow(self.rect.midbottom[0]-target_pos[0],2)+math.pow(self.rect.midbottom[1]-target_pos[1],2)) < self.movement_speed:
                self.rect.x = target_pos[0] - HERO_WIDTH/2
                self.rect.y = target_pos[1] - HERO_HEIGHT
            if self.rect.midbottom == target_pos:
                self.flag_moving = 0

    def attacking(self):
        pass

    def animation(self):
        pass

    def health_reduce(self, creep_damage):
        self.health -= creep_damage

    def attacking(self):
        pass

    def update(self):
        self.movement()
