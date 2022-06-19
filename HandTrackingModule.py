import cv2
import mediapipe as mp
import time
import numpy as np

'''
将21个坐标值直接放入列表 方便后续调用
'''

class handDetector():
    def __init__(self, mode=False, maxHands = 4, model_complexity=1, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.model_complexity = model_complexity

        self.mpHands = mp.solutions.hands
        # self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.detectionCon, self.trackCon)
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.model_complexity, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds = [4, 8, 12, 16, 20]
        self.jointIds = [[0, 5, 6], [0, 9, 10], [0, 13, 14], [0, 17, 18]]

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        #results.multi_handedness: 包括label和score，label是字符串"Left"或"Right"，score是置信度
        # 是否检测到手
        if self.results.multi_hand_landmarks:
            #self.num = 0
            for handLms in self.results.multi_hand_landmarks:
                #print(handLms)
                if draw:
                    # 标出手上的红点和连线
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
                #self.num = self.num + 1
        return img


    def findPosition(self, img, draw=True):
        #创建列表
        self.lmList = []
        if self.results.multi_hand_landmarks:
            #获得第一只手第一个坐标
            for handLms in self.results.multi_hand_landmarks:
                #myHand = self.results.multi_hand_landmarks
                #print(self.results.multi_hand_landmarks)
                # id和地标
                onehand = []
                for id, lm in enumerate(handLms.landmark):
                    # print(id, lm)
                    #h, w, c = img.shape
                    #print(h, w, c)
                    cx, cy, cz = int(lm.x * 1200), int(lm.y * 600), round(lm.z * 600, 3)
                    #print(id, cx, cy)
                    onehand.append([id, cx, cy, cz])
                    # 放大21个地标中的某一个
                    if draw:
                        cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
                self.lmList.append(onehand)
        return self.lmList


    def findPosition1(self, img, draw=True):
        # 创建列表
        self.lmList = []
        if self.results.multi_hand_landmarks:
            # 获得第一只手第一个坐标
            for handLms in self.results.multi_hand_landmarks:
                # myHand = self.results.multi_hand_landmarks
                # print(self.results.multi_hand_landmarks)
                # id和地标
                for id, lm in enumerate(handLms.landmark):
                    # print(id, lm)
                    # h, w, c = img.shape
                    # print(h, w, c)
                    cx, cy, cz = round(lm.x, 4), round(lm.y, 4), round(lm.z, 4)
                    # print(id, cx, cy)
                    self.lmList.append(cx)
                    self.lmList.append(cy)
                    self.lmList.append(cz)
                    # 放大21个地标中的某一个
                    if draw:
                        cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
        return self.lmList


    def pressornot(self):
        self.presslist = []
        jointIds = [[0, 5, 6], [0, 9, 10], [0, 13, 14], [0, 17, 18]]
        anglelist = [155, 160, 160, 155]
        if self.lmList != []:
            for num in range(0,len(self.lmList)):
                onehand = []
                if abs(self.lmList[num][3][1] - self.lmList[num][5][1]) < 30:
                    onehand.append(1)
                else:
                    onehand.append(0)
                for i in range(0,4):
                    radians_fingers = np.arctan2(self.lmList[num][jointIds[i][0]][3] - self.lmList[num][jointIds[i][1]][3], self.lmList[num][jointIds[i][0]][2] - self.lmList[num][jointIds[i][1]][2]) \
                                      - np.arctan2(self.lmList[num][jointIds[i][2]][3] - self.lmList[num][jointIds[i][1]][3], self.lmList[num][jointIds[i][2]][2] - self.lmList[num][jointIds[i][1]][2])
                    angle = np.abs(radians_fingers * 180.0 / np.pi)
                    if angle <= anglelist[i]:
                        onehand.append(1)
                    else:
                        onehand.append(0)
                self.presslist.append(onehand)
        else:
            self.presslist = []
        '''
        for id in range(0, 5):
            if abs(self.lmList[0][self.tipIds[id]][3]) > 1.4:
                self.presslist.append(1)
            else:
                self.presslist.append(0)
        return self.presslist
        '''
        return self.presslist


def main():
    # 初始 当前时间均为0
    pTime = 0
    cTime = 0
    # 获取摄像头
    cap = cv2.VideoCapture(0)
    #创建一个手部检测器
    detector = handDetector()
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        #print(num)
        #得到坐标值列表
        lmList =detector.findPosition(img, draw=False)
        #print(lmList)
        presslist = detector.pressornot()
        print(presslist)
        #print(lmList[0][4])

        cTime = time.time()
        # 帧速率
        fps = 1 / (cTime - pTime)
        pTime = cTime

        if success == True:
            img = cv2.flip(img, 180)
        # 显示帧速率 10 70位置 设置字体颜色等
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(33)

if __name__ == "__main__":
    main()


