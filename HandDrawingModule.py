import pygame
#画手的类
class Hand():
    def __init__(self, screen, lmList, presslist):
        self.lmList = lmList
        self.screen = screen
        self.presslist = presslist
        self.Handx=[]
        self.Handy=[]
        self.HandList=[]

    def drawlines(self, x, y, List):
        for id in range(x, y):
            pygame.draw.line(self.screen, (125, 125, 125), (List[id][1], List[id][2]), (List[id + 1][1], List[id + 1][2]), 4)

    def drawline(self, x, y, List):
        pygame.draw.line(self.screen, (125, 125, 125), (List[x][1], List[x][2]), (List[y][1], List[y][2]), 4)

    def drawhand(self):
        for num in range(0, len(self.lmList)):
            for id in range(0, 21):
                pygame.draw.circle(self.screen, (125, 125, 125), (self.lmList[num][id][1], self.lmList[num][id][2]), 8)
            self.drawlines(0, 4, self.lmList[num])
            self.drawlines(5, 8, self.lmList[num])
            self.drawlines(9, 12, self.lmList[num])
            self.drawlines(13, 16, self.lmList[num])
            self.drawlines(17, 20, self.lmList[num])
            self.drawline(0, 5, self.lmList[num])
            self.drawline(5, 9, self.lmList[num])
            self.drawline(9, 13, self.lmList[num])
            self.drawline(13, 17, self.lmList[num])
            self.drawline(0, 17, self.lmList[num])

    def magnifydot(self):
        tipIds = [4, 8, 12, 16, 20]
        for i in range(0, len(self.lmList)):
            for j in range(0, 5):
                if self.presslist[i][j] == 1:
                    pygame.draw.circle(self.screen, (0, 0, 0), (self.lmList[i][tipIds[j]][1], self.lmList[i][tipIds[j]][2]), 12)

    def getHandList(self):
        self.Handx=[]
        self.Handy=[]
        if len(self.lmList) == 1:
            if self.presslist[0][0] == 1:
                self.Handx.append(self.lmList[0][4][1])
                self.Handy.append(self.lmList[0][4][2])
            if self.presslist[0][1] == 1:
                self.Handx.append(self.lmList[0][8][1])
                self.Handy.append(self.lmList[0][8][2])
            if self.presslist[0][2] == 1:
                self.Handx.append(self.lmList[0][12][1])
                self.Handy.append(self.lmList[0][12][2])
            if self.presslist[0][3] == 1:
                self.Handx.append(self.lmList[0][16][1])
                self.Handy.append(self.lmList[0][16][2])
            if self.presslist[0][4] == 1:
                self.Handx.append(self.lmList[0][20][1])
                self.Handy.append(self.lmList[0][20][2])
        elif len(self.lmList) == 2:
            if self.presslist[0][0] == 1:
                self.Handx.append(self.lmList[0][4][1])
                self.Handy.append(self.lmList[0][4][2])
            if self.presslist[0][1] == 1:
                self.Handx.append(self.lmList[0][8][1])
                self.Handy.append(self.lmList[0][8][2])
            if self.presslist[0][2] == 1:
                self.Handx.append(self.lmList[0][12][1])
                self.Handy.append(self.lmList[0][12][2])
            if self.presslist[0][3] == 1:
                self.Handx.append(self.lmList[0][16][1])
                self.Handy.append(self.lmList[0][16][2])
            if self.presslist[0][4] == 1:
                self.Handx.append(self.lmList[0][20][1])
                self.Handy.append(self.lmList[0][20][2])
            if self.presslist[1][0] == 1:
                self.Handx.append(self.lmList[1][4][1])
                self.Handy.append(self.lmList[1][4][2])
            if self.presslist[1][1] == 1:
                self.Handx.append(self.lmList[1][8][1])
                self.Handy.append(self.lmList[1][8][2])
            if self.presslist[1][2] == 1:
                self.Handx.append(self.lmList[1][12][1])
                self.Handy.append(self.lmList[1][12][2])
            if self.presslist[0][3] == 1:
                self.Handx.append(self.lmList[1][16][1])
                self.Handy.append(self.lmList[1][16][2])
            if self.presslist[0][4] == 1:
                self.Handx.append(self.lmList[1][20][1])
                self.Handy.append(self.lmList[1][20][2])
        for i in range(0, len(self.Handx)):
            if (5 <= self.Handx[i] <= 61 and 305<=self.Handy[i]<=491) or (5<=self.Handx[i]<=82 and 501<=self.Handy[i]<=595):
                self.HandList.append(1)
            elif (71<= self.Handx[i]<=107) and (305<=self.Handy[i]<=491):
                self.HandList.append(2)
            elif (117 <= self.Handx[i] <= 145 and 305<=self.Handy[i]<=491) or (92<=self.Handx[i]<=169 and 501<=self.Handy[i]<=595):
                self.HandList.append(3)
            elif (155<= self.Handx[i]<=194) and (305<=self.Handy[i]<=491):
                self.HandList.append(4)
            elif (204 <= self.Handx[i] <= 254 and 305<=self.Handy[i]<=491) or (179<=self.Handx[i]<=254 and 501<=self.Handy[i]<=595):
                self.HandList.append(5)
            elif (264 <= self.Handx[i] <= 315 and 305 <= self.Handy[i] <= 491) or (264 <= self.Handx[i] <= 340 and 501 <= self.Handy[i]<=595):
                self.HandList.append(6)
            elif (325 <= self.Handx[i] <= 364) and (305 <= self.Handy[i] <= 491):
                self.HandList.append(7)
            elif (374 <= self.Handx[i] <= 401 and 305 <= self.Handy[i] <= 491) or (350 <= self.Handx[i] <= 424 and 501 <= self.Handy[i]<=595):
                self.HandList.append(8)
            elif (411 <= self.Handx[i] <= 448) and (305 <= self.Handy[i] <= 491):
                self.HandList.append(9)
            elif (458 <= self.Handx[i] <= 485 and 305 <= self.Handy[i] <= 491) or (434 <= self.Handx[i] <= 511 and 501 <= self.Handy[i] <= 595):
                self.HandList.append(10)
            elif (495 <= self.Handx[i] <= 535) and (305 <= self.Handy[i] <= 491):
                self.HandList.append(11)
            elif (545 <= self.Handx[i] <= 595 and 305 <= self.Handy[i] <= 491) or (511 <= self.Handx[i] <= 595 and 501 <= self.Handy[i] <= 595):
                self.HandList.append(12)
            elif (605 <= self.Handx[i] <= 661 and 305<=self.Handy[i]<=491) or (605<=self.Handx[i]<=682 and 501<=self.Handy[i]<=595):
                self.HandList.append(13)
            elif (671<= self.Handx[i]<=707) and (305<=self.Handy[i]<=491):
                self.HandList.append(14)
            elif (717 <= self.Handx[i] <= 745 and 305<=self.Handy[i]<=491) or (692<=self.Handx[i]<=769 and 501<=self.Handy[i]<=595):
                self.HandList.append(15)
            elif (755<= self.Handx[i]<=794) and (305<=self.Handy[i]<=491):
                self.HandList.append(16)
            elif (804 <= self.Handx[i] <= 854 and 305<=self.Handy[i]<=491) or (779<=self.Handx[i]<=854 and 501<=self.Handy[i]<=595):
                self.HandList.append(17)
            elif (864 <= self.Handx[i] <= 915 and 305 <= self.Handy[i] <= 491) or (864 <= self.Handx[i] <= 940 and 501 <= self.Handy[i]<=595):
                self.HandList.append(18)
            elif (925 <= self.Handx[i] <= 964) and (305 <= self.Handy[i] <= 491):
                self.HandList.append(19)
            elif (974 <= self.Handx[i] <= 1001 and 305 <= self.Handy[i] <= 491) or (950 <= self.Handx[i] <= 1024 and 501 <= self.Handy[i]<=595):
                self.HandList.append(20)
            elif (1011 <= self.Handx[i] <= 1048) and (305 <= self.Handy[i] <= 491):
                self.HandList.append(21)
            elif (1058 <= self.Handx[i] <= 1085 and 305 <= self.Handy[i] <= 491) or (1034 <= self.Handx[i] <= 1111 and 501 <= self.Handy[i] <= 595):
                self.HandList.append(22)
            elif (1095 <= self.Handx[i] <= 1135) and (305 <= self.Handy[i] <= 491):
                self.HandList.append(23)
            elif (1145 <= self.Handx[i] <= 1195 and 305 <= self.Handy[i] <= 491) or (1111 <= self.Handx[i] <= 1195 and 501 <= self.Handy[i] <= 595):
                self.HandList.append(24)
        return self.HandList