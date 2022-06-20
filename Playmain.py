import pygame
import sys
import cv2 as cv
import numpy as np
import torch
from handmodel1 import Hands
import HandTrackingModule as htm
import pygame.midi as pm
from draw_piano import PAINO
from draw_guita import GUITA
from piano_guita import PIANO_GUITA
from cnn_vgg16_model import CNN_MODEL
from figure_input import drawhand
import ModeChoice as mc

class play_music():
    def __init__(self, cap):

        self.cap = cap
        self.history = np.zeros([5, 5], int)
        self.history1 = np.zeros([5, 5], int)

        self.out_history = 0
        self.out_before = 0
        self.img_size = 128
        self.model = CNN_MODEL()
        self.model.eval()
        # 加载参数
        model_param = torch.load('model_param_128_test.pkl', map_location=torch.device('cpu'))
        self.model.load_state_dict(model_param)
    def play(self, mode):
        # pygame.init()
        pm.init()
        pygame.init()

        player = pm.Output(0)
        # cap = cv.VideoCapture(0)
        screen = pygame.display.set_mode((1200, 600))
        detector = htm.handDetector(detectionCon=0.75)
        play_mode = 1
        before = 0
        if mode == 0:
            Instruments = PAINO()
            player.set_instrument(1)
            self.next_mode = 12

        elif mode == 1:
            Instruments = GUITA()
            player.set_instrument(24)
            self.next_mode = 13

        elif mode == 2:
            Instruments = PIANO_GUITA()
            self.next_mode = 14


        running = True
        while running:
            if mode == 0:
                img = pygame.image.load("./images/img_3.png")
                bakc_img = pygame.transform.scale(img, (1200, 600))
                screen.blit(bakc_img, (0, 0))
                points = Instruments.get_point()
                pygame.draw.polygon(screen, (255, 255, 255),
                                    (points[2][0], points[3][0], points[5][0],
                                     points[5][14], points[3][14], points[2][14]), 0)
                pygame.draw.polygon(screen, (255, 255, 255),
                                    (points[0][0], points[1][0], points[4][0],
                                     points[4][14], points[1][14], points[0][14]), 0)
            elif mode == 1:
                img = pygame.image.load("./images/img_4.jpg")
                bakc_img = pygame.transform.scale(img, (1200, 600))
                screen.blit(bakc_img, (0, 0))

                y_list = Instruments.y_list
                # print(y_list)
                for n in range(len(y_list)):
                    pygame.draw.line(screen, (0, 0, 0), (0, y_list[n]), (1200, y_list[n]), width=3)


            elif mode == 2:
                img = pygame.image.load("./images/img_17.png")
                bakc_img = pygame.transform.scale(img, (1200, 600))
                screen.blit(bakc_img, (0, 0))
                points = Instruments.get_point()
                pygame.draw.polygon(screen, (255, 255, 255),
                                    (points[2][0], points[3][0], points[5][0],
                                     points[5][7], points[3][7], points[2][7]), 0)
                pygame.draw.polygon(screen, (255, 255, 255),
                                    (points[0][0], points[1][0], points[4][0],
                                     points[4][7], points[1][7], points[0][7]), 0)
                y_list_1 = Instruments.y_list
                # print(y_list_1)
                for n in range(6):
                    pygame.draw.line(screen, (0, 0, 0), (595, y_list_1[n]), (1200, y_list_1[n]), width=3)
            hands = Hands(screen)
            success, img = self.cap.read()
            if success == True:
                img = cv.flip(img, 180)


            img = detector.findHands(img)
            lmList = detector.findPosition(img, draw=False)
            mode1 = mc.Mode(screen, self.next_mode, lmList)
            current_mode, self.next_mode = mode1.home()
            if self.next_mode == 1:
                del player
                pm.quit()
                return self.next_mode

            for num in range(0, len(lmList)):
                if mode == 0:

                    for index, i in enumerate(list([lmList[num][4],lmList[num][8],lmList[num][12],lmList[num][16],lmList[num][20]])):
                        judge = Instruments.judge(screen, i[1], i[2])

                        if judge not in self.history:
                            player.note_on(judge, 127)

                        self.history[0][index] = self.history[1][index]
                        self.history[1][index] = self.history[2][index]
                        self.history[2][index] = self.history[3][index]
                        self.history[3][index] = self.history[4][index]
                        self.history[4][index] = judge
                if mode == 1:


                    # pygame.draw.rect(screen, (180, 180, 180),
                    #                  ((695 + play_mode * 135, 13), (830 + play_mode * 135, 68)), 0)
                    if lmList[num][0][1] <= 380 and lmList[num][0][1] >= 0:
                        figure_list = detector.findPosition1(screen,draw=False)
                        figure_list = figure_list[63*num:]
                        figure_list.insert(0, 1)
                        # print(figure_list)
                        figure_img = np.zeros([self.img_size, self.img_size], np.uint8)
                        drawhand(figure_list, figure_img)
                        # cv.imshow('img', figure_img)
                        # cv.waitKey()
                        # cv.destroyAllWindows()

                        figure_img = torch.tensor(figure_img)
                        figure_img = figure_img.to(torch.float32)
                        figure_img = figure_img.unsqueeze(0)
                        figure_img = figure_img.unsqueeze(1)

                        output = self.model(figure_img)
                        _, out = torch.max(output, 1)
                        self.out_history = int(out)
                        pygame.draw.rect(screen, (200, 200, 200), (self.out_history * 200 + 10, 80, 180, 80), 0)
                    else:
                        # print(lmList[num][8][1], lmList[num][8][2])
                        if 685 < lmList[num][8][1] < 1015 and 13 < lmList[num][8][2] < 81:
                            # print(1)
                            play_mode = 1
                        elif 1015 < lmList[num][8][1] < 1180 and 13 < lmList[num][8][2] < 81:
                            # print(2)
                            play_mode = 2

                        before = Instruments.judge(screen, self.out_history, lmList[num][8][2], player, play_mode, before, open = hands.figure8(lmList))
                if mode == 2:
                    #演奏钢琴
                    if lmList[num][0][1] >= 760 or lmList[num][0][1] <= 595:
                        for index, i in enumerate(list([lmList[num][4],lmList[num][8],lmList[num][12],lmList[num][16],lmList[num][20]])):
                            judge = Instruments.judge_piano(screen, i[1], i[2])

                            if judge not in self.history1:
                                player.set_instrument(1)
                                player.note_on(judge, 127)

                            self.history1[0][index] = self.history1[1][index]
                            self.history1[1][index] = self.history1[2][index]
                            self.history1[2][index] = self.history1[3][index]
                            self.history1[3][index] = self.history1[4][index]
                            self.history1[4][index] = judge
                    #演奏吉他
                    if 880 < lmList[num][8][1] < 1030 and 15 < lmList[num][8][2] < 70:
                        # print(1)
                        play_mode = 1
                    elif 1030 < lmList[num][8][1] < 1180 and 15 < lmList[num][8][2] < 70:
                        # print(2)
                        play_mode = 2
                    if lmList[num][0][1] <= 760 and lmList[num][0][1] >= 595:
                        figure_list = detector.findPosition1(screen,draw=False)
                        figure_list = figure_list[63*num:]
                        figure_list.insert(0, 1)
                        # print(figure_list)
                        figure_img = np.zeros([self.img_size, self.img_size], np.uint8)
                        drawhand(figure_list, figure_img)
                        # cv.imshow('img', figure_img)
                        # cv.waitKey()
                        # cv.destroyAllWindows()

                        figure_img = torch.tensor(figure_img)
                        figure_img = figure_img.to(torch.float32)
                        figure_img = figure_img.unsqueeze(0)
                        figure_img = figure_img.unsqueeze(1)

                        output = self.model(figure_img)
                        _, out = torch.max(output, 1)
                        self.out_before = int(out)
                        if self.out_before<3:
                            pygame.draw.rect(screen, (200, 200, 200), (self.out_before*180+670, 80, 140, 60), 0)
                        elif self.out_before >= 3:
                            pygame.draw.rect(screen, (200, 200, 200), (self.out_before * 180 + 130, 160, 140, 60), 0)

                    elif lmList[num][0][1] >= 760:
                        before = Instruments.judge_guita(screen, self.out_before, lmList[num][8][2], player, play_mode, before, open = hands.figure8(lmList))

            Instruments.draw(screen, play_mode)

            for num in range(0, len(lmList)):
                hands.drawhand(lmList[num])

            pygame.display.update()
            for event in pygame.event.get():
                # for num in range(0, len(lmList)):
                if event.type == pygame.QUIT:
                    running = False

        del player
        pm.quit()
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    #0:钢琴
    #1:吉他
    #2:双人合奏
    cap = cv.VideoCapture(0)
    GAME3 = play_music(cap)
    next_mode = GAME3.play(2)
    # GAME2 = play_music()
    # GAME2.play(0)