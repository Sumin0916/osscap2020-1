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

#setpixel param from 1: red,green,yellow,blue,pink,cyan,white,red..
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
    return mon_Blk

def prograss(array,score):
    if (score <= 9):
        array[3][20+score] = 1 ## 22부터 30까지
def show_life(array,life):
    count = 0
    array[1][1] = 0;array[1][3] = 0;array[1][5] = 0;array[1][7] = 0;array[1][9] = 0;
    num_array = [1,3,5,7,9] #1, 3, 5, 7, 9
    for i in num_array:
        array[1][i] = 11
        count += 1
        if count >= life:
            break
def show_hand(array,key):
    array[9][8] = 0;array[7][9] = 0;array[9][9] = 0;array[7][8] = 0;array[8][9] = 0;array[10][8] = 0;array[10][9] = 0
    if key == 'rock':
        array[7][8] = 31;array[7][9] = 31;array[8][9] = 31
    elif key == 'paper':
        array[7][8] = 31;array[7][9] = 31;array[8][9] = 31;array[9][8] = 31;array[9][9] = 31
    elif key == 'scissor':
        array[7][9] = 31;array[9][9] = 31 # hand[8][8]
def hit_react(array):
    for _ in range(3):
        array[4][4] = 0;array[4][5] = 0;array[5][3] = 0;array[5][6] = 0;array[6][3] = 0;array[6][6] = 0;array[7][4] = 0;array[7][5] = 0;array[14][2] = 0;array[14][6] = 0
        array[8][3] = 0;array[8][4] = 0;array[8][5] = 0;array[8][6] = 0;array[8][7] = 0;array[8][8] = 0;array[9][2] = 0;array[9][4] = 0;array[9][5] = 0
        array[10][2] = 0;array[10][4] = 0;array[10][5] = 0;array[11][4] = 0;array[11][5] = 0;array[12][4] = 0;array[12][6] = 0;array[13][3] = 0;array[13][6] = 0
        array[8][9] = 0;array[7][8] = 0;array[7][9] = 0;array[9][8] = 0;array[9][9] = 0;
        iScreen = Matrix(array);oScreen = Matrix(iScreen)
        draw_led(oScreen)
        time.sleep(0.2)
        array[4][4] = 31;array[4][5] = 31;array[5][3] = 31;array[5][6] = 31;array[6][3] = 31;array[6][6] = 31;array[7][4] = 31;array[7][5] = 31;array[14][2] = 31;array[14][6] = 31
        array[8][3] = 31;array[8][4] = 31;array[8][5] = 31;array[8][6] = 31;array[8][7] = 31;array[8][8] = 31;array[9][2] = 31;array[9][4] = 31;array[9][5] = 31
        array[10][2] = 31;array[10][4] = 31;array[10][5] = 31;array[11][4] = 31;array[11][5] = 31;array[12][4] = 31;array[12][6] = 31;array[13][3] = 31;array[13][6] = 31
        iScreen = Matrix(array);oScreen = Matrix(iScreen)
        draw_led(oScreen)
        time.sleep(0.2) # 31
