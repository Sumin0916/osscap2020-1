from matrix import *
import LED_display as LMD
import threading
import time
import random
import pygame as pg

pg.init()
screen = pg.display.set_mode((1, 1))

def LED_init():
    thread=threading.Thread(target=LMD.main, args=())
    thread.setDaemon(True)
    thread.start()
    return
def end_print(num):
    pass
    # if num == 1: 승리시 출력할 내용
    # elif num == 0 : 패배시 출력할 내용
#setpixel param from 1: red,green,yellow,blue,pink,cyan,white,red..
def show_boss_life(oScreen,Boss_life):
    Boss_life_array = [[21,21,21,21,21,21,21],[21,0,0,0,0,0,21],[21,21,21,21,21,21,21]]
    Boss_life -= 1
    for i in range(5):
        if (i <= Boss_life):
            Boss_life_array[1][1+i] = 11
    Boss_life = Matrix(Boss_life_array)
    Boss_tempBlk = iScreen.clip(0, 23, 0 + Boss_life.get_dy(), 23 + Boss_life.get_dx())
    Boss_tempBlk = Boss_tempBlk + Boss_life
    oScreen.paste(Boss_tempBlk, 0, 23)
def draw_led(m):
    array = m.get_array()
    for y in range(m.get_dy()):
        for x in range(m.get_dx()):
            if 1 <= array[y][x] <= 10: ## 초록색 출력
                LMD.set_pixel(x,y, 2)
            elif array[y][x] == 0: ## 0이면 공백 출력
                LMD.set_pixel(x,y,0)
            elif 11 <= array[y][x] <= 20:  ## 빨간색 출력
                LMD.set_pixel(x,y,1)
            elif 21 <= array[y][x] <= 30:  ## 노란색 출력
                LMD.set_pixel(x,y,3)
            elif 31 <= array[y][x] <= 40:  ## cyan
                LMD.set_pixel(x,y,7)
def set_array_mon(set_mon_num):
    if set_mon_num == 1:  # scissor
        mon_Blk = [[0, 0, 1, 0, 1, 0, 0, 0],
                   [0, 0, 1, 0, 1, 0, 0, 0],
                   [0, 0, 1, 0, 1, 0, 0, 0],
                   [0, 0, 1, 1, 1, 1, 0, 0],
                   [0, 0, 1, 0, 0, 0, 1, 0],
                   [0, 1, 0, 0, 1, 0, 0, 1],#core: [5][4]
                   [0, 0, 1, 0, 0, 0, 1, 0],
                   [0, 0, 0, 1, 1, 1, 0, 0]]
    elif set_mon_num == 2:  # rock
        mon_Blk = [[0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 1, 1, 1, 1, 1, 0],
                   [0, 1, 1, 0, 0, 0, 1, 1],
                   [0, 1, 0, 0, 1, 0, 0, 1],#core: [5][4]
                   [0, 0, 1, 0, 0, 0, 1, 1],
                   [0, 0, 0, 1, 1, 1, 0, 0]]
    elif set_mon_num == 3:  # paper
        mon_Blk = [[0, 0, 0, 1, 0, 1, 0, 0],
                   [0, 1, 0, 1, 0, 1, 0, 0],
                   [0, 1, 0, 1, 0, 1, 0, 1],
                   [0, 1, 0, 1, 1, 1, 0, 1],
                   [0, 0, 1, 0, 0, 0, 1, 0],
                   [1, 0, 1, 0, 1, 0, 1, 1],#core: [5][4]
                   [0, 1, 1, 0, 0, 0, 1, 0],
                   [0, 0, 0, 1, 1, 1, 0, 0]]
    else:
        mon_Blk = [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]
    return mon_Blk
def die_mon(ArrayScreen):
    effect_list = [[[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]],
                ##
                [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 1, 0, 0, 0],
                [0, 0, 0, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]],
                ##
                [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 1, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]],
                ##
                [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 1, 1, 0],
                [0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 1, 1, 0, 1, 0],
                [0, 0, 1, 0, 0, 1, 0, 0],
                [0, 1, 0, 1, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]],
                ##
                [[0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 0, 0, 0, 1, 1, 0],
                [0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 1, 0, 0],
                [0, 1, 0, 0, 0, 1, 0, 0],
                [1, 0, 0, 0, 1, 0, 1, 0]],
                ##
                [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 1, 0, 0],
                [1, 0, 0, 0, 0, 0, 1, 0]],
                ##
                [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 1, 0]],
                ##
                [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]]
    for i in range(8):
        effect = Matrix(effect_list[i])
        iScreen = Matrix(ArrayScreen);oScreen = Matrix(iScreen)
        tempBlk = iScreen.clip(6, 22, 6 + effect.get_dy(), 22 + effect.get_dx());tempBlk = tempBlk + effect
        iScreen.paste(tempBlk, 6, 22)            
        draw_led(oScreen)
        time.sleep(0.3)
