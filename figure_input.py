import cv2 as cv
def drawline(x, y, List, img):
    img_size = 128
    i1_x = int(List[3*x+1] * img_size)
    i1_y = int(List[3*x+2] * img_size)
    if i1_x > img_size - 1:
        i1_x = img_size - 1
    if i1_y > img_size - 1:
        i1_y = img_size - 1

    i2_x = int(List[3 * y+1] * img_size)
    i2_y = int(List[3 * y + 2] * img_size)
    if i2_x > img_size - 1:
        i2_x = img_size - 1
    if i2_y > img_size - 1:
        i2_y = img_size - 1
    cv.line(img, (i1_x, i1_y), (i2_x, i2_y), 255, 2)
def drawlines(x, List, img):
    drawline(x, x+1, List, img)
    drawline(x+1, x+2, List, img)
    drawline(x+2, x+3, List, img)

def drawhand(List, img):
    drawlines(1, List, img)
    drawlines(5, List, img)
    drawlines(9, List, img)
    drawlines(13, List, img)
    drawlines(17, List, img)

    drawline(0, 5, List, img)
    drawline(5, 9, List, img)
    drawline(9, 13, List, img)
    drawline(13, 17, List, img)
    drawline(0, 17, List, img)
    drawline(0, 1, List, img)