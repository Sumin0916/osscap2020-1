from matrix import *
import time
import random


def draw_matrix(m):
    array = m.get_array()
    for y in range(m.get_dy()):
        for x in range(m.get_dx()):
            if array[y][x] == 0:
                print("□", end='')
            elif array[y][x] == 1:
                print("■", end='')
            else:
                print("XX", end='')
        print()


def set_arrayBlk(num):
    if num == 1: #sissor
        mon_Blk = [ [0,0,1,0,1,0,0,0],
                    [0,0,1,0,1,0,0,0],
                    [0,0,1,0,1,0,0,0],
                    [0,0,1,1,1,1,0,0],
                    [0,0,1,0,0,0,1,0],
                    [0,1,0,0,1,0,0,1],
                    [0,0,1,0,0,0,1,0],
                    [0,0,0,1,1,1,0,0] ]
       
    elif num == 2: #rock
        mon_Blk =  [[0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,1,1,1,1,1,0],
                    [0,1,1,0,0,0,1,1],
                    [0,1,0,0,1,0,0,1],
                    [0,0,1,0,0,0,1,1],
                    [0,0,0,1,1,1,0,0]]

    elif num == 3: #paper
        mon_Blk = [ [0,0,0,1,0,1,0,0],
                    [0,1,0,1,0,1,0,0],
                    [0,1,0,1,0,1,0,1],
                    [0,1,0,1,1,1,0,1],
                    [0,0,1,0,0,0,1,0],
                    [1,0,1,0,1,0,1,1],
                    [0,1,1,0,0,0,1,0],
                    [0,0,0,1,1,1,0,0] ]

    return mon_Blk


iScreenDy = 14
iScreenDx = 30
iScreenDw = 1
top = 6
left = 22

G_top = 11
G_left = 23

Gun = [[1,1]]


ArrayScreen=[
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
            ]





def play(heart) :

    life = heart
    
    key = input('키를 누르세요: [ q (quit) / a (Scissor) / s (Rock) / d (Paper) ] \n잘못입력하면 목숨이 깎입니다.: ')
    if key == 'q':
        print('Game terminated...')
        life = 0
        return life

    elif key == 'a':  # 가위
        if ( num == 3) :
            print("이김")
            return life
        else :
            life -= 1
            return life
            

    elif key == 's':  # 바위
        if ( num == 1) :
            print("이김")
            return life
        else :
            life -= 1
            return life
            
    elif key == 'd':  # 보
        if ( num == 2) :
            print("이김")
            return life
        else :
            life -= 1
            return life
            
    else:
        print('Wrong key!!!')
        life -= 1
        return life

######################Fucking Print########################


heart = 5
G_time = 5

while True:
    
    
    
    iScreen = Matrix(ArrayScreen)
    oScreen = Matrix(iScreen)
    num = random.randint(1, 3)
    currBlk = Matrix(set_arrayBlk(num))
    tempBlk = iScreen.clip(top, left, top + currBlk.get_dy(), left + currBlk.get_dx())
    tempBlk = tempBlk + currBlk
    oScreen.paste(tempBlk, top, left)



        
    GunBlk = Matrix(Gun)
    G_tempBlk = iScreen.clip(G_top, G_left, G_top + GunBlk.get_dy(), G_left + GunBlk.get_dx())
    G_tempBlk = G_tempBlk + GunBlk
    oScreen.paste(G_tempBlk, G_top, G_left)
    
   

    draw_matrix(oScreen);
    print()
    
    

    heart = play(heart)
    print(heart)

    if( heart == 0):
        print("게임 종료")
        break


    
    

    

    
    
