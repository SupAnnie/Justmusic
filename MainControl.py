import glob
import os

import cv2
import pygame, sys
from comtypes import CLSCTX_ALL
from pycaw.api.endpointvolume import IAudioEndpointVolume
from pycaw.utils import AudioUtilities
from ctypes import cast, POINTER
from pygame.constants import QUIT
import HandTrackingModule as htm
import HandDrawingModule as hdm
import VolumeModule as vm
import ModeChoice as mc
import ActionIdentify as ai
import game3
import Playmain
import mp3tomidi
from moviepy.editor import *
from ActionIdentify import LSTM

pygame.init()
# 使用摄像头
cap = cv2.VideoCapture(0)
# 游戏界面设置
screen = pygame.display.set_mode((1200, 600))
# 音量控制
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# 创建手部检测的实体
detector = htm.handDetector(maxHands=1, detectionCon=0.75)
input = []
num = 0
action_identify = [2, 2]
current_mode = 1
next_mode = 1
game_return = 0
flag = False
dellist = []
mp3musiclist = glob.glob("*.mp3")

# print(mp3musiclist)
mp3musiclist2 = glob.glob("./MP3music/*.mp3")
print(mp3musiclist2)
mp3musiclist.extend(mp3musiclist2)
print(mp3musiclist)
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
    cv2.waitKey(33)
    # 得到手部的坐标列表[[[id],[x],[y],[z]],[第二只手],...]
    lmList1 = detector.findPosition1(img, draw=False)
    # print(lmList1)
    if len(lmList1) != 0:
        num = num + 1
        # print(lmList)
        # print(num)
        if (num <= 10):
            input.append(lmList1)
        else:
            for i in range(0, 9):
                input[i] = input[i + 1]
            input[9] = lmList1
            # print("input8:{}", format(input[8]))
    if len(input) == 10:
        # 获得神经网络的输入
        Detector2 = ai.ActionDetector(input)
        action = Detector2.GetAction()
        action_identify[0] = action_identify[1]
        action_identify[1] = action
        # gamemanager = game.Manager(screen)
        # print(action_identify)
    lmList = detector.findPosition(img, draw=False)
    # print(next_mode)
    mode = mc.Mode(screen, next_mode, lmList)
    current_mode, next_mode = mode.home()
    # print(next_mode)
    presslist = detector.pressornot()
    # if running == False:
    #     del mode
    # print(current_mode)
    # 1游戏

    # print(game_return)
    if current_mode == 1:
        pygame.mixer.music.stop()
        if action_identify == [2, 1]:
            next_mode = 2
        if action_identify == [2, 0]:
            next_mode = 4
            mode.MusicPlay()
    # 2演奏
    if current_mode == 2:
        if action_identify == [2, 1]:
            next_mode = 3
        if action_identify == [2, 0]:
            next_mode = 7
    # 3双人
    if current_mode == 3:
        if action_identify == [2, 1]:
            next_mode = 1
        if action_identify == [2, 0]:
            next_mode = 14
    # 4游戏选择1
    if current_mode == 4:
        if action_identify == [2, 1]:
            next_mode = 5
            mode.MusicPlay()
        if action_identify == [2, 0]:
            next_mode = 9
    # 5游戏选择2
    if current_mode == 5:
        if action_identify == [2, 1]:
            next_mode = 6
            mode.MusicPlay()
        if action_identify == [2, 0]:
            next_mode = 10
    # 6游戏选择3
    if current_mode == 6:
        if action_identify == [2, 1]:
            next_mode = 17
            mode.MusicPlay()
            if flag == True:
                pygame.mixer.music.stop()
                # pygame.mixer.music.load("./MP3music\\童话.mp3")
                # pygame.mixer.music.play(start=2.0)
                for musicmp3 in mp3musiclist:
                    print(musicmp3[11:-4])
                    if musicmp3[0:-4] == musicname or musicmp3[11:-4] == musicname:
                        pygame.mixer.music.load(musicmp3)
                        pygame.mixer.music.play(start=2.0)
                        break
            if flag == False:
                pygame.mixer.music.stop()
        if action_identify == [2, 0]:
            next_mode = 11
    # 15游戏选择5
    if current_mode == 15:
        pygame.mixer.music.stop()
        if action_identify == [2, 1]:
            next_mode = 4
            pygame.mixer.music.load(r'E:\project\bgmusic\dylanf - 天空之城（经典钢琴版）.mp3')
            pygame.mixer.music.play(start=2.0)
        if action_identify == [2, 0]:
            next_mode = 16
    # 17游戏选择4
    if current_mode == 17:
        # pygame.mixer.music.stop()
        if action_identify == [2, 1]:
            next_mode = 15
            # if flag == True:
            #
            #     pygame.mixer.music.stop()
            #     pygame.mixer.music.load('./MP3music/' + musicname + '.mp3')
            #     pygame.mixer.music.play(start=2.0)
            # mode.MusicPlay()
        if action_identify == [2, 0]:
            next_mode = 18
        if flag == True:
            pygame.draw.rect(screen, (255, 255, 255), (450, 150, 280, 280), 0)
            font1 = pygame.font.Font("Muyao.ttf", 60)
            text1 = font1.render(musicname, True, (125, 125, 125))
            # print(musicname)
            screen.blit(text1, (440, 250))

    # 7钢琴演奏
    if current_mode == 7:
        if action_identify == [2, 1]:
            next_mode = 8
        if action_identify == [2, 0]:
            next_mode = 12
    # 8吉他演奏
    if current_mode == 8:
        if action_identify == [2, 1]:
            next_mode = 7
        if action_identify == [2, 0]:
            next_mode = 13
    # 9游戏1 sky_city
    if current_mode == 9:
        gamemanager1 = game3.Manager(screen, cap, 2)
        next_mode = gamemanager1.main()
    # 10游戏2  little_star
    if current_mode == 10:
        gamemanager2 = game3.Manager(screen, cap, 3)
        next_mode = gamemanager2.main()
    # 11游戏3
    if current_mode == 11:
        gamemanager3 = game3.Manager(screen, cap, 1)
        next_mode = gamemanager3.main()
        # 12钢琴
    if current_mode == 12:
        GAME2 = Playmain.play_music(cap)
        next_mode = GAME2.play(0)
        # next_mode = GAME2.Return()
        # print(game_return)
        # 13吉他
    if current_mode == 13:
        GAME3 = Playmain.play_music(cap)
        next_mode = GAME3.play(1)
        # 14双人
    if current_mode == 14:
        GAME4 = Playmain.play_music(cap)
        next_mode = GAME4.play(2)
    # 选歌
    if current_mode == 16:
        dirs = os.listdir("./music/")
        for savename in dirs:
            if (savename != "lemon.mid") and (savename != "lemon_note.csv") and (savename != "little_star.mid") and \
                    (savename != "little_star_note.csv") and (savename != "sky_city.mid") and (
                    savename != "sky_city_note.csv"):
        #         if len(dellist) < 2:
        #             dellist.append(savename)
        # for delname in dellist:
                os.remove('./music/' + savename)
        GAME4 = mp3tomidi.Manager(cap, screen)
        next_mode = GAME4.main()
        musicname, flag = GAME4.getmusicname()
    # 游戏4
    if current_mode == 18:
        gamemanager4 = game3.Manager(screen, cap, 4)
        next_mode = gamemanager4.main()
    # 添加歌曲


        # if current_mode2 == 1:
        #     if current_mode1 != 1 and action == 1:
        #         current_mode2 = 0
        #         current_mode1 = 1


            # time.sleep(1)
            # continue
        # print("action:{}".format(action))
        # print(current_mode)

    # gamemanager = game.Manager(screen)
    # gamemanager.main()

    # if next_mode == 9:
    #     gamemanager = game.Manager(screen)
    #     gamemanager.main()

    # 创建画出手部的实体
    handmodel = hdm.Hand(screen, lmList, presslist)
    # 画出手部坐标和骨架
    handmodel.drawhand()

    # 创建音量实体
    volumeobj = vm.Volume(screen, lmList, volume)
    # 画出音量表示
    volumeobj.showvolume()
    # next_mode = volumeobj.home()
    pygame.display.update()
