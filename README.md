# 오픈소스 기초설계 (가)반_9조

### 사용 오픈소스
1. 영상 인식을 위한 오픈 소스: https://github.com/opencv/opencv
2. 키입력을 위한 오픈 소스: https://github.com/moses-palmer/pynput
3. LED 출력 오픈 소스: https://github.com/hzeller/rpi-rgb-led-matrix
4. 동작인식 관련하여 넘파이 사용: https://github.com/numpy/numpy



### 준비과정
#### Raspberry pi Camera Module을 연결 :http://www.3demp.com/community/boardDetails.php?cbID=233

#### pynput과 numpy 설치
```
sudo pip3 install pynput
sudo pip3 install numpy
```
#### OpenCV 설치
```
아래의 pip 커맨드로 설치 가능
sudo pip3 install opencv-contrib-python
오류가 발생한다면 아래 링크를 따라 설치 
```
https://webnautes.tistory.com/916




### 시작방법
```
git clone https://github.com/caretop/osscap2020
```
```
cd osscap2020/game_final
```
```
python3 LED_game.py
```
- 영상인식 모드로 게임 실행시, 카메라 모듈에 손이 비치도록 조정해야 인식이 시작됨
- 또한 초록색 사각형 범위 안에 손이 들어가야 인식됨 



### 시연영상


