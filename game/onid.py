import pygame as pg
import sys
import time
import random

image_load_list = [["walk_1","걷기 1", (80, 80)], ["walk_2","걷기 2", (80, 80)], ["dino_image", "dino", (80,80)], ["obstacle_1", "가위괴물", (100, 100)], ["obstacle_2", "바위괴물", (100, 100)], ["obstacle_3", "보괴물", (100, 100)],  ["t_gameover", "게임오버_글자", (480,30)], ["gameover_image", "게임오버 다시하기", (88, 80)], ["die_image", "dino die" ,(80, 80)]]

for image_load in image_load_list:
    globals()[image_load[0]] = pg.transform.scale(pg.image.load("{}.PNG".format(image_load[1])), image_load[2])


random_obstacle_list = [(obstacle_1, (120, 100)), (obstacle_2, (90, 90)), (obstacle_3, (50, 100)) ]

screen = pg.display.set_mode((1000, 500))
pg.display.set_caption("Open source 9")

pg.init()
pg.key.set_repeat(1, 1)

collision_list = [(57, 53), (11, 75), (83, 14)]
dust_list = []

best_score = 0

def game_set():
    global walk_image, dino_x, dino_y, walk_image2, dust_list, game_speed , speed_up,  jump, jump_speed, add_obstacle, obstacle_list, die
    walk_image = 0
    dino_x = 50
    dino_y = 380
    walk_image2 = 0
    game_speed = 5
    speed_up = 0
    jump = False
    jump_speed = 0
    add_obstacle = 0
    obstacle_list = []
    die = False


def d_dino():
    global walk_image, walk_image2
    if die:
        screen.blit(die_image, (dino_x, dino_y))
    else:
        if jump:
            screen.blit(dino_image, (dino_x, dino_y))
        else:
            if walk_image % 2 == 1:
                screen.blit(walk_1, (dino_x, dino_y))
            else:
                screen.blit(walk_2, (dino_x, dino_y))
            if walk_image2 % 10 == 0:
                walk_image += 1

def u_dino():
    global  walk_image2
    walk_image2 += 1

def d_background():
    screen.fill((255,255,255))
    pg.draw.line(screen,(83,83,83),(0, 450), (1000, 450), 1)
    for dust in dust_list:
        pg.draw.line(screen,(83,83,83) ,(dust[0], dust[1]), (dust[0] + dust[2], dust[1]))


def u_obstacle():
    global add_obstacle
    if add_obstacle > random.randint(300, 400): # (obstacle_1, (150, 100))
        random_list = random_obstacle_list[random.randint(0, 3)]
        obstacle_list.append([random_list[0],[1000, random.randint(460, 470) - random_list[1][1]], random_list])
        add_obstacle = 0
    for obstacle in obstacle_list:
        if obstacle[1][0] < -200:
            obstacle_list.remove(obstacle)
        else:
            obstacle[1][0] -= game_speed
    add_obstacle += 1
    


def d_obstacle():
    for obstacle in obstacle_list:
        screen.blit(obstacle[0], obstacle[1])

def d_gameover():
    screen.blit(t_gameover ,(260, 154))
    screen.blit(gameover_image, (446, 240))

def check_collision():
    for collision_xy in collision_list:
        for obstacle in obstacle_list:
            if dino_x + collision_xy[0] > obstacle[1][0] and dino_x + collision_xy[0] < obstacle[1][0] + obstacle[2][1][0] and dino_y + collision_xy[1] > obstacle[1][1] and dino_y + collision_xy[1] < obstacle[1][1] + obstacle[2][1][1]:
                return True
def speed():
    global jump, jump_speed, speed_up, game_speed, dino_y
    if jump:
        dino_y -= jump_speed
        jump_speed -= 0.6
        if dino_y > 380:
            jump = False
    else:
        jump_speed = 0

    if not game_speed > 15:
        if speed_up % 1000 == 0:
            game_speed += 1
    speed_up += 1

def scissor():
    if obstacle[0] ==  obstacle_1 :
        


game_set()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
            sys.quit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                if not die:
                    scissor()
                else:
                    die = False
                    game_set()

    u_dino()
    d_background()
    d_obstacle()
    d_dino()

    if not die:

        u_obstacle()

        if check_collision():
            die = True

        speed()

    else:
        d_gameover()

    pg.display.update()

    time.sleep(0.008)