def prograss(array,score):
    if (score <= 9):
        array[3][20+score] = 1
def show_life(array,hero_life):
    count = 0
    array[1][1] = 0;array[1][3] = 0;array[1][5] = 0;array[1][7] = 0;array[1][9] = 0
    num_array = [1,3,5,7,9] 
    for i in num_array:
        array[1][i] = 11
        count += 1
        if count >= hero_life:
            break
def show_hand(array,key):
    array[9][8] = 0;array[7][9] = 0;array[9][9] = 0;array[7][8] = 0;array[8][9] = 0;array[10][8] = 0;array[10][9] = 0
    if key == 'rock':
        array[7][8] = 31;array[7][9] = 31;array[8][9] = 31
    elif key == 'paper':
        array[7][8] = 31;array[7][9] = 31;array[8][9] = 31;array[9][8] = 31;array[9][9] = 31
    elif key == 'scissor':
        array[7][9] = 31;array[9][9] = 31
def hero_hit_react(array):
    for _ in range(3):
        array[4][4] = 0;array[4][5] = 0;array[5][3] = 0;array[5][6] = 0;array[6][3] = 0;array[6][6] = 0;array[7][4] = 0;array[7][5] = 0;array[14][2] = 0;array[14][6] = 0
        array[8][3] = 0;array[8][4] = 0;array[8][5] = 0;array[8][6] = 0;array[8][7] = 0;array[8][8] = 0;array[9][2] = 0;array[9][4] = 0;array[9][5] = 0
        array[10][2] = 0;array[10][4] = 0;array[10][5] = 0;array[11][4] = 0;array[11][5] = 0;array[12][4] = 0;array[12][6] = 0;array[13][3] = 0;array[13][6] = 0
        array[8][9] = 0;array[7][8] = 0;array[7][9] = 0;array[9][8] = 0;array[9][9] = 0
        iScreen = Matrix(array);oScreen = Matrix(iScreen)
        draw_led(oScreen)
        time.sleep(0.2)
        array[4][4] = 31;array[4][5] = 31;array[5][3] = 31;array[5][6] = 31;array[6][3] = 31;array[6][6] = 31;array[7][4] = 31;array[7][5] = 31;array[14][2] = 31;array[14][6] = 31
        array[8][3] = 31;array[8][4] = 31;array[8][5] = 31;array[8][6] = 31;array[8][7] = 31;array[8][8] = 31;array[9][2] = 31;array[9][4] = 31;array[9][5] = 31
        array[10][2] = 31;array[10][4] = 31;array[10][5] = 31;array[11][4] = 31;array[11][5] = 31;array[12][4] = 31;array[12][6] = 31;array[13][3] = 31;array[13][6] = 31
        iScreen = Matrix(array);oScreen = Matrix(iScreen)
        draw_led(oScreen)
        time.sleep(0.2) # 31
def Boss_hit_react(array,Boss_array):
    Boss_hit_array = [[0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0]]
    for _ in range(3):
        effect = Matrix(Boss_hit_array)
        iScreen = Matrix(ArrayScreen);oScreen = Matrix(iScreen)
        tempBlk = iScreen.clip(8, 21, 8 + effect.get_dy(), 21 + effect.get_dx());tempBlk = tempBlk + effect
        iScreen.paste(tempBlk, 8, 21)
        draw_led(oScreen)
        time.sleep(0.2)
        effect = Matrix(Boss_array)
        iScreen = Matrix(ArrayScreen);oScreen = Matrix(iScreen)
        tempBlk = iScreen.clip(8, 21, 8 + effect.get_dy(), 21 + effect.get_dx());tempBlk = tempBlk + effect
        iScreen.paste(tempBlk, 8, 21)
        draw_led(oScreen)
        time.sleep(0.2)
