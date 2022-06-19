import glob
import os
import time
import pygame
import cv2
import HandTrackingModule as htm
import HandDrawingModule as hdm
import pandas as pd
import numpy as np
import pygame.midi
import ModeChoice as mc
from mido import Message, MidiFile, MidiTrack


class GameSound(object):
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.set_num_channels(32)
        freq = 44100
        bitsize = -16
        channels = 16
        buffer = 1024
        pygame.mixer.init(freq, bitsize, channels, buffer)
        pygame.midi.init()

    def playBGMmp3(self, file):     #不会暂停
        s = pygame.mixer.Sound(file)
        pygame.mixer.Sound.play(s).set_volume(0.4)

    def playBGMmid(self, file):     #可以暂停
        pygame.mixer.music.load(file)
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play(1)
        pygame.mixer.music.pause()
    def playSound(self,List):   #不会暂停
        keyDict={1:'c1',2:'c1#',3:'d1',4:'d1#',5:'e1',6:'f1',7:'f1#',8:'g1',9:'g1#',10:'a1',11:'a1#',12:'b1',13:'c2',14:'c2#',15:'d2',16:'d2#',17:'e2',18:'f2',19:'f2#',20:'g2',21:'g2#',22:'a2',23:'a2#',24:'b2'}
        for i in List:
            # pygame.mixer.Sound("audios2/" + keyDict[i] + " (V0).mp3").set_volume(0.01)
            pygame.mixer.Sound("audios2/" + keyDict[i] + " (V0).mp3").play(maxtime=2500).set_volume(0.2)

        # keyDict={1:60,2:61,3:62,4:63,5:64,6:65,7:66,8:67,9:68,10:69,11:70,12:71,13:72,14:73,15:74,16:75,17:76,18:77,19:78,20:79,21:80,22:81,23:82,24:83}
        #
        #
        # player = pygame.midi.Output(0)
        # player.set_instrument(0)  # 选择乐器
        # for i in List:
        #     player.note_on(note=keyDict[i],channel=2,velocity=64,time=0)
        #     player.note_off(note=keyDict[i],channel=2,velocity=64,time=1000)
        # del player
        # # pygame.midi.quit()


class Note(pygame.sprite.Sprite):       #音符类，继承精灵类
    def __init__(self,screen,notelist,delta):
        pygame.sprite.Sprite.__init__(self)     #调用精灵类的初始化方法
        self.image=pygame.image.load("./images/note.png")
        self.screen = screen
        self.rect=self.image.get_rect()     #获取矩形对象
        self.speed = 5
        self.rect.x=notelist[0]-15      #减去图片宽度的一半
        self.rect.y=-30      #减去图片长度
        self.time=(notelist[2])*delta #减去图片下落到中点的时间（300/5/20 )
        self.keyind=notelist[3]
        #self.is_coming=False
    def update(self,time):
        if time>=self.time+1:
            self.rect.y = self.rect.y + self.speed
            if self.rect.y > 300-30:
                self.kill()
        #     if self.rect.y > 250:
        #         print(self.keyind)
        #         print("is coming")
        #         self.is_coming = True
        #     else:
        #         self.is_coming=False
        # return self.is_coming


