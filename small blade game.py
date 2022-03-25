from settings import *
import pygame
import math


class Hero(pygame.sprite.Sprite):
    def __init__(self, name, health, movement_speed, damage, foreswing, backswing, flag_moving):
        super(Hero, self).__init__()
        self.name = name
        self.health = health
        self.movement_speed = movement_speed
        self.damage = damage
        self.foreswing = foreswing
        self.backswing = backswing
        self.flag_moving = flag_moving

        self.hero_surface = pygame.transform.scale(
            pygame.image.load('assets/graphics/heroes/hero 45.png').convert_alpha(), (HERO_HEIGHT, HERO_WIDTH)
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
            # if abs(self.rect.x-target_pos[0]) < x_speed or \
            #         abs(self.rect.y-target_pos[1]) < y_speed:
            if math.sqrt(math.pow(self.rect.midbottom[0] - target_pos[0], 2) + math.pow(
                    self.rect.midbottom[1] - target_pos[1], 2)) < self.movement_speed:
                self.rect.x = target_pos[0] - HERO_WIDTH / 2
                self.rect.y = target_pos[1] - HERO_HEIGHT
            if self.rect.midbottom == target_pos:
                self.flag_moving = 0

    def attack(self):
        pass

    def animation(self):
        if self.flag_moving == 1:
            pass

    def draw_health_bar(self):
        health_bar_background = pygame.Rect(self.rect.midtop[0] - 42, self.rect.midtop[1] - 22, 84, 12)
        health_bar_content = pygame.Rect(self.rect.midtop[0] - 40, self.rect.midtop[1] - 20,
                                         80 * (self.health / HERO_HEALTH), 8)
        pygame.draw.rect(screen, BLACK, health_bar_background)
        pygame.draw.rect(screen, RED, health_bar_content)

    def health_reduce(self, creep_damage):
        self.health -= creep_damage

    def update(self):
        self.draw_health_bar()
        self.movement()


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
            hero.draw(screen)
            hero.update()
            creep_enemy_group.draw(screen)
            creep_enemy_group.update(hero.sprite.rect.midbottom)
            # update实际上是类的成员函数的集合, 调用了update函数就相当于调用了类里面update函数下所有的成员函数

            # game_active = collision_hero_creep_enemy()
            if hero.sprite.health <= 0: game_active = 0

        else:
            screen.fill((94, 129, 162))

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()