iScreenDy = 14;iScreenDx = 30;iScreenDw = 1;top = 6;left = 22
def set_score (score):
    if score == 0:
        score_Blk = [
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 1, 1, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 1, 1, 1, 0, 0, 0]]
    elif score == 1:
        score_Blk = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 1, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 1, 1, 0, 0]]
    elif score == 2:
        score_Blk = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 1, 1, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 1, 1, 1, 0, 0],
                    [0, 0, 0, 1, 1, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 1, 1, 1, 0]]
    elif score == 3:
        score_Blk = [[0, 0, 0, 1, 1, 1, 0, 0, 0],
                     [0, 0, 1, 0, 0, 0, 1, 0, 0],
                     [0, 0, 1, 0, 0, 0, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 1, 0, 0],
                     [0, 0, 0, 0, 1, 1, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 1, 0, 0],
                     [0, 0, 1, 0, 0, 0, 1, 0, 0],
                     [0, 0, 1, 0, 0, 0, 1, 0, 0],
                     [0, 0, 0, 1, 1, 1, 0, 0, 0]]
    elif score == 4:
        score_Blk = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 1, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0]]
    elif score == 5:
        score_Blk = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 1, 1, 1, 0, 0, 0]]
    elif score == 6:
        score_Blk = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 1, 0, 0, 0],
           [0, 0, 0, 0, 1, 0, 0, 0, 0],
           [0, 0, 0, 1, 0, 0, 0, 0, 0],
           [0, 0, 1, 1, 1, 1, 0, 0, 0],
           [0, 0, 1, 0, 0, 0, 1, 0, 0],
           [0, 0, 1, 0, 0, 0, 1, 0, 0],
           [0, 0, 1, 0, 0, 0, 1, 0, 0],
           [0, 0, 0, 1, 1, 1, 0, 0, 0]]
    elif score == 7:
        score_Blk = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 1, 1, 1, 1, 1, 0, 0],
             [0, 0, 1, 0, 0, 0, 1, 0, 0],
             [0, 0, 1, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 0, 0, 0]]
    elif score == 8:
        score_Blk = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 1, 1, 0, 0, 0],
             [0, 0, 1, 0, 0, 0, 1, 0, 0],
             [0, 0, 1, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 1, 1, 1, 0, 0, 0],
             [0, 0, 1, 0, 0, 0, 1, 0, 0],
             [0, 0, 1, 0, 0, 0, 1, 0, 0],
             [0, 0, 1, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 1, 1, 1, 0, 0, 0]]
    elif score == 9:
        score_Blk = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0]]
    return score_Blk
Gun = [[11, 11]]
Boss = [[0,11,0,0,0,0,0,0,0,11,0],
        [0,11,11,0,0,0,0,0,11,11,0],
        [0,11,11,1,1,1,1,1,11,11,0],
        [0,0,1,1,1,1,1,1,1,0,0],
        [0,0,1,1,0,0,0,1,1,0,0],
        [0,0,0,0,0,0,0,1,1,0,0],
        [0,0,0,0,0,0,1,1,0,0,0],
        [0,0,0,0,0,1,1,0,0,0,0],
        [0,0,0,0,1,1,0,0,0,0,0],
        [0,0,0,0,1,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,1,1,0,0,0,0,0],
        [0,0,0,0,1,1,0,0,0,0,0]]
thinking_Boss = [[0,11,0,0,0,0,0,0,0,11,0],
                [0,11,11,0,0,0,0,0,11,11,0],
                [0,11,11,1,1,1,1,1,11,11,0],
                [0,0,1,1,1,1,1,1,1,0,0],
                [0,0,1,1,0,0,0,1,1,0,0],
                [0,0,0,0,0,0,0,1,1,0,0],
                [0,0,0,0,0,0,1,1,0,0,0],
                [0,1,0,0,0,1,1,0,1,1,0],
                [1,0,1,0,1,1,0,1,0,0,1],
                [0,0,1,0,1,1,0,0,0,1,0],
                [0,1,0,0,0,0,0,0,1,0,0],
                [0,0,0,0,1,1,0,0,0,0,0],
                [0,1,0,0,1,1,0,0,1,0,0]]
