import numpy as np
import cv2 as cv
from datetime import datetime, timedelta # 일정 시간동안 동작인식 함수를 작동시킴
import collections  #collections.counter을 이용해 인식한 동작 수를 셈 

def skinmask(img):
    hsvim = cv.cvtColor(img, cv.COLOR_BGR2HSV)  #(입력받는 B/G/R이미지를 hsv=색상/채도/명도 이미지로 변경)
    lower = np.array([0, 48, 80], dtype = "uint8") #HSV 로 봤을 때 피부색의 최저치
    upper = np.array([20, 255, 255], dtype = "uint8") #HSV 로 봤을 때 피부색의 최대치
    skinRegionHSV = cv.inRange(hsvim, lower, upper) #lower와 upper값 사이로 피부색 영역 검출
    blurred = cv.blur(skinRegionHSV, (2,2)) #피부색 영역을 블러처리함 
    ret, thresh = cv.threshold(blurred,0,255,cv.THRESH_BINARY) # 피부색 이미지 2진수화(임계화)
    return thresh

def getcnthull(mask_img): #컨투어 검출 
    contours, hierarchy = cv.findContours(mask_img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    contours = max(contours, key=lambda x: cv.contourArea(x))
    hull = cv.convexHull(contours) #컨투어의 끝점들 연결 
    return contours, hull

def getdefects(contours): #검출한 손가락 끝점들(hull)을 이용해 손가락 사이들 알아내기 
    hull = cv.convexHull(contours, returnPoints=False)
    defects = cv.convexityDefects(contours, hull)
    return defects


def rps():
    
    ip_list=[]#5초간 인식한 동작들을 저장함(rck, ppr, scr)
    cap = cv.VideoCapture(0) # '0' for webcam
    end_time = datetime.now() + timedelta(seconds=5) #5초간 입력을 받음 
    while cap.isOpened() and datetime.now() < end_time:
        _, img = cap.read()
        try:
            mask_img = skinmask(img)
            contours, hull = getcnthull(mask_img)
            cv.drawContours(img, [contours], -1, (255,255,0), 2)
            cv.drawContours(img, [hull], -1, (0, 255, 255), 2)
            defects = getdefects(contours)
            if defects is not None:
                cnt = 0
                for i in range(defects.shape[0]):  # 디펙트들 사이의 각도들 측정 
                    s, e, f, d = defects[i][0] #(시작점, 끝점, 시작점에서 가장 먼 점, 가장 먼 점까지의 거리)
                    start = tuple(contours[s][0])
                    end = tuple(contours[e][0])
                    far = tuple(contours[f][0])
                    a = np.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
                    b = np.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
                    c = np.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
                    angle = np.arccos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))  #     코사인값 구하기 
                    if angle <= np.pi / 2:  #각도가 90도 이하면 손가락으로 취급 
                        cnt += 1
                        cv.circle(img, far, 4, [0, 0, 255], -1)
                if cnt > 0:
                    cnt = cnt+1
                #cv.putText(img, str(cnt), (0, 50), cv.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0) , 2, cv.LINE_AA)
            
            if cnt >=2 and cnt <5:
                #print("Scissors")
                cv.putText(img, str("scr"), (0, 50), cv.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0) , 2, cv.LINE_AA)
                ip_list.append('scr')
                #return str("scissor")
            elif cnt>=5:
                cv.putText(img, str("paper"), (0, 50), cv.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0) , 2, cv.LINE_AA)
                ip_list.append('ppr')
                #return str("paper")
            else:
                cv.putText(img, str("Rck"), (0, 50), cv.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0) , 2, cv.LINE_AA)
                ip_list.appned('rck')
                #return str("wha?")
            
            cv.imshow("img", img)
        except:
            pass
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
            
    print(collections.Counter(ip_list))
    cap.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    rps()
    
