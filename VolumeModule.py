import numpy as np
import pygame, sys
from pygame.constants import QUIT
import HandTrackingModule as htm
import HandDrawingModule as hdm
import cv2
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import ModeChoice as mc

class Volume():
    def __init__(self, screen, lmList, volume):
        self.lmList = lmList
        self.screen = screen
        self.volume = volume

    def vol_tansfer(self, x):
        dict = {0: -65.25, 1: -56.99, 2: -51.67, 3: -47.74, 4: -44.62, 5: -42.03, 6: -39.82, 7: -37.89, 8: -36.17,
                9: -34.63, 10: -33.24,
                11: -31.96, 12: -30.78, 13: -29.68, 14: -28.66, 15: -27.7, 16: -26.8, 17: -25.95, 18: -25.15,
                19: -24.38,
                20: -23.65,
                21: -22.96, 22: -22.3, 23: -21.66, 24: -21.05, 25: -20.46, 26: -19.9, 27: -19.35, 28: -18.82,
                29: -18.32,
                30: -17.82,
                31: -17.35, 32: -16.88, 33: -16.44, 34: -16.0, 35: -15.58, 36: -15.16, 37: -14.76, 38: -14.37,
                39: -13.99,
                40: -13.62,
                41: -13.26, 42: -12.9, 43: -12.56, 44: -12.22, 45: -11.89, 46: -11.56, 47: -11.24, 48: -10.93,
                49: -10.63,
                50: -10.33,
                51: -10.04, 52: -9.75, 53: -9.47, 54: -9.19, 55: -8.92, 56: -8.65, 57: -8.39, 58: -8.13, 59: -7.88,
                60: -7.63,
                61: -7.38, 62: -7.14, 63: -6.9, 64: -6.67, 65: -6.44, 66: -6.21, 67: -5.99, 68: -5.76, 69: -5.55,
                70: -5.33,
                71: -5.12, 72: -4.91, 73: -4.71, 74: -4.5, 75: -4.3, 76: -4.11, 77: -3.91, 78: -3.72, 79: -3.53,
                80: -3.34,
                81: -3.15, 82: -2.97, 83: -2.79, 84: -2.61, 85: -2.43, 86: -2.26, 87: -2.09, 88: -1.91, 89: -1.75,
                90: -1.58,
                91: -1.41, 92: -1.25, 93: -1.09, 94: -0.93, 95: -0.77, 96: -0.61, 97: -0.46, 98: -0.3, 99: -0.15,
                100: 0.0}
        return dict[x]

    def showvolume(self):
        # volume.GetMute()
        # volume.GetMasterVolumeLevel()
        volRAnge = self.volume.GetVolumeRange()
        minVol = volRAnge[0]
        maxVol = volRAnge[1]
        vol = self.volume.GetMasterVolumeLevel()
        for num in range(0, len(self.lmList)):
            if self.lmList[num][20][1] > 1120 and self.lmList[num][20][2] < 120:
                x1, y1 = self.lmList[num][4][1], self.lmList[num][4][2]
                x2, y2 = self.lmList[num][8][1], self.lmList[num][8][2]
                cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
                # pygame.draw.circle(screen, (0, 0, 0), (x1, y1), 12)
                # pygame.draw.circle(screen, (0, 0, 0), (x2, y2), 12)
                pygame.draw.line(self.screen, (125, 125, 125), (x1, y1), (x2, y2), 6)
                # min:20  max:150
                length = math.hypot(x2 - x1, y2 - y1)
                # print(length)
                # 音量：-65-0
                vol = np.interp(length, [20, 150], [minVol, maxVol])
                # print(percent)
                # 范围为-65-0:0-100
                self.volume.SetMasterVolumeLevel(vol, None)
                break
            else:
                continue
                # 范围为-65-0:0-100

        #print(vol)
        global percent
        for i in range(100):
            vol_dict = self.vol_tansfer(i)
            if (abs(vol - vol_dict) < 0.4):
                percent = i
                break
            else:
                continue

        top, height = 20 + 1.5 * (100 - percent), 1.5 * percent
        pygame.draw.rect(self.screen, (125, 125, 125), [1150, top, 20, height])
        pygame.draw.rect(self.screen, (125, 125, 125), [1150, 20, 20, 150], 2)

    def home(self):
        homekey = pygame.image.load("./images/homekey.png")
        self.screen.blit(homekey, (20, 20))
        # print(self.lmList[0][8][1])
        for num in range(0, len(self.lmList)):
            if self.lmList[num][8][1] < 70 and self.lmList[num][8][2] < 70:
                # print(self.lmList[num][8][1])
                # mode = mc.Mode(self.screen)
                # mode.ModePlay()
                next_mode = 1
                break
            else:
                continue
        return next_mode


def main():
    pygame.init()
    # 使用摄像头
    cap = cv2.VideoCapture(0)
    # 游戏界面设置
    screen = pygame.display.set_mode((1200, 600))

    # 创建手部检测的实体
    detector = htm.handDetector(detectionCon=0.75)
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # 游戏界面填充
        screen.fill((255, 255, 255))

        # 摄像头读出的图片
        success, img = cap.read()
        # 摄像头镜像翻转
        if success == True:
            img = cv2.flip(img, 180)

        img = detector.findHands(img)
        # 得到手部的坐标列表[[[id],[x],[y],[z]],[第二只手],...]
        lmList = detector.findPosition(img, draw=False)
        presslist = detector.pressornot()
        handmodel = hdm.Hand(screen, lmList, presslist)

        # 创建音量实体
        volumeobj = Volume(screen, lmList, volume)
        # 画出音量表示
        volumeobj.showvolume()
        volumeobj.home()
        handmodel.drawhand()
        pygame.display.update()

if __name__ == "__main__":
    main()