ArrayScreen = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 21, 0, 21, 0, 21, 0, 21, 0, 21, 0, 0, 0, 0, 0, 0, 0, 0, 21, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 11, 1], 
    [1, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 0, 0, 0, 0, 0, 0, 0, 0, 21, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 11, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 0, 1],
    [1, 0, 0, 0, 31, 31, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 1],
    [1, 0, 0, 31, 0, 0, 31, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 31, 0, 0, 31, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 31, 31, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 31, 31, 31, 31, 31, 31, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 31, 0, 31, 31, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 31, 0, 31, 31, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 31, 31, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], #총 Y축
    [1, 0, 0, 0, 31, 0, 31, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 31, 0, 0, 31, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 31, 0, 0, 0, 31, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
ScoreScreen =[
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
hero_life = 5;G_time = 0.6;score = 0;temp_key = 0
LED_init()
while (hero_life > 0):
    G_top = 11;G_left = 25;Boss_top = 8;Boss_left = 21;key = 0
    prograss(ArrayScreen,score);show_life(ArrayScreen,hero_life);show_hand(ArrayScreen,temp_key)
    iScreen = Matrix(ArrayScreen);oScreen = Matrix(iScreen)
    set_mon_num = random.randint(1, 3)
    curr_mon = Matrix(set_array_mon(set_mon_num))
    tempBlk = iScreen.clip(top, left, top + curr_mon.get_dy(), left + curr_mon.get_dx());tempBlk = tempBlk + curr_mon
    iScreen.paste(tempBlk, top, left)
    if (score != 10):
        while (G_left >= 5):
            GunBlk = Matrix(Gun)
            oScreen = Matrix(iScreen)
            G_tempBlk = iScreen.clip(G_top, G_left, G_top + GunBlk.get_dy(), G_left + GunBlk.get_dx())
            G_tempBlk = G_tempBlk + GunBlk
            oScreen.paste(G_tempBlk, G_top, G_left)
            draw_led(oScreen)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == ord('q'):
                        key = 'quit'
                    if event.key == ord('a'):
                        key = 'scissor'
                        temp_key = 'scissor'
                    if event.key == ord('s'):
                        key = 'rock'
                        temp_key = 'rock'
                    if event.key == ord('d'):
                        key = 'paper'
                        temp_key = 'paper'
            if key == 'quit':
                hero_life = 0
                break
            elif key == 'scissor':  # 가위
                if (set_mon_num == 3):
                    G_time = 0.8*G_time
                    score += 1
                    curr_mon = Matrix(set_array_mon(4))
                    tempBlk = iScreen.clip(top, left, top + curr_mon.get_dy(), left + curr_mon.get_dx());tempBlk = tempBlk + curr_mon
                    iScreen.paste(tempBlk, top, left)
                    die_mon(ArrayScreen)
                    break
            elif key == 'rock':  # 바위
                if (set_mon_num == 1):
                    G_time = 0.8*G_time
                    score += 1
                    curr_mon = Matrix(set_array_mon(4))
                    tempBlk = iScreen.clip(top, left, top + curr_mon.get_dy(), left + curr_mon.get_dx());tempBlk = tempBlk + curr_mon
                    iScreen.paste(tempBlk, top, left)
                    die_mon(ArrayScreen)
                    break
            elif key == 'paper':  # 보
                if (set_mon_num == 2):
                    G_time = 0.8*G_time
                    score += 1
                    curr_mon = Matrix(set_array_mon(4))
                    tempBlk = iScreen.clip(top, left, top + curr_mon.get_dy(), left + curr_mon.get_dx());tempBlk = tempBlk + curr_mon
                    iScreen.paste(tempBlk, top, left)
                    die_mon(ArrayScreen)
                    break
            if (G_left == 5): #총알이 닿으면 피 1 깎임
                hero_life -= 1
                hero_hit_react(ArrayScreen)
                set_mon_num = random.randint(1, 3)
                curr_mon = Matrix(set_array_mon(set_mon_num))
                tempBlk = iScreen.clip(top, left, top + curr_mon.get_dy(), left + curr_mon.get_dx());tempBlk = tempBlk + curr_mon
                iScreen.paste(tempBlk, top, left)
                break
            elif (hero_life <= 0):
                end_print(0)
                time.sleep(3)
                break
            G_left -= 1 #총알 움직임
            time.sleep(G_time)
#############################################BOSS###################################################
    else :
        G_time = 1 #다시 게임시간 간격 원래대로 조정
        Boss_life = 5
        temp_key = 0
        for i in range(1,5):
            if (1<= i <= 2):
                ArrayScreen[i][19] = 0;ArrayScreen[i][29] = 0;ArrayScreen[i][30] = 0
            elif (i == 3):
                for j in range(19,31):
                    ArrayScreen[i][j] = 0
            elif (i == 4):
                for j in range(19,31):
                    ArrayScreen[i][j] = 0 # ArrayScreen 진행바 청소
        while(True):
            show_life(ArrayScreen,hero_life);show_hand(ArrayScreen,temp_key)
            iScreen = Matrix(ArrayScreen);oScreen = Matrix(iScreen)
            BossBlk = Matrix(thinking_Boss)
            Boss_tempBlk = iScreen.clip(Boss_top, Boss_left, Boss_top + BossBlk.get_dy(), Boss_left + BossBlk.get_dx())
            Boss_tempBlk = Boss_tempBlk + BossBlk
            oScreen.paste(Boss_tempBlk, Boss_top, Boss_left)
            show_boss_life(oScreen,Boss_life)
            draw_led(oScreen)
            Boss_pick = random.randint(1, 3)
            time.sleep(2)
            BossBlk = Matrix(Boss)
            Boss_tempBlk = iScreen.clip(Boss_top, Boss_left, Boss_top + BossBlk.get_dy(), Boss_left + BossBlk.get_dx())
            Boss_tempBlk = Boss_tempBlk + BossBlk
            oScreen.paste(Boss_tempBlk, Boss_top, Boss_left)
            show_boss_life(oScreen,Boss_life)
            draw_led(oScreen)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == ord('q'):
                        key = 'quit'
                    if event.key == ord('a'):
                        key = 'scissor'
                        temp_key = 'scissor'
                    if event.key == ord('s'):
                        key = 'rock'
                        temp_key = 'rock'
                    if event.key == ord('d'):
                        key = 'paper'
                        temp_key = 'paper'
            if key == 'quit':
                hero_life = 0
                break
            elif key == 'scissor':
                if (Boss_pick == 3):
                    Boss_hit_react(ArrayScreen,Boss)
                    Boss_life -= 1
                    score += 1
                else:
                    hero_hit_react(ArrayScreen)
                    hero_life -= 1
            elif key == 'rock':
                if (Boss_pick == 1):
                    Boss_hit_react(ArrayScreen,Boss)
                    Boss_life -= 1
                    score += 1
                else:
                    hero_hit_react(ArrayScreen)
                    hero_life -= 1
            elif key == 'paper':
                if (Boss_pick == 2):
                    Boss_hit_react(ArrayScreen,Boss)
                    Boss_life -= 1
                    score += 1
                else:
                    hero_hit_react(ArrayScreen)
                    hero_life -= 1
            if (Boss_life == 1):
                for i in range(13):
                    for j in range(11):
                        if (Boss[i][j] >= 0):
                            Boss[i][j] = 11
                            thinking_Boss[i][j] = 11
            elif (Boss_life == 3):
                for i in range(13):
                    for j in range(11):
                        if (Boss[i][j] >= 0):
                            Boss[i][j] = 21
                            thinking_Boss[i][j] = 21
            if (hero_life <= 0):
                end_print(0)
                time.sleep(3)
                break
            elif (Boss_life <= 0):
                score += 10
                end_print(1)
                time.sleep(3)
                break
    if (hero_life <= 0):
        score += hero_life * 3
        score_10 = score // 10;score_1 = score % 10
        score_10_left = 8;score_10_top = 4;score_1_left = 15;score_1_top = 4
        SiScreen = Matrix(ScoreScreen);SoScreen = Matrix(SiScreen)
        currBlk_1 = Matrix(set_score(score_1));currBlk_10 = Matrix(set_score(score_10))
        tempBlk_1 = SiScreen.clip(score_1_top, score_1_left, score_1_top + currBlk_1.get_dy(), score_1_left + currBlk_1.get_dx());tempBlk_1 = tempBlk_1 + currBlk_1
        tempBlk_10 = SiScreen.clip(score_10_top, score_10_left, score_10_top + currBlk_10.get_dy(),score_10_left + currBlk_10.get_dx());tempBlk_10 = tempBlk_10 + currBlk_10
        SoScreen.paste(tempBlk_1, score_1_top, score_1_left);SoScreen.paste(tempBlk_10, score_10_top, score_10_left)
        draw_led(SoScreen)
        break