class Key(pygame.sprite.Sprite):
    def __init__(self,screen,ind):
        #pygame.sprite.Sprite.__init__(self)
        self.image1=pygame.image.load("./images/key1.png")
        self.image2=pygame.image.load("./images/key2.png")
        self.image3=pygame.image.load("./images/key3.png")
        self.image4=pygame.image.load("./images/key4.png")
        self.screen = screen
        self.ind=ind
    def update(self):
        if self.ind==1:
            self.screen.blit(self.image1,(0,300))
        elif self.ind==2:
            self.screen.blit(self.image2,(63,300))
        elif self.ind==3:
            self.screen.blit(self.image3, (87, 300))
        elif self.ind==4:
            self.screen.blit(self.image2,(147,300))
        elif self.ind==5:
            self.screen.blit(self.image4,(171,300))
        elif self.ind==6:
            self.screen.blit(self.image1,(257,300))
        elif self.ind==7:
            self.screen.blit(self.image2,(320,300))
        elif self.ind==8:
            self.screen.blit(self.image3,(343,300))
        elif self.ind==9:
            self.screen.blit(self.image2,(405,300))
        elif self.ind==10:
            self.screen.blit(self.image3,(429,300))
        elif self.ind==11:
            self.screen.blit(self.image2,(490,300))
        elif self.ind==12:
            self.screen.blit(self.image4,(514,300))
        elif self.ind==13:
            self.screen.blit(self.image1,(600,300))
        elif self.ind==14:
            self.screen.blit(self.image2,(662,300))
        elif self.ind==15:
            self.screen.blit(self.image3,(686,300))
        elif self.ind==16:
            self.screen.blit(self.image2,(747,300))
        elif self.ind==17:
            self.screen.blit(self.image4,(771,300))
        elif self.ind==18:
            self.screen.blit(self.image1,(857,300))
        elif self.ind==19:
            self.screen.blit(self.image2,(918,300))
        elif self.ind==20:
            self.screen.blit(self.image3,(943,300))
        elif self.ind==21:
            self.screen.blit(self.image2,(1005,300))
        elif self.ind==22:
            self.screen.blit(self.image3,(1028,300))
        elif self.ind==23:
            self.screen.blit(self.image2,(1090,300))
        elif self.ind==24:
            self.screen.blit(self.image4,(1112,300))


class StatusButton(object):
    def __init__(self,screen):
        #"image_name“接收一个元组，元组的0下标必须是暂停的图片，1下标必须是运行的图片
        #super(StatusButton,self).__init__(*groups)
        #准备用于切换显示的两张图片
        image_names=('pause.png','resume.png')
        self.screen=screen
        self.images=[pygame.image.load("./images/"+name)for name in image_names]
        self.image=self.images[0]
        # self.rect = self.image.get_rect()
        # self.rect.topleft=(1100,0)
    def switch_status(self,is_pause):
        #根据是否暂停，切换要使用的图片对象
        self.image=self.images[1 if is_pause else 0]

