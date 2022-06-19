import pygame, sys
from pygame.constants import QUIT
from guita_music import music_guita

class PIANO_GUITA():
    def __init__(self):
        #吉他
        img1 = pygame.image.load("./images/img01.png")
        img2 = pygame.image.load("./images/img02.png")
        img3 = pygame.image.load("./images/img03.png")
        img4 = pygame.image.load("./images/img04.png")
        img5 = pygame.image.load("./images/img05.png")
        img6 = pygame.image.load("./images/img06.png")

        img1 = pygame.transform.scale(img1, (45, 60))
        img2 = pygame.transform.scale(img2, (45, 60))
        img3 = pygame.transform.scale(img3, (45, 60))
        img4 = pygame.transform.scale(img4, (45, 60))
        img5 = pygame.transform.scale(img5, (45, 60))
        img6 = pygame.transform.scale(img6, (45, 60))
        self.img = [img1, img2, img3, img4, img5, img6]

        font = pygame.font.Font('Muyao.ttf', 50)   # 15:font size
        text1 = font.render('C', True, (0, 0, 0))
        text2 = font.render('Dm', True, (0, 0, 0))
        text3 = font.render('Em', True, (0, 0, 0))
        text4 = font.render('F', True, (0, 0, 0))
        text5 = font.render('G', True, (0, 0, 0))
        text6 = font.render('Am', True, (0, 0, 0))
        self.text = [text1, text2, text3, text4, text5, text6]
        font1 = pygame.font.Font('Muyao.ttf', 50)
        self.mode1 = font1.render('弹唱', True, (125, 125, 125))
        self.mode2 = font1.render('指弹', True, (125, 125, 125))

        self.img_w = 90
        self.img_h = 120
        self.guita_h = 60
        self.y_list = []
        self.count = 5
        self.music = music_guita()
        self.high = 150
        for i in range(6):
            self.y_list.append(560 - i * self.guita_h)
        self.y_list1 = [600, 560, 500, 440, 380, 320, 260, -3]

        #钢琴
        self.key_h = 300
        self.key_w = 85
        self.key_black_h = 150
        self.key_black_w = 30
        self.NUM_key = 7
        self.angle = 0.60
        self.h = 80
        self.h1 = 25
        self.h2 = 16
        self.rate = 0.81
        self.xlist = []
        for i in range(7):
            self.xlist.append(i*self.key_w)
        self.points = self.get_point()
    def draw(self, screen, play_mode):
        #吉他

        pygame.draw.line(screen, (160, 160, 160), (760, self.y_list[5]), (760, self.y_list[0]), width = 6)

        for i in range(3):
            screen.blit(self.text[i], (i*180+670, 80))
            screen.blit(self.img[i], (i*180+740, 80))
        for i in range(3, 6):
            screen.blit(self.text[i], (i*180+130, 160))
            screen.blit(self.img[i], (i*180+200, 160))
        pygame.draw.rect(screen, (255, 255, 255), (880, 15, 300, 55), 0)
        # play_mode = 2
        pygame.draw.rect(screen, (230, 230, 230), ((730 + play_mode * 150, 15), (150, 55)), 0)
        screen.blit(self.mode1, (910, 20))
        screen.blit(self.mode2, (1060, 20))
        #钢琴
        for n in range(self.NUM_key+1):
            pygame.draw.line(screen, (0, 0, 0), self.points[0][n], self.points[1][n], width=1)
            pygame.draw.line(screen, (0, 0, 0), self.points[2][n], self.points[3][n], width=1)
            pygame.draw.line(screen, (0, 0, 0), self.points[1][n], self.points[4][n], width=1)
            pygame.draw.line(screen, (0, 0, 0), self.points[3][n], self.points[5][n], width=1)

        pygame.draw.line(screen, (0, 0, 0), (-self.angle*300+300, 600-self.angle*self.key_h-self.h), (self.angle*300+298, 600-self.angle*self.key_h-self.h), width=1)
        pygame.draw.line(screen, (0, 0, 0), (-self.angle*300+300, 600-2*self.angle*self.key_h-2*self.h-self.h2), (self.angle*300+298, 600-2*self.angle*self.key_h-2*self.h-self.h2), width=1)
        pygame.draw.line(screen, (0, 0, 0), (0, 600-self.angle*self.key_h-2*self.h-self.h2), (595, 600-self.angle*self.key_h -2*self.h-self.h2), width=1)
        pygame.draw.line(screen, (0, 0, 0), (0, 600-self.angle*self.key_h-self.h-self.h2), (595, 600-self.angle*self.key_h-self.h-self.h2), width=1)
        pygame.draw.line(screen, (0, 0, 0), (0, 600-self.h), (595, 600-self.h), width=1)
        # pygame.draw.line(screen, (200, 200, 200), (0, self.jude_line), (1200, self.jude_line), width=2)
        # pygame.draw.line(screen, (200, 200, 200), (0, self.jude_line-self.angle*self.key_h-20), (1200, self.jude_line-self.angle*self.key_h-20), width=2)

        for n in range(5):
            pygame.draw.polygon(screen, (30, 30, 30), (self.points[6][n], self.points[14][n], self.points[9][n], self.points[18][n]), 0)
            pygame.draw.polygon(screen, (30, 30, 30), (self.points[7][n], self.points[15][n], self.points[8][n], self.points[19][n]), 0)
            pygame.draw.polygon(screen, (30, 30, 30), (self.points[10][n], self.points[17][n], self.points[13][n], self.points[20][n]), 0)
            pygame.draw.polygon(screen, (30, 30, 30), (self.points[11][n], self.points[16][n], self.points[12][n], self.points[21][n]), 0)
        for n in range(5):

            pygame.draw.polygon(screen, (45, 45, 45), (self.points[8][n], self.points[9][n], self.points[14][n], self.points[15][n]), 0)
            pygame.draw.polygon(screen, (45, 45, 45), (self.points[12][n], self.points[13][n], self.points[16][n], self.points[17][n]), 0)

        for n in range(5):
            pygame.draw.polygon(screen, (50, 50, 50), (self.points[6][n],self.points[7][n],self.points[15][n], self.points[14][n]), 0)
            pygame.draw.polygon(screen, (50, 50, 50), (self.points[10][n], self.points[11][n], self.points[17][n], self.points[16][n]), 0)


        #乐器分割线
        pygame.draw.line(screen, (0, 0, 0), (595, 0), (595, 600), width=4)

    def judge_guita(self, screen, key, y, player, play_mode, before, open = False):
        #吉他
        # if key<3:
        #     pygame.draw.rect(screen, (200, 200, 200), (key*180+670, 80, 140, 60), 0)
        # elif key >= 3:
        #     pygame.draw.rect(screen, (200, 200, 200), (key * 180 + 130, 160, 140, 60), 0)

        if play_mode == 1:

            if open == False:
                pass

            elif y < self.y_list[0] and y > self.y_list[5] and open == True:
                # count = count + 1
                # if count == 3:
                if y > before + self.high:
                    self.music.music_play1(key, 1, player)
                elif y < before - self.high:
                    self.music.music_play1(key, 0, player)
                else:
                    pass
                count = 0
                before = y
            else:
                pass
            return before
        if play_mode == 2:
            if open == False or y == None or before == None:
                pass
            elif 0 <= y < 600 and 0 <= before < 600:
                for i in range(7):
                    if self.y_list1[i + 1] < y <= self.y_list1[i]:
                        end = i - 1
                        # print('end:', end)
                for i in range(7):
                    if self.y_list1[i + 1] < before <= self.y_list1[i]:
                        start = i - 1
                        # print('start:', start)
                if end > start:
                    for i in range(start, end):
                        pygame.draw.line(screen, (175, 175, 175), (595, self.y_list[i + 1]), (1200, self.y_list[i + 1]),
                                         width=3)
                if end < start:
                    for i in range(start, end, -1):
                        pygame.draw.line(screen, (175, 175, 175), (595, self.y_list[i]), (1200, self.y_list[i]), width=3)
                self.music.music_play2(key, start, end, player)
            before = y
            return before

    def judge_piano(self, screen, x, y):
        keys1 = {0: 48, 1: 50, 2: 52, 3: 53, 4: 55, 5: 57, 6: 59}
        keys2 = {0: 60, 1: 62, 2: 64, 3: 65, 4: 67, 5: 69, 6: 71}
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
        for n in range(self.NUM_key+1):
            point1 = (self.angle*(n * self.key_w-300)+300, 600-2*self.angle*self.key_h-2*self.h-self.h2)
            point2 = (n * self.key_w, 600-self.angle*self.key_h-2*self.h-self.h2)
            point3 = (self.angle*(n * self.key_w-300)+300, 600-self.angle*self.key_h-self.h)
            point4 = (n * self.key_w, 600-self.h)
            point5 = (n * self.key_w, 600-self.angle*self.key_h-self.h-self.h2)
            point6 = (n * self.key_w, 600)
            points1.append(point1)
            points2.append(point2)
            points3.append(point3)
            points4.append(point4)
            points5.append(point5)
            points6.append(point6)
        for n in list([1, 2, 4, 5, 6]):
            point1_b = (self.angle*((n-1/4)*self.key_w-300)+300, 600-self.angle*self.key_h-self.h-self.h2)
            point2_b = (self.angle*((n+1/4)*self.key_w-300)+300, 600-self.angle*self.key_h-self.h-self.h2)
            point3_b = (self.rate*((n+1/4)*self.key_w-300)+300, self.angle*self.key_black_h+600-self.angle*self.key_h-self.h)
            point4_b = (self.rate*((n-1/4)*self.key_w-300)+300, self.angle*self.key_black_h+600-self.angle*self.key_h-self.h)
            point5_b = (self.angle*((n-1/4)*self.key_w-300)+300,600-2*self.angle * self.key_h-2*self.h-2*self.h2)
            point6_b = (self.angle*((n+1/4)*self.key_w-300)+300,600-2*self.angle * self.key_h-2*self.h-2*self.h2)
            point7_b = (self.rate*((n+1/4)*self.key_w-300)+300, self.angle*self.key_black_h+600-2*self.angle*self.key_h-2*self.h-self.h2)
            point8_b = (self.rate*((n-1/4)*self.key_w-300)+300, self.angle*self.key_black_h+600-2*self.angle*self.key_h-2*self.h-self.h2)
            point9_b = (self.rate*((n-1/4)*self.key_w-300)+300, self.angle*self.key_black_h+600-self.angle*self.key_h-self.h-self.h1)
            point10_b = (self.rate*((n+1/4)*self.key_w-300)+300, self.angle*self.key_black_h+600-self.angle*self.key_h-self.h-self.h1)
            point11_b = (self.rate*((n-1/4)*self.key_w-300)+300, self.angle*self.key_black_h+600-2*self.angle*self.key_h-2*self.h-self.h1-self.h2)
            point12_b = (self.rate*((n+1/4)*self.key_w-300)+300, self.angle*self.key_black_h+600-2*self.angle*self.key_h-2*self.h-self.h1-self.h2)
            point13_b = (self.angle*((n-1/4)*self.key_w-300)+300, 600-self.angle*self.key_h-self.h)
            point14_b = (self.angle*((n+1/4)*self.key_w-300)+300, 600-self.angle*self.key_h-self.h)
            point15_b = (self.angle*((n-1/4)*self.key_w-300)+300, 600-2*self.angle*self.key_h-2*self.h-self.h2)
            point16_b = (self.angle*((n+1/4)*self.key_w-300)+300, 600-2*self.angle*self.key_h-2*self.h-self.h2)
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



if __name__ == "__main__":
    pygame.init()
    piano_guita = PIANO_GUITA()

    screen = pygame.display.set_mode((1200, 600))
    while True:
        screen.fill((255, 255, 255))
        piano_guita.draw(screen)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()