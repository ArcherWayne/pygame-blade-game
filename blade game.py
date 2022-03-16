import random
import pygame
from settings import *
from hero import Hero
from creep_enemy import Creep_enemy

# from creep_hero import Creep_hero

def display_time():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    time_surface = font.render(f'Time:{current_time}', False, (64, 64, 64))
    time_rect = time_surface.get_rect(center=(WIN_WIDTH / 2, 100))
    screen.blit(time_surface, time_rect)


def collision_hero_creep_enemy():
    c_list = pygame.sprite.spritecollide(hero.sprite, creep_enemy_group, False)
    if c_list:
        hero.sprite.health_reduce(c_list[0].damage)
        print(hero.sprite.health)
        # .后面没有所需要的参数是因为pycharm编辑器
        # 血量为零 游戏停止
        if hero.sprite.health <= 0:
            creep_enemy_group.empty()
            return False
    return True


def loadingscreen():
    loadingscreen_surface = pygame.transform.scale(
        pygame.image.load(random.choice(
            ['loadingscreen/wallhaven (1).jpg',
             'loadingscreen/wallhaven (1).png',
             'loadingscreen/wallhaven (2).jpg',
             'loadingscreen/wallhaven (2).png',
             'loadingscreen/wallhaven (3).jpg',
             'loadingscreen/wallhaven (3).png',
             'loadingscreen/wallhaven (4).jpg',
             'loadingscreen/wallhaven (5).jpg']
        )).convert(), (WIN_WIDTH, WIN_HEIGTH)
    )
    loadingscreen_rect = loadingscreen_surface.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGTH / 2))
    screen.blit(loadingscreen_surface, loadingscreen_rect)


pygame.init()

# background
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGTH))
pygame.display.set_caption('blade game')
pygame.display.set_icon(pygame.image.load('assets/blade game.png'))
background_surface = pygame.transform.scale(
    pygame.image.load('assets/ground.png').convert(), (WIN_WIDTH, WIN_HEIGTH))
background_rect = background_surface.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGTH / 2))
clock = pygame.time.Clock()
font = pygame.font.Font('font/Pixeltype.ttf', 50)

# Groups
hero = pygame.sprite.GroupSingle()  # 定义hero这样一个单group 用来放玩家角色
hero.add(Hero('example hero', 110, 10, 20, 0.3, 0.1, 0))  # 在hero这个group中添加Hero这个类, 之后, 这个group中就有了这个类的实例
# __init__(self, name, health, movement_speed, damage, forswing, backswing, flag_moving)
creep_enemy_group = pygame.sprite.Group()

creep_enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(creep_enemy_timer, 3000)


def main():
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
                        creep_enemy_group.add(Creep_enemy(50, 3, random.randint(19, 25), 0.4, 0.2, 200 + i * 80))
                    # __init__(self, health, movement_speed, damage, forswing, backswing)
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    game_active = True
                    hero.sprite.health = 110  # 重置血量
                    start_time = int(pygame.time.get_ticks() / 1000)

        # actual game loop
        if game_active:
            screen.fill((255, 255, 255))
            screen.blit(background_surface, background_rect)

            # tuple 鼠标按键和鼠标位置
            hero.draw(screen)
            hero.update()

            # print(hero.sprite.rect.x, hero.sprite.rect.y)
            creep_enemy_group.draw(screen)
            creep_enemy_group.update([hero.sprite.rect.x, hero.sprite.rect.y])
            # update实际上是类的成员函数的集合, 调用了update函数就相当于调用了类里面update函数下所有的成员函数

            display_time()
            game_active = collision_hero_creep_enemy()

        else:
            screen.fill((94, 129, 162))
            # hero.

            # loadingscreen()

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
