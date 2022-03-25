import random
import pygame
from settings import *
from tower import Tower
from hero import Hero
from creep_enemy import Creep_enemy


# from creep_hero import Creep_hero

def display_time(start_time):
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    time_surface = font.render(f'Time:{current_time}', False, (64, 64, 64))
    time_rect = time_surface.get_rect(center=(WIN_WIDTH / 2, 100))
    screen.blit(time_surface, time_rect)
    return current_time


def loadingscreen():
    loadingscreen_surface = pygame.transform.scale(
        pygame.image.load('assets/loadingscreen/dota2-loadingscreen.png').convert(), (WIN_WIDTH, WIN_HEIGTH))
    loadingscreen_rect = loadingscreen_surface.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGTH / 2))
    screen.blit(loadingscreen_surface, loadingscreen_rect)
    endinfo_surface = font.render(f'HEI JI BAAAA', False, (115, 34, 16))
    endinfo_rect = endinfo_surface.get_rect(center=(WIN_WIDTH / 2, 100))
    screen.blit(endinfo_surface, endinfo_rect)


def collision_hero_creep_enemy():
    c_list = pygame.sprite.spritecollide(hero.sprite, creep_enemy_group, False)
    if c_list:
        hero.sprite.health_reduce(c_list[0].damage)
        c_list[0].health_reduce(hero.sprite.damage)
        print(hero.sprite.health)
        print(c_list[0].health)

pygame.init()

# background
pygame.display.set_caption('blade game')
pygame.display.set_icon(pygame.image.load('assets/blade game.png'))
background_surface = pygame.transform.scale(
    pygame.image.load('assets/ground.png').convert(), (WIN_WIDTH, WIN_HEIGTH))
background_rect = background_surface.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGTH / 2))
clock = pygame.time.Clock()
font = pygame.font.Font('assets/font/Pixeltype.ttf', 50)

# Groups
hero = pygame.sprite.GroupSingle()  # 定义hero这样一个单group 用来放玩家角色
hero.add(Hero('example hero', HERO_HEALTH, HERO_MOVEMENT_SPEED, HERO_DAMAGE, HERO_FORESWING, HERO_BACKSWING,
              0))  # 在hero这个group中添加Hero这个类, 之后, 这个group中就有了这个类的实例
creep_enemy_group = pygame.sprite.Group()
tower = pygame.sprite.Group()
tower.add(Tower(TOWER_HEALTH, TOWER_DAMAGE))
# tower2 = tower.add(Tower(TOWER_HEALTH, TOWER_DAMAGE))

creep_enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(creep_enemy_timer, 3000)


def main():
    # time = 0
    start_time = 0
    game_active = True
    while True:
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(

                )
            if game_active:
                if event.type == creep_enemy_timer:
                    for i in range(5):
                        creep_enemy_group.add(
                            Creep_enemy(CREEP_HEALTH, CREEP_MOVEMENT_SPEED, CREEP_DAMAGE, CREEP_FORESWING,
                                        CREEP_BACKSWING, 200 + i * 80))
                if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                    hero.sprite.health = 0
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    game_active = True
                    hero.sprite.rect.midbottom = (250, 400)
                    hero.sprite.health = HERO_HEALTH  # 重置血量
                    start_time = int(pygame.time.get_ticks() / 1000)

        # actual game loop
        if game_active:
            screen.fill((255, 255, 255))
            screen.blit(background_surface, background_rect)

            # tuple 鼠标按键和鼠标位置
            tower.draw(screen)
            tower.update()
            hero.draw(screen)
            hero.update()
            creep_enemy_group.draw(screen)
            creep_enemy_group.update(hero.sprite.rect.midbottom)
            # update实际上是类的成员函数的集合, 调用了update函数就相当于调用了类里面update函数下所有的成员函数

            time = display_time(start_time)
            collision_hero_creep_enemy()
            # game_active = collision_hero_creep_enemy()
            if hero.sprite.health <= 0: game_active = 0

        else:
            screen.fill((94, 129, 162))
            loadingscreen()

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
