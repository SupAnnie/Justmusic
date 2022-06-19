import os
import sys
import cv2
import pygame
from pygame import QUIT
import HandTrackingModule as htm
import HandDrawingModule as hdm
import Playmain

class Mode():
    def __init__(self, screen, next_mode, lmList):
        self.screen = screen
        self.next_mode = next_mode
        self.lmList = lmList

    def ModeGame(self):
        background = pygame.image.load("./images/bgg.png")
        self.screen.blit(background, (200, 100))
        imgmode1 = pygame.image.load("./images/game_698x347.png")
        imgmode1 = pygame.transform.scale(imgmode1, (600, 300))
        self.screen.blit(imgmode1, (305, 160))
        font1 = pygame.font.Font("Muyao.ttf", 70)
        text1 = font1.render('Game Mode', True, (125, 125, 125))
        self.screen.blit(text1, (460, 460))
        pygame.draw.circle(self.screen, (125, 125, 125), (150, 100), 15)
        pygame.draw.circle(self.screen, (125, 125, 125), (600, 100), 15, 2)
        pygame.draw.circle(self.screen, (125, 125, 125), (1050, 100), 15, 2)
        pygame.draw.line(self.screen, (125, 125, 125), (165, 100), (585, 100), 8)
        pygame.draw.line(self.screen, (125, 125, 125), (615, 100), (1035, 100), 8)

    def ModePlay(self):
        background = pygame.image.load("./images/bgg.png")
        self.screen.blit(background, (200, 100))
        pygame.draw.circle(self.screen, (125, 125, 125), (150, 100), 15, 2)
        pygame.draw.circle(self.screen, (125, 125, 125), (600, 100), 15)
        pygame.draw.circle(self.screen, (125, 125, 125), (1050, 100), 15, 2)
        pygame.draw.line(self.screen, (125, 125, 125), (165, 100), (585, 100), 8)
        pygame.draw.line(self.screen, (125, 125, 125), (615, 100), (1035, 100), 8)
        imgmode21 = pygame.image.load("./images/imgmode2.png")
        imgmode21 = pygame.transform.scale(imgmode21, (480, 240))
        self.screen.blit(imgmode21, (305, 160))
        imgmode22 = pygame.image.load("./images/imgmode22.png")
        imgmode22 = pygame.transform.scale(imgmode22, (480, 240))
        self.screen.blit(imgmode22, (425, 220))
        font1 = pygame.font.Font("Muyao.ttf", 70)
        text1 = font1.render('Single-player Mode', True, (125, 125, 125))
        self.screen.blit(text1, (350, 460))


    def ModeDouble(self):
        background = pygame.image.load("./images/bgg.png")
        self.screen.blit(background, (200, 100))
        pygame.draw.circle(self.screen, (125, 125, 125), (150, 100), 15, 2)
        pygame.draw.circle(self.screen, (125, 125, 125), (600, 100), 15, 2)
        pygame.draw.circle(self.screen, (125, 125, 125), (1050, 100), 15)
        pygame.draw.line(self.screen, (125, 125, 125), (165, 100), (585, 100), 8)
        pygame.draw.line(self.screen, (125, 125, 125), (615, 100), (1035, 100), 8)
        imgmode3 = pygame.image.load("./images/imgmode3.png")
        imgmode1 = pygame.transform.scale(imgmode3, (600, 300))
        self.screen.blit(imgmode1, (305, 160))
        font1 = pygame.font.Font("Muyao.ttf", 70)
        text1 = font1.render('Two-player Mode', True, (125, 125, 125))
        self.screen.blit(text1, (380, 460))

    def GameOne(self):
        # background = pygame.image.load("./images/bg2.png")
        # self.screen.blit(background, (50, 85))
        # game1 = pygame.image.load("./images/game1_553x311.jpg")
        # self.screen.blit(game1, (320, 158))
        game1 = pygame.image.load("./images/game1_1100x500 (1).png")
        game1 = pygame.transform.scale(game1, (1100, 500))
        self.screen.blit(game1, (50, 60))
        # collosion_Sound = pygame.mixer.Sound(r'E:\project\bgmusic\Luna Safari - 【钢琴】Lemon（电视剧《非自然死亡》主题曲）.mp3')
        # collosion_Sound.play()
        # pygame.mixer.music.stop()
        # pygame.mixer.music.load(r'E:\project\bgmusic\dylanf - 天空之城（经典钢琴版）.mp3')
        # pygame.mixer.music.play()


    def GameTwo(self):
        # background = pygame.image.load("./images/bg3.png")
        # self.screen.blit(background, (45, 80))
        game2 = pygame.image.load("./images/game2_1100x500.png")
        self.screen.blit(game2, (50, 60))
        # pygame.mixer.music.stop()
        # pygame.mixer.music.load(r"E:\project\bgmusic\Wolfgang Amadeus Mozart - 小星星变奏曲.mp3")
        # pygame.mixer.music.play()

    def GameThree(self):
        # background = pygame.image.load("./images/bg3.png")
        # self.screen.blit(background, (45, 80))
        game3 = pygame.image.load("./images/game3_1100x500 (2).png")
        game3 = pygame.transform.scale(game3, (1100, 500))
        self.screen.blit(game3, (50, 60))
        # file = r'E:\project\bgmusic\Luna Safari - 【钢琴】Lemon（电视剧《非自然死亡》主题曲）.mp3'
        # pygame.mixer.music.stop()
        # pygame.mixer.music.load(r'E:\project\bgmusic\Luna Safari - 【钢琴】Lemon（电视剧《非自然死亡》主题曲）.mp3')
        # pygame.mixer.music.play()

    def GameFour(self):
        game4 = pygame.image.load("./images/game4_1100x500.png")
        game4 = pygame.transform.scale(game4, (1100, 500))
        self.screen.blit(game4, (50, 60))

    def GameFive(self):
        game5 = pygame.image.load("./images/game5_1100x500.png")
        game5 = pygame.transform.scale(game5, (1100, 500))
        self.screen.blit(game5, (50, 60))

    def MusicPlay(self):
        songs = [r'E:\project\bgmusic\dylanf - 天空之城（经典钢琴版）.mp3',
                 r'E:\project\bgmusic\Luna Safari - 【钢琴】Lemon（电视剧《非自然死亡》主题曲）.mp3',
                 r'E:\project\bgmusic\Wolfgang Amadeus Mozart - 小星星变奏曲.mp3']
        pygame.mixer.music.stop()
        # 播放音乐
        if self.next_mode == 1 :
            pygame.mixer.music.load(songs[0])
        elif self.next_mode == 4 or self.next_mode == 5:
            pygame.mixer.music.load(songs[self.next_mode-3])
        # print("music")
        pygame.mixer.music.play(start=2.0)


    def PlayPiano(self):
        piano = pygame.image.load("./images/playpiano_1100x500.png")
        self.screen.blit(piano, (50, 60))

    def PlayGuitar(self):
        guitar = pygame.image.load("./images/playguitar_1100x500.png")
        self.screen.blit(guitar, (50, 60))

    def home(self):
        running = True
        # print(self.lmList[0][8][1])
        # print("work")
        for num in range(0, len(self.lmList)):
            if (self.lmList[num][8][1] < 70 and self.lmList[num][8][2] < 70):
                # print(self.lmList[num][8][1])
                # mode = mc.Mode(self.screen)
                # mode.ModePlay()
                self.next_mode = 1
                # current_mode = 1
                # pygame.init()
                # running = False
            #     break
            # else:
            #     continue
        # game_return = 0
        flag = False  #判断有无读入音乐
        if self.next_mode == 1:
            # pygame.init()
            self.ModeGame()
            current_mode = 1
            # running = False
        elif self.next_mode == 2:
            self.ModePlay()
            current_mode = 2
        elif self.next_mode == 3:
            self.ModeDouble()
            current_mode = 3
        elif self.next_mode == 4:
            self.GameOne()
            current_mode = 4
            # self.MusicPlay()
        elif self.next_mode == 5:
            self.GameTwo()
            current_mode = 5
            # self.MusicPlay()
        elif self.next_mode == 6:
            self.GameThree()
            current_mode = 6
            # self.MusicPlay()
        elif self.next_mode == 7:
            self.PlayPiano()
            current_mode = 7
        elif self.next_mode == 8:
            self.PlayGuitar()
            current_mode = 8
        elif self.next_mode == 9:
            # gamemanager = game.Manager(self.screen)
            # gamemanager.main()
            current_mode = 9
        elif self.next_mode == 10:
            current_mode = 10
        elif self.next_mode == 11:
            current_mode = 11
        elif self.next_mode == 12:
            current_mode = 12
        elif self.next_mode == 13:
            current_mode = 13
        elif self.next_mode == 14:
            current_mode = 14
        elif self.next_mode == 15:
            self.GameFour()
            current_mode = 15
        elif self.next_mode == 16:
            current_mode = 16
        elif self.next_mode == 17:
            self.GameFive()
            current_mode = 17
        elif self.next_mode == 18:
            current_mode = 18
        homekey = pygame.image.load("./images/homekey.png")
        self.screen.blit(homekey, (20, 20))
        return current_mode,self.next_mode


