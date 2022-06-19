import pygame, sys
from pygame.constants import QUIT
from guita_music import music_guita


class GUITA():
    def __init__(self):
        img1 = pygame.image.load("./images/img01.png")
        img2 = pygame.image.load("./images/img02.png")
        img3 = pygame.image.load("./images/img03.png")
        img4 = pygame.image.load("./images/img04.png")
        img5 = pygame.image.load("./images/img05.png")
        img6 = pygame.image.load("./images/img06.png")
        self.img = [img1, img2, img3, img4, img5, img6]
        # font_name = pygame.font.match_font('Muyao')
        font = pygame.font.Font('Muyao.ttf', 70)  # 15:font size
        text1 = font.render('C', True, (0, 0, 0))
        text2 = font.render('Dm', True, (0, 0, 0))
        text3 = font.render('Em', True, (0, 0, 0))
        text4 = font.render('F', True, (0, 0, 0))
        text5 = font.render('G', True, (0, 0, 0))
        text6 = font.render('Am', True, (0, 0, 0))
        self.text = [text1, text2, text3, text4, text5, text6]
        font1 = pygame.font.Font('Muyao.ttf', 60)
        self.mode1 = font1.render('弹唱', True, (125, 125, 125))
        self.mode2 = font1.render('指弹', True, (125, 125, 125))
        self.img_w = 90
        self.img_h = 120
        self.guita_h = 65
        self.y_list = []
        self.count = 5
        self.music = music_guita()
        self.high = 150
        for i in range(6):
            self.y_list.append(540 - i * self.guita_h)
        self.y_list1 = [600, 540, 475, 410, 345, 280, 215, -3]

    def draw(self, screen, play_mode):

        # for n in range(6):
        #     pygame.draw.line(screen, (0, 0, 0), (0, self.y_list[n]), (1200, self.y_list[n]), width = 2)
        pygame.draw.line(screen, (160, 160, 160), (380, self.y_list[5]), (380, self.y_list[0]), width = 6)

        for i in range(6):
            screen.blit(self.text[i], (i*200+10, 85))
            screen.blit(self.img[i], (i*200+95, 85))
        pygame.draw.rect(screen, (255, 255, 255), (850, 13, 330, 68), 0)

        pygame.draw.rect(screen, (230, 230, 230), ((685 + play_mode * 165, 13), (165, 68)), 0)
        screen.blit(self.mode1, (880, 20))
        screen.blit(self.mode2, (1030, 20))
    def judge(self, screen, key, y, player, play_mode, before, open = False):
        # number = []
        # key_C = {0: 48, 1: 44, 2: 48, 3: 51, 4: 44, 5: 48}
        # for i in range(6):
        #     if y <= self.y_list[i]+10 and y >= self.y_list[i]-10:
        #         a = int(key_C.get(i))
        #         player.note_on(a, 127)
        # pygame.draw.rect(screen, (200, 200, 200), (key * 200 + 10, 80, 180, 80), 0)
        if play_mode == 1:

            if open == False:
                pass

            elif y < self.y_list[0] and y > self.y_list[5] and open == True:
                # count = count + 1
                # if count == 3:
                if y > before+self.high:
                    self.music.music_play1(key, 1, player)
                elif y < before-self.high:
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
                        pygame.draw.line(screen, (175, 175, 175), (0, self.y_list[i + 1]), (1200, self.y_list[i + 1]),
                                         width=3)
                if end < start:
                    for i in range(start, end, -1):
                        pygame.draw.line(screen, (175, 175, 175), (0, self.y_list[i]), (1200, self.y_list[i]), width=3)
                self.music.music_play2(key, start, end, player)
            before = y
            return before
if __name__ == "__main__":

    pygame.init()
    guita = GUITA()

    screen = pygame.display.set_mode((1200, 600))
    while True:
        screen.fill((255, 255, 255))
        guita.draw(screen)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


