import cv2
import pygame, sys
from pygame.constants import QUIT
import HandTrackingModule as htm


def drawlines(x, y, List):
    for id in range(x, y):
        pygame.draw.line(screen, (125, 125, 125), (List[id][1], List[id][2]), (List[id + 1][1], List[id + 1][2]), 4)

def drawline(x, y, List):
    pygame.draw.line(screen, (125, 125, 125), (List[x][1], List[x][2]), (List[y][1], List[y][2]), 4)

def drawhand(List):
    for id in range(0, 21):
        pygame.draw.circle(screen, (125, 125, 125), (List[id][1], List[id][2]), 8)

        # pygame.lines(surface, color, closed, pointlist, width=1)
    # pygame.draw.lines(screen, (0, 0, 255), False, [[0, 80], [50, 90], [200, 80], [220, 30]], 1)
    drawlines(0, 4, List)
    drawlines(5, 8, List)
    drawlines(9, 12, List)
    drawlines(13, 16, List)
    drawlines(17, 20, List)
    drawline(0, 5, List)
    drawline(5, 9, List)
    drawline(9, 13, List)
    drawline(13, 17, List)
    drawline(0, 17, List)

    # pygame.draw.lines(screen, c_color, False, line1, 4)
    # pygame.draw.lines(screen, c_color, False, line2, 4)

def magnifydot(lmList, presslist):
    tipIds = [4, 8, 12, 16, 20]
    for i in range(0, len(lmList)):
        for j in range(0, 5):
            if presslist[i][j] == 1:
                pygame.draw.circle(screen, (0, 0, 0), (lmList[i][tipIds[j]][1], lmList[i][tipIds[j]][2]), 12)

pygame.init()

cap = cv2.VideoCapture(0)
#cv2.namedWindow("Image", cv2.WINDOW_GUI_NORMAL)
#cv2.resizeWindow("Image", 800, 600)
#cap.set(3, 400)
#cap.set(4, 300)
screen = pygame.display.set_mode((1200, 600))

detector = htm.handDetector(detectionCon=0.75)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))

    success, img = cap.read()
    if success == True:
        img = cv2.flip(img, 180)


    img = detector.findHands(img)
    c_color = (125, 125, 125)
    lmList = detector.findPosition(img, draw=False)
    presslist = detector.pressornot()
    #print(presslist)
    magnifydot(lmList, presslist)

    #cv2.imshow("Image", img)
    #cv2.waitKey(1)

    #print(lmList)
    for num in range(0, len(lmList)):
        drawhand(lmList[num])


    pygame.display.update()






