import math
import random

import pygame
from random import randint


class Creep_enemy(pygame.sprite.Sprite):
    def __init__(self, health, movement_speed, damage, forswing, backswing, spawn_location):
        super(Creep_enemy, self).__init__()
        self.health = health
        self.movement_speed = movement_speed
        self.damage = damage
        self.foreswing = forswing
        self.backswing = backswing

        self.creep_enemy_surface = pygame.transform.scale(
            pygame.image.load('assets/creep_enemy.png').convert_alpha(), (60, 60)
        )
        self.image = self.creep_enemy_surface
        self.rect = self.image.get_rect(center=(1500, spawn_location))

    def movement(self, hero_pos):
        distance_hero_creep = math.sqrt(math.pow(hero_pos[0] - self.rect.x, 2) + math.pow(hero_pos[1] - self.rect.y, 2))
        if distance_hero_creep <= 300:

            self.creep_enemy_surface = pygame.transform.scale(
                pygame.image.load('assets/graphics/Player/jump.png').convert_alpha(), (60, 60)
            )
            self.image = self.creep_enemy_surface

            y_distance = self.rect.midbottom[1] - hero_pos[1]
            x_distance = self.rect.midbottom[0] - hero_pos[0]

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

        else:
            self.creep_enemy_surface = pygame.transform.scale(
                pygame.image.load('assets/creep_enemy.png').convert_alpha(), (60, 60)
            )
            self.image = self.creep_enemy_surface
            self.rect.x -= self.movement_speed


    def seek(self):
        pass

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

    def update(self, hero_pos):
        self.movement(hero_pos)
        self.destroy()