import pygame
from settings import *
import math
import hero

class Creep_enemy(pygame.sprite.Sprite):
    def __init__(self, health, movement_speed, damage, foreswing, backswing, spawn_location):
        super(Creep_enemy, self).__init__()
        self.health = health
        self.movement_speed = movement_speed
        self.damage = damage
        self.foreswing = foreswing
        self.backswing = backswing

        self.creep_enemy_surface = pygame.transform.scale(
            pygame.image.load('assets/creep_enemy.png').convert_alpha(), (CREEP_HEIGHT, CREEP_WIDTH)
        )
        self.image = self.creep_enemy_surface
        self.rect = self.image.get_rect(center=(1500, spawn_location))

    def movement(self, hero_pos):
        distance_hero_creep = math.sqrt(math.pow(hero_pos[0] - self.rect.x, 2) + math.pow(hero_pos[1] - self.rect.y, 2))
        if 300 >= distance_hero_creep >= 60:
            self.creep_enemy_surface = pygame.transform.scale(
                pygame.image.load('assets/graphics/Player/jump.png').convert_alpha(), (60, 60)
            )
            self.image = self.creep_enemy_surface

            y_distance = self.rect.midbottom[1] - hero_pos[1]
            x_distance = self.rect.midbottom[0] - hero_pos[0]

            y_speed = int(math.sqrt(
                math.pow(self.movement_speed, 2) / (math.pow((x_distance / y_distance), 2) + 1)
            )) if y_distance != 0 else 0
            x_speed = int(math.sqrt(
                math.pow(self.movement_speed, 2) / (math.pow((y_distance / x_distance), 2) + 1)
            )) if x_distance != 0 else 0

            if y_distance < 0:
                self.rect.y += y_speed
            elif y_distance > 0:
                self.rect.y -= y_speed
            if x_distance < 0:
                self.rect.x += x_speed
            elif x_distance > 0:
                self.rect.x -= x_speed

        if distance_hero_creep < 60:
            pass

        else:
            self.creep_enemy_surface = pygame.transform.scale(
                pygame.image.load('assets/creep_enemy.png').convert_alpha(), (60, 60)
            )
            self.image = self.creep_enemy_surface
            self.rect.x -= self.movement_speed



    def draw_health_bar(self):
        health_bar_background = pygame.Rect(self.rect.midtop[0] - 32, self.rect.midtop[1] - 22, 64, 12)
        health_bar_content = pygame.Rect(self.rect.midtop[0] - 30, self.rect.midtop[1] - 20,
                                         60 * (self.health / CREEP_HEALTH), 8)
        pygame.draw.rect(screen, BLACK, health_bar_background)
        pygame.draw.rect(screen, RED, health_bar_content)

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

        if self.health <= 0:
            self.kill()

    def attack(self):
        pass


    def health_reduce(self, hero_damage):
        self.health -= hero_damage

    def update(self, hero_pos):
        self.movement(hero_pos)
        self.draw_health_bar()
        self.destroy()
