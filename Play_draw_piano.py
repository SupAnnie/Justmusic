# import cv2
# import numpy as np
import pygame, sys
from pygame.constants import QUIT
# import pygame.midi as pm
import time

class PAINO():
    def __init__(self):
        # self.jude_line = 550
        self.key_h = 300
        self.key_w = 85
        self.key_black_h = 150
        self.key_black_w = 30
        self.NUM_key = 7
        self.num_key_w = 2
        self.angle = 0.65
        self.h = 80
        self.h1 = 25
        self.h2 = 16
        self.rate = 0.825
        self.xlist = []
        for i in range(self.num_key_w*7):
            self.xlist.append(i*self.key_w)
        self.points = self.get_point()
    def get_point(self):
        points = []
        points1 = []
        points2 = []
        points3 = []
        points4 = []
        points5 = []
        points6 = []
        points1_b = []
        points2_b = []
        points3_b = []
        points4_b = []
        points5_b = []
        points6_b = []
        points7_b = []
        points8_b = []
        points9_b = []
        points10_b = []
        points11_b = []
        points12_b = []
        points13_b = []
        points14_b = []
        points15_b = []
        points16_b = []
        for n in range(self.num_key_w * self.NUM_key+1):
            point1 = (self.angle*(n * self.key_w-600)+600, 600-2*self.angle*self.key_h-2*self.h-self.h2)
            point2 = (n * self.key_w, 600-self.angle*self.key_h-2*self.h-self.h2)
            point3 = (self.angle*(n * self.key_w-600)+600, 600-self.angle*self.key_h-self.h)
            point4 = (n * self.key_w, 600-self.h)
            point5 = (n * self.key_w, 600-self.angle*self.key_h-self.h-self.h2)
            point6 = (n * self.key_w, 600)
            points1.append(point1)
            points2.append(point2)
            points3.append(point3)
            points4.append(point4)
            points5.append(point5)
            points6.append(point6)
        for i in range(self.num_key_w):
            for n in list([1, 2, 4, 5, 6]):
                point1_b = (self.angle*((i*7+n-1/4)*self.key_w-600)+600, 600-self.angle*self.key_h-self.h-self.h2)
                point2_b = (self.angle*((i*7+n+1/4)*self.key_w-600)+600, 600-self.angle*self.key_h-self.h-self.h2)
                point3_b = (self.rate*((i*7+n+1/4)*self.key_w-600)+600, self.angle*self.key_black_h+600-self.angle*self.key_h-self.h)
                point4_b = (self.rate*((i*7+n-1/4)*self.key_w-600)+600, self.angle*self.key_black_h+600-self.angle*self.key_h-self.h)
                point5_b = (self.angle*((i*7+n-1/4)*self.key_w-600)+600,600-2*self.angle * self.key_h-2*self.h-2*self.h2)
                point6_b = (self.angle*((i*7+n+1/4)*self.key_w-600)+600,600-2*self.angle * self.key_h-2*self.h-2*self.h2)
                point7_b = (self.rate*((i*7+n+1/4)*self.key_w-600)+600, self.angle*self.key_black_h+600-2*self.angle*self.key_h-2*self.h-self.h2)
                point8_b = (self.rate*((i*7+n-1/4)*self.key_w-600)+600, self.angle*self.key_black_h+600-2*self.angle*self.key_h-2*self.h-self.h2)
                point9_b = (self.rate*((i*7+n-1/4)*self.key_w-600)+600, self.angle*self.key_black_h+600-self.angle*self.key_h-self.h-self.h1)
                point10_b = (self.rate*((i*7+n+1/4)*self.key_w-600)+600, self.angle*self.key_black_h+600-self.angle*self.key_h-self.h-self.h1)
                point11_b = (self.rate*((i*7+n-1/4)*self.key_w-600)+600, self.angle*self.key_black_h+600-2*self.angle*self.key_h-2*self.h-self.h1-self.h2)
                point12_b = (self.rate*((i*7+n+1/4)*self.key_w-600)+600, self.angle*self.key_black_h+600-2*self.angle*self.key_h-2*self.h-self.h1-self.h2)
                point13_b = (self.angle*((i*7+n-1/4)*self.key_w-600)+600, 600-self.angle*self.key_h-self.h)
                point14_b = (self.angle*((i*7+n+1/4)*self.key_w-600)+600, 600-self.angle*self.key_h-self.h)
                point15_b = (self.angle*((i*7+n-1/4)*self.key_w-600)+600, 600-2*self.angle*self.key_h-2*self.h-self.h2)
                point16_b = (self.angle*((i*7+n+1/4)*self.key_w-600)+600, 600-2*self.angle*self.key_h-2*self.h-self.h2)
                points1_b.append(point1_b)
                points2_b.append(point2_b)
                points3_b.append(point3_b)
                points4_b.append(point4_b)
                points5_b.append(point5_b)
                points6_b.append(point6_b)
                points7_b.append(point7_b)
                points8_b.append(point8_b)
                points9_b.append(point9_b)
                points10_b.append(point10_b)
                points11_b.append(point11_b)
                points12_b.append(point12_b)
                points13_b.append(point13_b)
                points14_b.append(point14_b)
                points15_b.append(point15_b)
                points16_b.append(point16_b)
        points.append(points1)
        points.append(points2)
        points.append(points3)
        points.append(points4)
        points.append(points5)
        points.append(points6)
        points.append(points1_b)
        points.append(points2_b)
        points.append(points3_b)
        points.append(points4_b)
        points.append(points5_b)
        points.append(points6_b)
        points.append(points7_b)
        points.append(points8_b)
        points.append(points9_b)
        points.append(points10_b)
        points.append(points11_b)
        points.append(points12_b)
        points.append(points13_b)
        points.append(points14_b)
        points.append(points15_b)
        points.append(points16_b)
        return points
    def draw(self, screen):
        for n in range(self.num_key_w * self.NUM_key+1):
            pygame.draw.line(screen, (0, 0, 0), self.points[0][n], self.points[1][n], width=1)
            pygame.draw.line(screen, (0, 0, 0), self.points[2][n], self.points[3][n], width=1)
            pygame.draw.line(screen, (0, 0, 0), self.points[1][n], self.points[4][n], width=1)
            pygame.draw.line(screen, (0, 0, 0), self.points[3][n], self.points[5][n], width=1)

        pygame.draw.line(screen, (0, 0, 0), (0, 600-self.angle*self.key_h-self.h), (1200, 600-self.angle*self.key_h-self.h), width=1)
        pygame.draw.line(screen, (0, 0, 0), (0, 600-2*self.angle*self.key_h-2*self.h-self.h2), (1200, 600-2*self.angle*self.key_h-2*self.h-self.h2), width=1)
        pygame.draw.line(screen, (0, 0, 0), (0, 600-self.angle*self.key_h-2*self.h-self.h2), (1200, 600-self.angle*self.key_h -2*self.h-self.h2), width=1)
        pygame.draw.line(screen, (0, 0, 0), (0, 600-self.angle*self.key_h-self.h-self.h2), (1200, 600-self.angle*self.key_h-self.h-self.h2), width=1)
        pygame.draw.line(screen, (0, 0, 0), (0, 600-self.h), (1200, 600-self.h), width=1)
        # pygame.draw.line(screen, (200, 200, 200), (0, self.jude_line), (1200, self.jude_line), width=2)
        # pygame.draw.line(screen, (200, 200, 200), (0, self.jude_line-self.angle*self.key_h-20), (1200, self.jude_line-self.angle*self.key_h-20), width=2)

        for n in range(self.num_key_w * 5):
            pygame.draw.polygon(screen, (30, 30, 30), (self.points[6][n], self.points[14][n], self.points[9][n], self.points[18][n]), 0)
            pygame.draw.polygon(screen, (30, 30, 30), (self.points[7][n], self.points[15][n], self.points[8][n], self.points[19][n]), 0)
            pygame.draw.polygon(screen, (30, 30, 30), (self.points[10][n], self.points[17][n], self.points[13][n], self.points[20][n]), 0)
            pygame.draw.polygon(screen, (30, 30, 30), (self.points[11][n], self.points[16][n], self.points[12][n], self.points[21][n]), 0)
        for n in range(self.num_key_w * 5):

            pygame.draw.polygon(screen, (45, 45, 45), (self.points[8][n], self.points[9][n], self.points[14][n], self.points[15][n]), 0)
            pygame.draw.polygon(screen, (45, 45, 45), (self.points[12][n], self.points[13][n], self.points[16][n], self.points[17][n]), 0)

        for n in range(self.num_key_w * 5):
            pygame.draw.polygon(screen, (50, 50, 50), (self.points[6][n],self.points[7][n],self.points[15][n], self.points[14][n]), 0)
            pygame.draw.polygon(screen, (50, 50, 50), (self.points[10][n], self.points[11][n], self.points[17][n], self.points[16][n]), 0)
    def judge(self, screen, x, y):
        keys1 = {0: 36, 1: 38, 2: 40, 3: 41, 4: 43, 5: 45, 6: 47,
                 7: 48, 8: 50, 9: 52, 10: 53, 11: 55, 12: 57, 13: 59}
        keys2 = {0: 60, 1: 62, 2: 64, 3: 65, 4: 67, 5: 69, 6: 71,
                 7: 72, 8: 74, 9: 76, 10: 77, 11: 79, 12: 81, 13: 83}
        # keys_open = {36: True, 38: True, 40: True, 41: True, 43: True, 45: True, 47: True,
        #              48: True, 50: True, 52: True, 53: True, 55: True, 57: True, 59: True,
        #              60: True, 62: True, 64: True, 65: True, 67: True, 69: True, 71: True,
        #              72: True, 74: True, 76: True, 77: True, 79: True, 81: True, 83: True}
        nums = []
        if 600-self.angle*self.key_h-2*self.h-self.h2<y<600-self.angle*self.key_h-self.h-self.h2:
            for i in range(len(self.xlist)):
                if self.xlist[i]<x<self.xlist[i]+self.key_w:
                    pygame.draw.polygon(screen, (200, 200, 200), (self.points[0][i], self.points[0][i+1], self.points[1][i+1],
                                                                  self.points[4][i+1], self.points[4][i], self.points[1][i]),0)
                    # time.sleep(0.01)
                    a = int(keys1.get(i))
                    # keys_open[a] = False
                else:
                    a = 0
                nums.append(a)

        elif 600-self.h<y<600:
            for i in range(len(self.xlist)):
                if self.xlist[i]<x<self.xlist[i]+self.key_w:
                    pygame.draw.polygon(screen, (200, 200, 200), (self.points[2][i], self.points[2][i+1], self.points[3][i+1],
                                                                  self.points[5][i+1], self.points[5][i], self.points[3][i]),0)

                    # time.sleep(0.01)
                    a = int(keys2.get(i))
                    # keys_open[a] = False
                else:
                    a = 0
                nums.append(a)
        else:
            a = 0
            nums.append(a)
        if sum(nums) == 0:
            return 0

        else:
            for i in nums:
                if i > 0:
                    return i
        # return jud, op

if __name__ == "__main__":

    pygame.init()
    piano = PAINO()

    screen = pygame.display.set_mode((1200, 600))
    while True:
        screen.fill((255, 255, 255))
        piano.draw(screen)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

