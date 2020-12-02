import numpy as np
import math
import time
import cv2 as cv
from datetime import datetime, timedelta # 일정 시간동안 동작인식 함수를 작동시킴
#import collections  //collections.counter을 이용해 인식한 동작 수를 셈, 안 쓸 것 같음 
from pynput.keyboard import Key, Controller
keyboard = Controller()

def skinmask(roi):
    kernel = np.ones((3,3),np.uint8)  
    hsv = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
    lower = np.array([0,48,80], dtype=np.uint8)
    upper = np.array([20,255,255], dtype=np.uint8)

    mask = cv.inRange(hsv, lower, upper)
    mask = cv.dilate(mask,kernel,iterations = 4)
    mask = cv.GaussianBlur(mask,(5,5),100) 
    return mask 
       
def getcnt(mask_frame):
    contours,hierarchy= cv.findContours(mask_frame,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    cnt = max(contours, key = lambda x: cv.contourArea(x))
    return cnt

def getHullnDefects(cnt,approx):
    hull = cv.convexHull(cnt)

    areahull = cv.contourArea(hull)
    areacnt = cv.contourArea(cnt)
    arearatio=((areahull-areacnt)/areacnt)*100

    hull = cv.convexHull(approx, returnPoints=False)
    defects = cv.convexityDefects(approx, hull)

    return hull, defects, arearatio, areacnt 


def rps():
    cap = cv.VideoCapture(0) # '0' for webcam
    cap.set(cv.CAP_PROP_FRAME_WIDTH,800)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT,600)
    cap.set(cv.CAP_PROP_FPS,5)
    while (1): 
        try:
            ret, frame = cap.read()
            frame=cv.flip(frame,1)
            roi=frame[100:500, 100:500]  
            cv.rectangle(frame,(100,100),(500,500),(0,255,0),0)  

            mask_frame = skinmask(roi)

            cnt= getcnt(mask_frame)
            #형상을 approximate 하여 잡티를 없앰 
            epsilon = 0.0005*cv.arcLength(cnt,True)
            approx= cv.approxPolyDP(cnt,epsilon,True)

            hull, defects, arearatio, areacnt = getHullnDefects(cnt,approx)

            fngr=0
        
    
            for i in range(defects.shape[0]):
                s,e,f,d = defects[i,0]
                start = tuple(approx[s][0])
                end = tuple(approx[e][0])
                far = tuple(approx[f][0])
                pt= (100,180)
                
            
                a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
                b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
                c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
                s = (a+b+c)/2
                ar = math.sqrt(s*(s-a)*(s-b)*(s-c))
                d=(2*ar)/a
                
                angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57
                
                if angle <= 90 and d>30:
                    fngr += 1
                    cv.circle(roi, far, 3, [255,0,0], -1)
                
                cv.line(roi,start, end, [0,255,0], 2)
                
                
            fngr+=1

            font = cv.FONT_HERSHEY_SIMPLEX
            cv.putText(frame,'Put your hand in the box',(0,50), font, 2, (0,0,255), 3, cv.LINE_AA)
            if fngr==1:
                if areacnt<2000:
                    pass
                else:
                    if arearatio<12:
                        #cv.putText(frame,'Rock',(0,50), font, 2, (0,0,255), 3, cv.LINE_AA)
                        keyboard.press('s')
                        keyboard.release('s')
                        
            elif fngr==2:
               # cv.putText(frame,'Scissors',(0,50), font, 2, (0,0,255), 3, cv.LINE_AA)
                keyboard.press('a')
                keyboard.release('a')
                
            elif  fngr<=6 and fngr >=3:
               # cv.putText(frame,'Papers',(0,50), font, 2, (0,0,255), 3, cv.LINE_AA)
                keyboard.press('d')
                keyboard.release('d')
               
            
            else :
                cv.putText(frame,'reposition',(10,50), font, 2, (0,0,255), 3, cv.LINE_AA)
        
        #show the windows
            cv.imshow('mask',mask_frame)
            cv.imshow('frame',frame)
        
        except:
            pass
    
        k = cv.waitKey(5) & 0xFF
        if k == 27:
            break
    
    cv.destroyAllWindows()
    cap.release()  


if __name__ == "__main__":
    rps()
    
