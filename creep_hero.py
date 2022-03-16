import pygame

class Creep_hero(pygame.sprite.Sprite):
    def __init__(self, health, movement_speed, damage, forswing, backswing):
        super(Creep_hero, self).__init__()
        self.health = health
        self.movement_speed = movement_speed
        self.damage = damage
        self.foreswing = forswing
        self.backswing = backswing

    def movement(self):
        pass

    def seek(self):
        pass

    def update(self):
        pass

