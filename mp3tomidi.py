import time
import os
import numpy as np
import pandas as pd
import mido
from mido import Message, MidiFile, MidiTrack,MetaMessage
import pygame
import pygame.midi
from moviepy.audio.io.AudioFileClip import AudioFileClip
from piano_transcription_inference import PianoTranscription, sample_rate, load_audio
import cv2
import HandTrackingModule as htm
import HandDrawingModule as hdm
from mido import Message, MidiFile, MidiTrack
import os
import subprocess
import glob
import ModeChoice as mc

class Manager(object):
    def __init__(self, cap, screen):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.set_num_channels(32)
        self.screen = screen
        self.cap = cap
        self.background = pygame.image.load("./images/background.png")  # 导入背景图片
        self.ind=0
        self.flag=None      #是否确认
        self.flag2=None     #纯钢琴MP3转换是否完成
        self.flag3=None     #混合MP3转换是否完成
        self.choice=None
        freq = 44100
        bitsize = -16
        channels = 16
        buffer = 1024
        pygame.mixer.init(freq, bitsize, channels, buffer)
        pygame.mixer.music.set_volume(1)
    def exit(self):
        print('退出')
        pygame.quit()
        exit()
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
    def choose(self,lmList):
        if len(lmList) == 1:
            x = lmList[0][8][1]
            y = lmList[0][8][2]
            if (100+20<=x<=600-20) and (220+10<=y<=290-10):
                self.ind=1
                self.choice=1
            elif (100+20<=x<=600-20) and (290+10<=y<=360-10):
                self.ind=2
                self.choice = 1
            elif (100+20<=x<=600-20) and (360+10<=y<=430-10):
                self.ind=3
                self.choice = 1
            elif (100+20<=x<=600-20) and (430+10<=y<=500-10):
                self.ind=4
                self.choice = 1
            elif (100+20<=x<=600-20) and (500+10<=y<=570-10):
                self.ind=5
                self.choice = 1
            elif (600+20<=x<=1100-20) and (220+10<=y<=290-10):
                self.ind=6
                self.choice = 2
            elif (600+20<=x<=1100-20) and (290+10<=y<=360-10):
                self.ind=7
                self.choice = 2
            elif (600+20<=x<=1100-20) and (360+10<=y<=430-10):
                self.ind=8
                self.choice = 2
            elif (600+20<=x<=1100-20) and (430+10<=y<=500-10):
                self.ind=9
                self.choice = 2
            elif (600+20<=x<=1100-20) and (500+10<=y<=570-10):
                self.ind=10
                self.choice = 2
    def choose2(self,lmList):
        if len(lmList) == 1:
            x = lmList[0][8][1]
            y = lmList[0][8][2]
            if (200<=x<=350) and (250<=y<=300):
                self.instru="bass"
                pygame.mixer.music.load("./output2/"+self.filename[:-4]+"/bass.mp3")
                pygame.mixer.music.play(1)
            elif (500<=x<=650) and (250<=y<=300):
                self.instru="piano"
                pygame.mixer.music.load("./output2/"+self.filename[:-4]+"/piano.mp3")
                pygame.mixer.music.play(1)
            elif (800<=x<=950) and (250<=y<=300):
                self.instru="drums"
                pygame.mixer.music.load("./output2/"+self.filename[:-4]+"/drums.mp3")
                pygame.mixer.music.play(1)
            elif (300<=x<=450) and (400<=y<=450):
                self.instru="vocals"
                pygame.mixer.music.load("./output2/"+self.filename[:-4]+"/vocals.mp3")
                pygame.mixer.music.play(1)
            elif (650<=x<=800) and (400<=y<=450):
                self.instru="other"
                pygame.mixer.music.load("./output2/"+self.filename[:-4]+"/other.mp3")
                pygame.mixer.music.play(1)
    def verify(self,lmList):
        if len(lmList) == 1:
            x = lmList[0][8][1]
            y = lmList[0][8][2]
            if (900<=x<=1050) and (120<=y<=160):
                #print("Sure")
                self.flag=True
            elif (1075<=x<=1225) and (120<=y<=160):
                #print("Not sure")
                self.flag=False
                self.ind=0
    def trans(self):
        if self.flag==True:
            self.filename = self.files1[self.ind - 1]
            self.ind=0
            self.flag=False     #不再进行转换
            self.screen.blit(self.background, (0, 0))  # 贴上背景图片
            self.drawText("Please Choose one MP3 File", 350, 50, textHeight=40)
            self.drawText("The new song is being converted. Please wait for a few minutes.", 20, 120, textHeight=40,
                          fontColor=(141, 174, 217))
            k=1
            for i in self.files1:
                if k<=5:
                    self.drawText(str(k)+". "+i,100,150+70*k,textHeight=40)
                k=k+1
            k=1
            for i in self.files2:
                if k<=5:
                    self.drawText(str(k+5)+". "+i,600,150+70*k,textHeight=40)
                k=k+1
            pygame.display.update()  # 刷新窗口内容
            #time.sleep(5)
            # 加载所选的mp3文件，所有MP3文件存储在MP3music文件夹下
            (audio, _) = load_audio('./MP3music/'+self.filename, sr=sample_rate, mono=True)
            # 选择转换器
            transcriptor = PianoTranscription(device='cpu')  # 'cuda' | 'cpu'
            # mp3转换成midi，所有暂存的MIDI文件存储在MIDImusic文件夹下
            transcribed_dict = transcriptor.transcribe(audio, './MIDImusic/'+self.filename[:-4]+'.mid')
            # 读取mid文件
            mid = mido.MidiFile('./MIDImusic/'+self.filename[:-4]+'.mid')
            print('The length of mid is '+str(mid.length))
            #第一次改写mid文件
            mid1 = MidiFile()
            track0_1 = MidiTrack()
            track1_1 = MidiTrack()
            mid1.tracks.append(track0_1)
            mid1.tracks.append(track1_1)
            for i, track in enumerate(mid.tracks):  #enumerate()：创建索引序列，索引初始为0
                if i==0:
                    for msg in track:
                        track0_1.append(msg)
                if i==1:
                    for msg in track:
                        track1_1.append(msg)
            mid1.save('./MIDImusic/'+self.filename[:-4]+'1.mid')
            print('The length of mid1 is '+str(mid1.length))
            #第二次改写mid1文件，mid2文件记录伴奏。note文件记录下落的时间time、音符的序号note（音符的序号需要在59-83之间）
            mid2 = MidiFile()
            track0_2 = MidiTrack()
            track1_2 = MidiTrack()
            mid2.tracks.append(track0_2)
            mid2.tracks.append(track1_2)
            k=0
            time=0
            keyDict={60:42.85714286,61:85.71428571,62:128.5714286,63:171.4285714,64:214.2857143,65:300,66:342.8571429,
                     67:385.7142857,68:428.5714286,69:471.4285714,70:514.2857143,71:557.1428571,72:642.8571429,
                     73:685.7142857,74:728.5714286,75:771.4285714,76:814.2857143,77:900,78:942.8571429,79:985.7142857,
                     80:1028.571429,81:1071.428571,82:1114.285714,83:1157.142857}
            noteall=[]
            for i, track in enumerate(mid1.tracks):  #enumerate()：创建索引序列，索引初始为0
                if i==0:
                    for msg in track:
                        #print(msg)
                        track0_2.append(msg)
                if i==1:
                    for msg in track:
                        msg_str=str(msg).split(" ")
                        # print(msg_str)
                        if msg_str[0] != ("MetaMessage('end_of_track',") and (msg_str[0] != "<meta"):
                            time = time + int(msg_str[-1][5:])
                            #print(time)
                        if msg_str[0]=="note_on":        #是音符
                            if 60<=int(msg_str[2][5:])<=83:    #处于中间两个八度
                                if int(msg_str[3][9:])>=63:     #音量较大
                                    k = k + 1
                                    if k%8==0:                  #每三个满足条件的音符取一个
                                        note=msg_str[2][5:]
                                        onenote=[keyDict[int(note)],0,time/1000,int(note)-59]
                                        noteall.append(onenote)
                                        # print(onenote)
                                    else:
                                        track1_2.append(msg)
                                else:
                                    track1_2.append(msg)
                            else:
                                track1_2.append(msg)
                        else:
                            track1_2.append(msg)
            noteall=np.array(noteall)
            df=pd.DataFrame(noteall)
            df.to_csv('./music/'+self.filename[:-4]+'note.csv',header=None,index=None)
            mid2.save('./music/'+self.filename[:-4]+'.mid')
            # print('The length of mid2 is '+str(mid2.length))
            self.flag2=True
    def trans2(self):
        if self.flag==True:
            self.filename = self.files2[self.ind - 6]
            print(self.filename)
            self.ind=0
            self.flag=False     #不再进行转换
            self.screen.blit(self.background, (0, 0))  # 贴上背景图片
            self.drawText("Please Choose one MP3 File", 350, 50, textHeight=40)
            self.drawText("The song is being separated. Please wait for a few minutes.", 20, 120, textHeight=40,
                          fontColor=(141, 174, 217))
            k=1
            for i in self.files1:
                if k<=5:
                    self.drawText(str(k)+". "+i,100,150+70*k,textHeight=40)
                k=k+1
            k=1
            for i in self.files2:
                if k<=5:
                    self.drawText(str(k+5)+". "+i,600,150+70*k,textHeight=40)
                k=k+1
            pygame.display.update()  # 刷新窗口内容
            # time.sleep(10)
            # 开始分离
            cmd = "spleeter separate -p spleeter:5stems -o output " + self.filename
            subprocess.call(cmd, shell=True)
            # 将分离后的wav文件转为mp3文件
            input_path = "./output/" + self.filename[:-4]
            output_path = "./output2/" + self.filename[:-4]
            os.makedirs(output_path)
            nfile = os.listdir(input_path)
            for file in nfile:
                path1 = input_path + "/" + file
                path2 = output_path + "/" + os.path.splitext(file)[0]
                cmd = "ffmpeg -i " + path1 + " " + path2 + ".mp3"  # 将input_path路径下所有音频文件转为.mp3文件
                subprocess.call(cmd, shell=True)
            au = AudioFileClip("./output2/" + self.filename[:-4] + "/piano.mp3")
            new_au = au.fl_time(lambda t: 0.8 * t, apply_to=['mask', 'audio'])  # 1.1表示调整速度
            new_au = new_au.set_duration(au.duration / 0.8)  # 1.1表示调整速度
            new_au.write_audiofile("./output2/" + self.filename[:-4] + "/piano1.mp3")
            (audio, _) = load_audio('./output2/'+self.filename[:-4]+"/piano1.mp3", sr=sample_rate, mono=True)
            # 选择转换器
            transcriptor = PianoTranscription(device='cpu')  # 'cuda' | 'cpu'
            # mp3转换成midi，所有暂存的MIDI文件存储在MIDImusic文件夹下
            transcribed_dict = transcriptor.transcribe(audio, './MIDImusic/'+self.filename[:-4]+'.mid')
            # 读取mid文件
            mid = mido.MidiFile('./MIDImusic/'+self.filename[:-4]+'.mid')
            print('The length of mid is '+str(mid.length))
            #第一次改写mid文件
            mid1 = MidiFile()
            track0_1 = MidiTrack()
            track1_1 = MidiTrack()
            mid1.tracks.append(track0_1)
            mid1.tracks.append(track1_1)
            for i, track in enumerate(mid.tracks):  #enumerate()：创建索引序列，索引初始为0
                if i==0:
                    for msg in track:
                        track0_1.append(msg)
                if i==1:
                    for msg in track:
                        track1_1.append(msg)
            mid1.save('./MIDImusic/'+self.filename[:-4]+'1.mid')
            print('The length of mid1 is '+str(mid1.length))
            #第二次改写mid1文件，mid2文件记录伴奏。note文件记录下落的时间time、音符的序号note（音符的序号需要在59-83之间）
            mid2 = MidiFile()
            track0_2 = MidiTrack()
            track1_2 = MidiTrack()
            mid2.tracks.append(track0_2)
            mid2.tracks.append(track1_2)
            k=0
            time=0
            keyDict={60:42.85714286,61:85.71428571,62:128.5714286,63:171.4285714,64:214.2857143,65:300,66:342.8571429,
                     67:385.7142857,68:428.5714286,69:471.4285714,70:514.2857143,71:557.1428571,72:642.8571429,
                     73:685.7142857,74:728.5714286,75:771.4285714,76:814.2857143,77:900,78:942.8571429,79:985.7142857,
                     80:1028.571429,81:1071.428571,82:1114.285714,83:1157.142857}
            noteall=[]
            for i, track in enumerate(mid1.tracks):  #enumerate()：创建索引序列，索引初始为0
                if i==0:
                    for msg in track:
                        #print(msg)
                        track0_2.append(msg)
                if i==1:
                    for msg in track:
                        msg_str=str(msg).split(" ")
                        print(msg_str)
                        if msg_str[0] != ("MetaMessage('end_of_track',") and (msg_str[0] != "<meta"):
                            time = time + int(msg_str[-1][5:])
                            #print(time)
                        if msg_str[0]=="note_on":        #是音符
                            if 60<=int(msg_str[2][5:])<=83:    #处于中间两个八度
                                if int(msg_str[3][9:])>=63:     #音量较大
                                    k = k + 1
                                    if k%7==0:                  #每三个满足条件的音符取一个
                                        note=msg_str[2][5:]
                                        onenote=[keyDict[int(note)],0,time/1000,int(note)-59]
                                        noteall.append(onenote)
                                        print(onenote)
                                    else:
                                        track1_2.append(msg)
                                else:
                                    track1_2.append(msg)
                            else:
                                track1_2.append(msg)
                        else:
                            track1_2.append(msg)
            noteall=np.array(noteall)
            df=pd.DataFrame(noteall)
            df.to_csv('./music/'+self.filename[:-4]+'note.csv',header=None,index=None)
            mid2.save('./music/'+self.filename[:-4]+'.mid')
            print('The length of mid2 is '+str(mid2.length))
            self.flag3=True

    def main(self):
        # cap = cv2.VideoCapture(0)
        detector = htm.handDetector(detectionCon=0.75)
        self.screen.blit(self.background, (0, 0))  # 贴上背景图片
        self.files1 = os.listdir("./MP3music")  # 纯钢琴mp3的所有文件名称
        self.files2 = glob.glob( "*.mp3")   # 混合mp3的所有文件名称
        print(self.files1)
        print(self.files2)
        test = [0, 0, 0, 0, 0]
        self.next_mode = 16
        while True:
            for event in pygame.event.get():        #退出事件
                if event.type == pygame.QUIT:
                    self.exit() # 退出python程序
            self.screen.blit(self.background, (0, 0))   #贴上背景图片
            self.drawText("Please Choose one MP3 File", 350, 50, textHeight=40) #贴上文字：请选文件
            if self.flag3 !=True:
                k=1
                for i in self.files1:
                    if k<=5:
                        self.drawText(str(k)+". "+i,100,150+70*k,textHeight=40)
                    k=k+1
                k=1
                for i in self.files2:
                    if k<=5:
                        self.drawText(str(k+5)+". "+i,600,150+70*k,textHeight=40)
                    k=k+1
            success, img = self.cap.read()       #检测手部
            if success == True:
                img = cv2.flip(img, 180)
            img = detector.findHands(img)
            lmList = detector.findPosition(img, draw=False)
            mode = mc.Mode(self.screen, self.next_mode, lmList)
            current_mode, self.next_mode = mode.home()
            if self.next_mode == 1:
                return self.next_mode
            presslist = detector.pressornot()
            handmodel = hdm.Hand(self.screen, lmList, presslist)
            if len(presslist)==1:       #检测一只手的食指（不能同时检测两只手，不能检测其它手指）
                if (presslist[0][1] ==1) and (presslist[0][1] not in test):
                    if self.flag3 !=True:
                        self.choose(lmList)     #检测到手指按下后，选择是哪一首，返回self.ind
                        self.verify(lmList)     #检测到手指按下后，是否确认，返回self.flag
                        print("a song has been chosen")
                    elif self.flag3==True:  #混合MP3转换完成
                        self.choose2(lmList)
                        #print(self.instru)
                test[0]=test[1]
                test[1]=test[2]
                test[2]=test[3]
                test[3]=test[4]
                test[4]=presslist[0][1]
            elif len(presslist)==0:
                test[0]=test[1]
                test[1]=test[2]
                test[2]=test[3]
                test[3]=test[4]
                test[4]=0
            if (self.ind != 0) and (self.flag2!=True) and (self.flag3 !=True):
                self.drawText("You've chosen the song "+str(self.ind)+".    Are you sure ?",80,120,textHeight=40,fontColor=(141,174,217))
                self.drawText("YES",925,120,textHeight=40,fontColor=(158,250,195))
                self.drawText("NO", 1075, 120, textHeight=40, fontColor=(254, 72, 72))
            if self.choice==1:
                self.trans()    #当self.flag=True时，执行转换程序，并将self.ind=0
            if self.choice==2:
                self.trans2()
            if self.flag2==True:
                self.drawText("The convertion is finished. Please return to the home screen.", 40, 120, textHeight=40,
                                fontColor=(141, 174, 217))
            if self.flag3==True:
                self.drawText("The separation is finished.", 350, 120, textHeight=40, fontColor=(141, 174, 217))
                self.drawText("Return to the home screen for play or click the bottom for audition.", 100, 190, textHeight=30, fontColor=(141, 174, 217))
                self.drawText("bass",200,250,textHeight=40)
                self.drawText("piano",500,250,textHeight=40)
                self.drawText("drums",800,250,textHeight=40)
                self.drawText("vocals",300,400,textHeight=40)
                self.drawText("other",650,400,textHeight=40)
            #print(self.instru)
            handmodel.drawhand()    #画手
            handmodel.magnifydot()  #放大
            pygame.display.update()     #刷新窗口内容

    def getmusicname(self):
        return self.filename[:-4], True

if __name__=='__main__':
    manager = Manager()
    manager.main()