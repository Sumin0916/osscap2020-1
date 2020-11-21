from matrix import *
import time
import random
import pygame as pg

pg.init()
screen = pg.display.set_mode((1, 1))

def draw_matrix(m):
    array = m.get_array()
    for y in range(m.get_dy()):
        for x in range(m.get_dx()):
            if array[y][x] == 0:
                print("□ ", end='')
            elif array[y][x] == 1:
                print("■ ", end='')
            else:
                print("■ ", end='')
        print()

def set_arrayBlk(num):
    if num == 1:  # sissor
        mon_Blk = [[0, 0, 1, 0, 1, 0, 0, 0],
                   [0, 0, 1, 0, 1, 0, 0, 0],
                   [0, 0, 1, 0, 1, 0, 0, 0],
                   [0, 0, 1, 1, 1, 1, 0, 0],
                   [0, 0, 1, 0, 0, 0, 1, 0],
                   [0, 1, 0, 0, 1, 0, 0, 1],
                   [0, 0, 1, 0, 0, 0, 1, 0],
                   [0, 0, 0, 1, 1, 1, 0, 0]]

    elif num == 2:  # rock
        mon_Blk = [[0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 1, 1, 1, 1, 1, 0],
                   [0, 1, 1, 0, 0, 0, 1, 1],
                   [0, 1, 0, 0, 1, 0, 0, 1],
                   [0, 0, 1, 0, 0, 0, 1, 1],
                   [0, 0, 0, 1, 1, 1, 0, 0]]

    elif num == 3:  # paper
        mon_Blk = [[0, 0, 0, 1, 0, 1, 0, 0],
                   [0, 1, 0, 1, 0, 1, 0, 0],
                   [0, 1, 0, 1, 0, 1, 0, 1],
                   [0, 1, 0, 1, 1, 1, 0, 1],
                   [0, 0, 1, 0, 0, 0, 1, 0],
                   [1, 0, 1, 0, 1, 0, 1, 1],
                   [0, 1, 1, 0, 0, 0, 1, 0],
                   [0, 0, 0, 1, 1, 1, 0, 0]]

    return mon_Blk


iScreenDy = 14
iScreenDx = 30
iScreenDw = 1
top = 6
left = 22

#########SCORE#################

Gun = [[1, 1]]

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
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

######################Fucking Print########################


heart = 5
G_time = 1
score = 1

while (heart > 0):

    G_top = 11
    G_left = 23
    Boss_top = 2
    Boss_left = 21
    key = 0

    iScreen = Matrix(ArrayScreen)
    oScreen = Matrix(iScreen)
    num = random.randint(1, 3)
    currBlk = Matrix(set_arrayBlk(num))
    tempBlk = iScreen.clip(top, left, top + currBlk.get_dy(), left + currBlk.get_dx())
    tempBlk = tempBlk + currBlk
    iScreen.paste(tempBlk, top, left)

    if (score%10 != 0):
        while (G_left >= 5):

            GunBlk = Matrix(Gun)
            oScreen = Matrix(iScreen)
            G_tempBlk = iScreen.clip(G_top, G_left, G_top + GunBlk.get_dy(), G_left + GunBlk.get_dx())
            G_tempBlk = G_tempBlk + GunBlk
            oScreen.paste(G_tempBlk, G_top, G_left)

            draw_matrix(oScreen);
            print()

            print('키를 누르세요: [ q (quit) / 왼쪽키 (Scissor) / 아래키 (Rock) / 오른쪽키 (Paper) ] \n잘못입력하면 목숨이 깎입니다.')
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == ord('q'):
                        key = 'q'

                    if event.key == pg.K_LEFT:
                        key = 'a'

                    if event.key == pg.K_DOWN:
                        key = 's'

                    if event.key == pg.K_RIGHT:
                        key = 'd'

            if key == 'q':
                print('Game terminated...')
                heart = 0
                break

            elif key == 'a':  # 가위
                if (num == 3):
                    print("이김")
                    score += 1
                    break
                else:
                    heart -= 1
                    break

            elif key == 's':  # 바위d
                if (num == 1):
                    print("이김")
                    score += 1
                    break
                else:
                    heart -= 1
                    break

            elif key == 'd':  # 보
                if (num == 2):
                    print("이김")
                    score += 1
                    break
                else:
                    heart -= 1
                    break

            if (G_left == 5):
                heart = 0
                break
            else:
                G_left -= 1

            time.sleep(G_time)

    else :

        while(True):

            BossBlk = Matrix(Boss)
            Boss_tempBlk = iScreen.clip(Boss_top, Boss_left, Boss_top + BossBlk.get_dy(), Boss_left + BossBlk.get_dx())
            Boss_tempBlk = Boss_tempBlk + BossBlk
            oScreen.paste(Boss_tempBlk, Boss_top, Boss_left)
            draw_matrix(oScreen);
            print()


            Boss_pick = random.randint(1, 3)

            print('키를 누르세요: [ q (quit) / 왼쪽키 (Scissor) / 아래키 (Rock) / 오른쪽키 (Paper) ] \n잘못입력하면 목숨이 깎입니다.')
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == ord('q'):
                        key = 'q'

                    if event.key == pg.K_LEFT:
                        key = 'a'

                    if event.key == pg.K_DOWN:
                        key = 's'

                    if event.key == pg.K_RIGHT:
                        key = 'd'

            if key == 'q':
                print('Game terminated...')
                heart = 0
                break

            elif key == 'a':  # 가위
                if (Boss_pick == 3): #보
                    print("보스는 '보'를 냈습니다.")
                    print("이김")
                    time.sleep(1)
                    score += 1
                    break
                else:
                    if(Boss_pick == 1):
                        print("보스는 '가위'를 냈습니다.")
                        heart -= 1
                    if (Boss_pick == 2):
                        print("보스는 '바위'를 냈습니다.")
                        heart -= 1


            elif key == 's':  # 바위d
                if (Boss_pick == 1):
                    print("보스는 '가위'를 냈습니다.")
                    print("이김")
                    time.sleep(1)
                    score += 1
                    break
                else:
                    if(Boss_pick == 2):
                        print("보스는 '바위'를 냈습니다.")
                        heart -= 1
                    if (Boss_pick == 3):
                        print("보스는 '보'를 냈습니다.")
                        heart -= 1


            elif key == 'd':  # 보
                if (Boss_pick == 2): #주먹
                    print("보스는 '보'를 냈습니다.")
                    print("이김")
                    time.sleep(1)
                    score += 1
                    break
                else:
                    if(Boss_pick == 1):
                        print("보스는 '가위'를 냈습니다.")
                        heart -= 1
                    if (Boss_pick == 3):
                        print("보스는 '보'를 냈습니다.")
                        heart -= 1

            if(heart >0):
                print(heart)
            else:
                break

            time.sleep(10)

    if (G_time > 0.2):
        G_time -= 0.1

    print(heart)
    print(score)
    if (heart == 0):
        print("게임 종료")
        break