class Manager(object):
    def __init__(self, screen, cap, mode):
        pygame.init()
        self.screen=screen
        self.background = pygame.image.load("./images/background.png")  # 导入背景图片
        self.kbg=pygame.image.load("images/kbg.png")
        self.notes=pygame.sprite.Group()        #音符组
        self.sound=GameSound()                  #初始化播放器
        self.status = StatusButton(self.screen)
        self.cap = cap
        self.mode = mode
        self.dirs = os.listdir("./music/")
        print(self.dirs)
        csv = []
        for i in self.dirs:
            if i[-1] == "v":
                csv.append(i)
        for i in range(len(csv)):
            if (csv[i] != "lemon_note.csv") and (csv[i] != "little_star_note.csv") and (csv[i] != "sky_city_note.csv"):
                newcsv = csv[i]
        # print(newcsv)
        if self.mode == 1:
            NOTE=pd.read_csv("./music/little_star_note.csv",header=None)    #初始化NOTE列表
        elif self.mode == 2:
            NOTE = pd.read_csv("./music/sky_city_note.csv", header=None)
        elif self.mode == 3:
            NOTE = pd.read_csv("./music/lemon_note.csv", header=None)
        elif self.mode == 4:
            NOTE = pd.read_csv('./music/' + newcsv, header=None)
        NOTE=np.array(NOTE)
        self.NOTEList=[]
        for i in NOTE:
            self.NOTEList.append(i)
        self.NOTE_num=len(self.NOTEList)
        self.score=0
        #self.is_coming=False
        self.keyind=None
    def exit(self):
        print('退出')
        pygame.quit()
        exit()
    def new_note(self,list,delta):
        note=Note(self.screen,list,delta)
        self.notes.add(note)
    def cal_score(self,HandList,time):
        # if self.is_coming==True:
        #     if len(HandList)>=1:
        #         if int(self.keyind)==HandList[0]:
        #             print("yes")
        #             self.score = self.score + round(100 / self.NOTE_num, 1)
        for i in self.NOTEList:
            if abs(i[2]+8-time)<=0.5:
                if len(HandList)>=1:
                    #print(HandList[0])
                    #print(int(i[3]))
                    if HandList[0]==int(i[3]):
                        print("yes")
                        self.score=self.score+round(100/self.NOTE_num)
                        #print("score:",self.scroe)
    def drawText(self,text,x,y,textHeight=30,fontColor=(255,255,255),backgroundColor=None):
        #通过字体文件获取字体对象
        font_obj=pygame.font.Font("./text/muyao.ttf",textHeight)
        #配置要显示的文字
        text_obj=font_obj.render(text,True,fontColor,backgroundColor)
        #获取要显示的对象的rect
        text_rect=text_obj.get_rect()
        #设置要显示的对象的坐标
        text_rect.topleft=(x,y)
        #绘制字到指定的区域
        self.screen.blit(text_obj,text_rect)
    def main(self):
        # cap = cv2.VideoCapture(0)
        detector = htm.handDetector(detectionCon=0.75)
        self.screen.blit(self.background, (0, 0))  # 贴上背景图片
        self.screen.blit(self.kbg, (0, 300))  # 贴上琴键图片
        for i in self.NOTEList:
            self.new_note(i,60/60)  # 创建音符对象,并将它添加到精灵组里
        now=pygame.time.get_ticks()
        clock = pygame.time.Clock()
        time_pause_before=0
        delta_time=0
        sum_delta_time=0
        test=[[],[],[],[],[]]
        test2=[]
        delta_time_all=[0]
        myflag = True
        #flag = False
        mid = []
        for i in self.dirs:
            if i[-1] == "d":
                mid.append(i)
        for i in range(len(mid)):
            if (mid[i] != "lemon.mid") and (mid[i] != "little_star.mid") and (mid[i] != "sky_city.mid"):
                newmid = mid[i]
        # print(newmid)
        # self.newname = strmid[0:-5]
        if self.mode == 1:
            self.sound.playBGMmid("./music/little_star.mid")
        elif self.mode == 2:
            self.sound.playBGMmid("./music/sky_city.mid")
        elif self.mode == 3:
            self.sound.playBGMmid("./music/lemon.mid")
        elif self.mode == 4:
            self.sound.playBGMmid('./music/' + newmid)
        self.is_pause=False
        while True:
            clock.tick(20)  # 每秒循环20次
            print(clock.get_time())
            if self.is_pause==True:
                pygame.mixer.music.pause()
                self.screen.blit(self.background, (0, 0))   #贴上背景图片
                self.screen.blit(self.kbg, (0, 300))  # 贴上琴键图片
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.exit() # 退出python程序
                success, img = self.cap.read()
                if success == True:
                    img = cv2.flip(img, 180)
                img = detector.findHands(img)
                lmList = detector.findPosition(img, draw=False)
                if self.mode == 1:
                    self.next_mode = 9
                if self.mode == 2:
                    self.next_mode = 10
                if self.mode == 3:
                    self.next_mode = 11
                if self.mode == 4:
                    self.next_mode = 18
                mode = mc.Mode(self.screen, self.next_mode, lmList)
                current_mode, self.next_mode = mode.home()
                if self.next_mode == 1:
                    return self.next_mode
                presslist = detector.pressornot()
                handmodel = hdm.Hand(self.screen, lmList, presslist)
                HandList=handmodel.getHandList()
                if len(presslist)==1:
                    if sum(presslist[0])==4:
                        self.is_pause=not self.is_pause
                # if len(HandList)==4:
                #     self.is_pause=not self.is_pause
                self.notes.draw(self.screen)  # 显示音符
                self.drawText("SCORE:"+str(self.score), 0, 0)  # 显示分数
                self.drawText("The game is paused",450,180,textHeight=40)
                self.screen.blit(self.status.images[0], (1100, 0))
                handmodel.drawhand()    #画手
                handmodel.magnifydot()  #放大
                pygame.display.update()     #刷新窗口内容
                time_pause_after=(pygame.time.get_ticks() - now) / 1000
                delta_time=time_pause_after-time_pause_before

            elif self.is_pause==False:
                if delta_time != delta_time_all[-1]:
                    delta_time_all.append(delta_time)
                #print(delta_time_all)
                sum_delta_time=sum(delta_time_all)
                time=(pygame.time.get_ticks()-now)/1000-sum_delta_time
                #print(time)
                if time>=6.5:         #当时间=1+300/5/20时，才开始播放bgm
                    pygame.mixer.music.unpause()
                    if self.mode==4:
                        if myflag == True:
                            mp3musiclist = glob.glob("*.mp3")
                            print(mp3musiclist)
                            for musicmp3 in mp3musiclist:
                                if musicmp3[:-4] == newmid[:-4]:
                                    print("playplay")
                                    self.sound.playBGMmp3('./output2/' + newmid[:-4] + "/bass.mp3")
                                    self.sound.playBGMmp3('./output2/' + newmid[:-4] + "/drums.mp3")
                                    self.sound.playBGMmp3('./output2/' + newmid[:-4] + "/vocals.mp3")
                                    self.sound.playBGMmp3('./output2/' + newmid[:-4] + "/other.mp3")
                                    myflag=False
                                    break

                self.screen.blit(self.background, (0, 0))   #贴上背景图片
                self.screen.blit(self.kbg, (0, 300))  # 贴上琴键图片
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.exit() # 退出python程序
                success, img = self.cap.read()
                if success == True:
                    img = cv2.flip(img, 180)
                img = detector.findHands(img)
                lmList = detector.findPosition(img, draw=False)
                presslist = detector.pressornot()
                handmodel = hdm.Hand(self.screen, lmList, presslist)
                HandList=handmodel.getHandList()
                if len(presslist)==1:
                    if sum(presslist[0])==4:
                        self.is_pause=not self.is_pause
                if len(test2)==5:
                    test2[0]=test2[1]
                    test2[1]=test2[2]
                    test2[2]=test2[3]
                    test2[3]=test2[4]
                    test2[4]=presslist[0]
                # if len(HandList)==4:
                #     self.is_pause=not self.is_pause
                if HandList not in test:
                    self.sound.playSound(HandList)  # 播放琴键的声音
                    for i in HandList:          #琴键按下的动画
                        key=Key(self.screen,i)
                        key.update()
                    self.cal_score(HandList,time)  #计算分数
                #print(test)
                if len(test)==5:
                    test[0]=test[1]
                    test[1]=test[2]
                    test[2]=test[3]
                    test[3]=test[4]
                    test[4]=HandList
                #print(len(self.notes))
                if len(self.notes)==0:
                    self.drawText("The game is over",450,90,textHeight=40)
                    self.drawText("Your score is "+str(self.score),450,180,textHeight=40)
                self.drawText("SCORE:"+str(self.score), 0, 0)  # 显示分数
                self.notes.update(time)     #更新音符
                self.notes.draw(self.screen)    #显示音符
                self.screen.blit(self.status.images[1], (1100, 0))
                handmodel.drawhand()    #画手
                handmodel.magnifydot()  #放大
                pygame.display.update()     #刷新窗口内容
                time_pause_before=(pygame.time.get_ticks() - now) / 1000

if __name__=='__main__':
    pygame.init()
    # 使用摄像头
    cap = cv2.VideoCapture(0)
    # 游戏界面设置
    screen = pygame.display.set_mode((1200, 600))
    manager = Manager(screen, cap, 2)
    manager.main()