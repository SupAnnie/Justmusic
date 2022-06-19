import cv2
import numpy as np
import pygame, sys
from pygame.constants import QUIT
from multiprocessing import Pool
import HandTrackingModule as htm
import math


class Hands():
    def __init__(self, screen):
        self.screen = screen
        self.line1_color = (0, 255, 255)
        self.line2_color = (40, 215, 215)
        self.circle_color = (64, 224, 205)
    def drawlines(self, x, y, List):
        for id in range(x, y):
            pygame.draw.line(self.screen, self.line1_color, (List[id][1], List[id][2]), (List[id + 1][1], List[id + 1][2]), 7)

    def drawline(self, x, y, List):
        pygame.draw.line(self.screen, self.line2_color, (List[x][1], List[x][2]), (List[y][1], List[y][2]), 8)

    def drawhand(self, List):

        self.drawlines(0, 4, List)
        self.drawlines(5, 8, List)
        self.drawlines(9, 12, List)
        self.drawlines(13, 16, List)
        self.drawlines(17, 20, List)

        for id in range(0, 21):
            pygame.draw.circle(self.screen, self.circle_color, (List[id][1], List[id][2]), 8)

        self.drawline(0, 5, List)
        self.drawline(5, 9, List)
        self.drawline(9, 13, List)
        self.drawline(13, 17, List)
        self.drawline(0, 17, List)

        for id in list([0, 5, 9, 13, 17]):
            pygame.draw.circle(self.screen, self.circle_color, (List[id][1], List[id][2]), 8)
    def fingercounter(self, List):

        # 指尖列表，分别代表大拇指、食指、中指、无名指和小指的指尖
        tip_ids = [4, 8, 12, 16, 20]
        if len(List) == 2:
            fingers = []
            for tid in tip_ids:
                # 找到每个指尖的位置
                # x, y = List[0][tid][1], List[0][tid][2]
                # # cv2.circle(img, (x, y), 10, (0, 255, 0), cv2.FILLED)
                # # 如果是大拇指，如果大拇指指尖x位置大于大拇指第二关节的位置，则认为大拇指打开，否则认为大拇指关闭
                if tid == 4:
                #     a_x, b_x, c_x = List[0][tid][1]/1200, List[0][tid-1][1]/1200, List[0][tid-2][1]/1200  # 点a、b、c的x坐标
                #     a_y, b_y, c_y = List[0][tid][2]/600, List[0][tid-1][2]/600, List[0][tid-2][2]/600  # 点a、b、c的y坐标
                #     a_z, b_z, c_z = List[0][tid][3]/1200, List[0][tid-1][3]/1200, List[0][tid-2][3]/1200  # 点a、b、c的z坐标
                #
                #     x1, y1, z1 = (a_x - b_x), (a_y - b_y), (a_z - b_z)
                #     x2, y2, z2 = (c_x - b_x), (c_y - b_y), (c_z - b_z)
                #
                #     # 两个向量的夹角，即角点b的夹角余弦值
                #     cos_b = (x1 * x2 + y1 * y2 + z1 * z2) / (math.sqrt(x1 ** 2 + y1 ** 2 + z1 ** 2) * (
                #         math.sqrt(x2 ** 2 + y2 ** 2 + z2 ** 2)))  # 角点b的夹角余弦值
                #     B = round(math.degrees(math.acos(cos_b)), 3)  # 角点b的夹角值
                #     print(B)
                    if List[1][tid][1] >= List[1][8][1] and List[1][tid][1] <= List[1][20][1] or \
                            List[1][tid][1] >= List[1][20][1] and List[1][tid][1] <= List[1][8][1]:
                        fingers.append(0)
                    else:
                        fingers.append(1)
                # 如果是其他手指，如果这些手指的指尖的y位置大于第二关节的位置，则认为这个手指打开，否则认为这个手指关闭
                else:
                    if List[1][tid][2] < List[1][tid - 2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)
            # fingers是这样一个列表，5个数据，0代表一个手指关闭，1代表一个手指打开
            # 判断有几个手指打开
            cnt = fingers.count(1)
        else:
            cnt = 0
        print(cnt)
        return cnt
    def figure8(self, List):
        if len(List) > 0:
            if List[0][8][1] > List[0][6][1]:
                mode = False
            else:
                mode = True
            return mode


if __name__ == "__main__":


    pygame.init()

    cap = cv2.VideoCapture(0)

    screen = pygame.display.set_mode((1200, 600))

    detector = htm.handDetector(detectionCon=0.75)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))
        hands = Hands(screen)
        success, img = cap.read()
        if success == True:
            img = cv2.flip(img, 180)


        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)

        for num in range(0, len(lmList)):
            hands.drawhand(lmList[num])
        hands.fingercounter(lmList)





        pygame.display.update()