# class Bgmusic:
#     def __init__(self, mode):
#         self.mode = mode
#
#     def Play(self):
#         if self.mode == 4:
#             pygame.mixer.init()
#             pygame.mixer.music.load(r"E:\project\bgmusic\dylanf - 天空之城（经典钢琴版）.mp3")
#             pygame.mixer.music.play()


def main():
    pygame.init()
    # 使用摄像头
    cap = cv2.VideoCapture(0)
    # 游戏界面设置
    screen = pygame.display.set_mode((1200, 600))

    # 创建手部检测的实体
    detector = htm.handDetector(detectionCon=0.75)
    pygame.mixer.init()
    pygame.mixer.music.load(r"E:\project\bgmusic\dylanf - 天空之城（经典钢琴版）.mp3")
    pygame.mixer.music.play()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # 游戏界面填充
        screen.fill((255, 255, 255))
        # background = pygame.image.load("./images/bg2.png")
        # screen.blit(background, (200, 110))

        # 摄像头读出的图片
        success, img = cap.read()
        # 摄像头镜像翻转
        if success == True:
            img = cv2.flip(img, 180)

        img = detector.findHands(img)
        # 得到手部的坐标列表[[[id],[x],[y],[z]],[第二只手],...]
        lmList = detector.findPosition(img, draw=False)
        # print(lmList)
        # 得到手指是否按下的列表[[按下为1，没按为0（从左到右依次为拇指食指中指无名指小指）], [第二只手]]
        presslist = detector.pressornot()
        # print(presslist)
        mode = Mode(screen)
        mode.GameOne()

        # 创建画出手部的实体
        handmodel = hdm.Hand(screen, lmList, presslist)
        # 画出手部坐标和骨架
        handmodel.drawhand()


        pygame.display.update()

if __name__=='__main__':
    main()