iScreenDy = 14;iScreenDx = 30;iScreenDw = 1;top = 6;left = 22
#########SCORE###########
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
Boss_gun = [[11,11],[11,11]]
Boss = [
    [0,0,0,0,1,1,1,0,0,0,0],
    [0,0,0,0,1,0,1,0,0,0,0],
    [0,0,0,0,1,0,1,0,0,0,0],
    [0,0,0,0,1,0,1,0,0,0,0],
    [0,0,0,0,1,0,1,0,0,0,0],
    [1,1,1,1,1,0,1,1,1,1,1],
    [1,0,1,0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,1,1,1,0,0,0,1],
    [1,0,0,0,1,1,1,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1],
]
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
life = 5;G_time = 0.6;score = 0;temp_key = 0
LED_init()
while (life > 0):
    G_top = 11;G_left = 25;Boss_top = 2;Boss_left = 21;key = 0
    prograss(ArrayScreen,score);show_life(ArrayScreen,life);show_hand(ArrayScreen,temp_key)
    iScreen = Matrix(ArrayScreen);oScreen = Matrix(iScreen)
    set_mon_num = random.randint(1, 3)
    curr_mon = Matrix(set_array_mon(set_mon_num))
    tempBlk = iScreen.clip(top, left, top + curr_mon.get_dy(), left + curr_mon.get_dx());tempBlk = tempBlk + curr_mon
    iScreen.paste(tempBlk, top, left)
    if (score != 10): #10마리 죽이면 보스전으로 이동함 (시작 스코어는 0)
        while (G_left >= 5):
            GunBlk = Matrix(Gun)
            oScreen = Matrix(iScreen)
            G_tempBlk = iScreen.clip(G_top, G_left, G_top + GunBlk.get_dy(), G_left + GunBlk.get_dx())
            G_tempBlk = G_tempBlk + GunBlk
            oScreen.paste(G_tempBlk, G_top, G_left)
            draw_led(oScreen)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
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
                life = 0
                break
            elif key == 'scissor':  # 가위
                if (set_mon_num == 3):
                    G_time = 0.8*G_time
                    score += 1
                    break
            elif key == 'rock':  # 바위
                if (set_mon_num == 1):
                    G_time = 0.8*G_time
                    score += 1
                    break
            elif key == 'paper':  # 보
                if (set_mon_num == 2):
                    G_time = 0.8*G_time
                    score += 1
                    break
            if (G_left == 5): #총알이 닿으면 피 1 깎임
                life -= 1
                hit_react(ArrayScreen)
                set_mon_num = random.randint(1, 3)
                curr_mon = Matrix(set_array_mon(set_mon_num))
                tempBlk = iScreen.clip(top, left, top + curr_mon.get_dy(), left + curr_mon.get_dx());tempBlk = tempBlk + curr_mon
                iScreen.paste(tempBlk, top, left)
                break
            G_left -= 1 #총알 움직임
            time.sleep(G_time)
#############################################BOSS###################################################
    else :
        G_time = 1 #다시 게임시간 간격 원래대로 조정
        while(True):
            BossBlk = Matrix(Boss)
            Boss_tempBlk = iScreen.clip(Boss_top, Boss_left, Boss_top + BossBlk.get_dy(), Boss_left + BossBlk.get_dx())
            Boss_tempBlk = Boss_tempBlk + BossBlk
            oScreen.paste(Boss_tempBlk, Boss_top, Boss_left)
            Boss_pick = random.randint(1, 3)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == ord('q'):
                        key = 'quit'
                    if event.key == ord('a'):
                        key = 'scissor'
                    if event.key == ord('s'):
                        key = 'rock'
                    if event.key == ord('d'):
                        key = 'paper'
            if key == 'quit':
                life = 0
                break
            elif key == 'scissor':  # 가위
                if (Boss_pick == 3): #보
                    time.sleep(1)
                    score += 1
                    break
                else:
                    if(Boss_pick == 1):
                        life -= 1
                    if (Boss_pick == 2):
                        life -= 1
            elif key == 'rock':  # 바위d
                if (Boss_pick == 1):
                    time.sleep(1)
                    score += 1
                    break
                else:
                    if(Boss_pick == 2):
                        life -= 1
                    if (Boss_pick == 3):
                        life -= 1
            elif key == 'paper':  # 보
                if (Boss_pick == 2): #주먹
                    time.sleep(1)
                    score += 1
                    break
                else:
                    if(Boss_pick == 1):
                        life -= 1
                    if (Boss_pick == 3):
                        life -= 1
            if (life <= 0):
                break
            time.sleep(10)
    if (life <= 0):
        score_10 = score // 10
        score_1 = score % 10
        score_10_left = 8
        score_10_top = 4
        score_1_left = 15
        score_1_top = 4
        SiScreen = Matrix(ScoreScreen)
        SoScreen = Matrix(SiScreen)
        currBlk_1 = Matrix(set_score(score_1))
        tempBlk_1 = SiScreen.clip(score_1_top, score_1_left, score_1_top + currBlk_1.get_dy(), score_1_left + currBlk_1.get_dx())
        tempBlk_1 = tempBlk_1 + currBlk_1
        SoScreen.paste(tempBlk_1, score_1_top, score_1_left)
        currBlk_10 = Matrix(set_score(score_10))
        tempBlk_10 = SiScreen.clip(score_10_top, score_10_left, score_10_top + currBlk_10.get_dy(),score_10_left + currBlk_10.get_dx())
        tempBlk_10 = tempBlk_10 + currBlk_10
        SoScreen.paste(tempBlk_10, score_10   _top, score_10_left)
        draw_led(SoScreen)
        break
