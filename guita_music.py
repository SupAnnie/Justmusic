import pygame.midi as pm
import time
import numpy as np


class music_guita():
    def __init__(self):
        self.C = [76, 72, 67, 64, 60, 52]
        self.Dm = [77, 74, 69, 62, 57, 52]
        self.Em = [76, 71, 67, 64, 59, 52]
        self.F = [76, 72, 69, 65, 57, 52]
        self.G = [79, 71, 67, 62, 59, 55]
        self.Am = [76, 72, 69, 65, 57, 52]
        self.s = 0.015
    def music_play1(self, music, mode, player):
        music_key = {0:self.C, 1:self.Dm, 2:self.Em, 3:self.F, 4:self.G, 5:self.Am}
        if mode == 0:
            #向上
            for i in range(len(music_key.get(music))):
                player.note_on(music_key.get(music)[i], 127)
                time.sleep(self.s)
        else:
            #向下
            for i in range(len(music_key.get(music))-1, -1, -1):
                player.note_on(music_key.get(music)[i], 127)
                time.sleep(self.s)

    def music_play2(self, music, start, end, player):
        music_key = {0: self.C, 1: self.Dm, 2: self.Em, 3: self.F, 4: self.G, 5: self.Am}
        # if mode == 0:
        # if start > end:
        # 向上
        # for i in range(len(music_key.get(music))):
        if start == None or end == None:
            pass
        else:
            if end > start:
                for i in range(start, end):
                    player.note_on(music_key.get(music)[i + 1], 127)
                    # time.sleep(self.s)
            if end < start:
                for i in range(start, end, -1):
                    player.note_on(music_key.get(music)[i], 127)


if __name__ == "__main__":
    pm.init()
    player = pm.Output(0)
    player.set_instrument(24)
    MUSIC = music_guita()
    def music(key):
        s = 0.9
        MUSIC.music_play(key, 0, player)
        time.sleep(1*s)
        MUSIC.music_play(key, 0, player)
        time.sleep(0.5*s)
        MUSIC.music_play(key, 0, player)
        time.sleep(0.25*s)
        MUSIC.music_play(key, 1, player)
        time.sleep(0.25*s)

    music(3)
    music(4)
    music(2)
    music(5)
    music(1)
    music(4)
    music(0)
    music(0)



