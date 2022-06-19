from mido import Message, MidiFile, MidiTrack,MetaMessage

# def beat(time):            #与mido的拍子互换
#     time /= 60 * 1000
#     time = 1/time
#     return time
# print(beat(1000))

mid = MidiFile()
track = MidiTrack()
track2=MidiTrack()
track3=MidiTrack()
mid.tracks.append(track)
mid.tracks.append(track2)
mid.tracks.append(track3)
track.append(Message('program_change',channel=1, program=0, time=0))
track.append(Message('note_on', note=48, channel=1,velocity=127, time=0))       # 1
track.append(Message('note_off', note=48,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=55, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=55,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=52, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=52,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=55, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=55,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=48, channel=1,velocity=127, time=0))       #2
track.append(Message('note_off', note=48,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=53, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=53,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=55, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=55,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=53, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=53,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=48, channel=1,velocity=127, time=0))       #3
track.append(Message('note_off', note=48,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=57, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=57,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=53, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=53,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=57, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=57,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=48, channel=1,velocity=127, time=0))       #4
track.append(Message('note_off', note=48,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=55, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=55,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=60, channel=1,velocity=127, time=0))
track2.append(Message('note_on', note=64, channel=1,velocity=127, time=7000))
track.append(Message('note_off', note=60,channel=1, velocity=127, time=1000))
track2.append(Message('note_off', note=64,channel=1, velocity=127, time=1000))
track.append(Message('note_on', note=48, channel=1,velocity=127, time=0))       #5
track.append(Message('note_off', note=48,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=52, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=52,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=57, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=57,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=52, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=52,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=47, channel=1,velocity=127, time=0))       #6
track.append(Message('note_off', note=47,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=52, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=52,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=55, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=55,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=52, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=52,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=47, channel=1,velocity=127, time=0))       #7
track.append(Message('note_off', note=47,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=53, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=53,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=50, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=50,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=53, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=53,channel=1, velocity=127, time=250))
track.append(Message('note_on', note=55, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=55,channel=1, velocity=127, time=250))
track.append(Message('note_on', note=52, channel=1,velocity=127, time=0))       #8
track2.append(Message('note_on', note=55, channel=1,velocity=127, time=6000))
track3.append(Message('note_on', note=60, channel=1,velocity=127, time=14000))
track.append(Message('note_off', note=52,channel=1, velocity=127, time=1000))
track2.append(Message('note_off', note=55,channel=1, velocity=127, time=1000))
track3.append(Message('note_off', note=60,channel=1, velocity=127, time=1000))
track.append(Message('note_on', note=48, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=48,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=48, channel=1,velocity=127, time=500))       #9
track.append(Message('note_off', note=48,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=50, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=50,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=52, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=52,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=55, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=55,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=60, channel=1,velocity=127, time=0))       #10
track.append(Message('note_off', note=60,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=57, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=57,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=53, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=53,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=50, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=50,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=47, channel=1,velocity=127, time=0))       #11
track.append(Message('note_off', note=47,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=52, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=52,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=55, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=55,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=52, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=52,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=47, channel=1,velocity=127, time=0))       #12
track.append(Message('note_off', note=47,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=55, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=55,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=50, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=50,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=53, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=53,channel=1, velocity=127, time=250))
track.append(Message('note_on', note=55, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=55,channel=1, velocity=127, time=250))
track.append(Message('note_on', note=48, channel=1,velocity=127, time=0))       #13
track.append(Message('note_off', note=48,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=50, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=50,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=52, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=52,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=55, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=55,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=60, channel=1,velocity=127, time=0))       #14
track.append(Message('note_off', note=60,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=57, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=57,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=53, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=53,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=50, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=50,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=47, channel=1,velocity=127, time=0))       #15
track.append(Message('note_off', note=47,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=52, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=52,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=55, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=55,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=52, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=52,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=47, channel=1,velocity=127, time=0))       #16
track.append(Message('note_off', note=47,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=55, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=55,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=50, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=50,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=53, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=53,channel=1, velocity=127, time=250))
track.append(Message('note_on', note=55, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=55,channel=1, velocity=127, time=250))
track.append(Message('note_on', note=48, channel=1,velocity=127, time=0))       #17
track.append(Message('note_off', note=48,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=52, channel=1,velocity=127, time=0))
track2.append(Message('note_on', note=55, channel=1,velocity=127, time=17500))
track.append(Message('note_off', note=52,channel=1, velocity=127, time=500))
track2.append(Message('note_off', note=55,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=52, channel=1,velocity=127, time=0))
track2.append(Message('note_on', note=55, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=52,channel=1, velocity=127, time=500))
track2.append(Message('note_off', note=55,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=52, channel=1,velocity=127, time=0))
track2.append(Message('note_on', note=55, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=52,channel=1, velocity=127, time=500))
track2.append(Message('note_off', note=55,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=48, channel=1,velocity=127, time=0))       #18
track.append(Message('note_off', note=48,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=53, channel=1,velocity=127, time=0))
track2.append(Message('note_on', note=55, channel=1,velocity=127, time=500))
track.append(Message('note_off', note=53,channel=1, velocity=127, time=500))
track2.append(Message('note_off', note=55,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=53, channel=1,velocity=127, time=0))
track2.append(Message('note_on', note=55, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=53,channel=1, velocity=127, time=500))
track2.append(Message('note_off', note=55,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=53, channel=1,velocity=127, time=0))
track2.append(Message('note_on', note=55, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=53,channel=1, velocity=127, time=500))
track2.append(Message('note_off', note=55,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=48, channel=1,velocity=127, time=0))       #19
track.append(Message('note_off', note=48,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=53, channel=1,velocity=127, time=0))
track2.append(Message('note_on', note=57, channel=1,velocity=127, time=500))
track.append(Message('note_off', note=53,channel=1, velocity=127, time=500))
track2.append(Message('note_off', note=57,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=53, channel=1,velocity=127, time=0))
track2.append(Message('note_on', note=57, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=53,channel=1, velocity=127, time=500))
track2.append(Message('note_off', note=57,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=53, channel=1,velocity=127, time=0))
track2.append(Message('note_on', note=57, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=53,channel=1, velocity=127, time=500))
track2.append(Message('note_off', note=57,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=48, channel=1,velocity=127, time=0))       #20
track.append(Message('note_off', note=48,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=55, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=55,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=60, channel=1,velocity=127, time=0))
track2.append(Message('note_on', note=64, channel=1,velocity=127, time=1000))
track.append(Message('note_off', note=60,channel=1, velocity=127, time=500))
track2.append(Message('note_off', note=64,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=48, channel=1,velocity=127, time=500))       #21
track.append(Message('note_off', note=48,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=52, channel=1,velocity=127, time=0))
track2.append(Message('note_on', note=57, channel=1,velocity=127, time=1000))
track.append(Message('note_off', note=52,channel=1, velocity=127, time=500))
track2.append(Message('note_off', note=57,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=52, channel=1,velocity=127, time=0))
track2.append(Message('note_on', note=57, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=52,channel=1, velocity=127, time=500))
track2.append(Message('note_off', note=57,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=52, channel=1,velocity=127, time=0))
track2.append(Message('note_on', note=57, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=52,channel=1, velocity=127, time=500))
track2.append(Message('note_off', note=57,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=47, channel=1,velocity=127, time=0))       #22
track.append(Message('note_off', note=47,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=52, channel=1,velocity=127, time=0))
track2.append(Message('note_on', note=55, channel=1,velocity=127, time=500))
track.append(Message('note_off', note=52,channel=1, velocity=127, time=500))
track2.append(Message('note_off', note=55,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=52, channel=1,velocity=127, time=0))
track2.append(Message('note_on', note=55, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=52,channel=1, velocity=127, time=500))
track2.append(Message('note_off', note=55,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=52, channel=1,velocity=127, time=0))
track2.append(Message('note_on', note=55, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=52,channel=1, velocity=127, time=500))
track2.append(Message('note_off', note=55,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=47, channel=1,velocity=127, time=0))       #23
track.append(Message('note_off', note=47,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=50, channel=1,velocity=127, time=0))
track2.append(Message('note_on', note=53, channel=1,velocity=127, time=500))
track3.append(Message('note_on', note=55, channel=1,velocity=127, time=29500))
track.append(Message('note_off', note=50,channel=1, velocity=127, time=500))
track2.append(Message('note_off', note=53,channel=1, velocity=127, time=500))
track3.append(Message('note_off', note=55,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=47, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=47,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=50, channel=1,velocity=127, time=0))
track2.append(Message('note_on', note=53, channel=1,velocity=127, time=500))
track3.append(Message('note_on', note=55, channel=1,velocity=127, time=500))
track.append(Message('note_off', note=50,channel=1, velocity=127, time=500))
track2.append(Message('note_off', note=53,channel=1, velocity=127, time=500))
track3.append(Message('note_off', note=55,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=48, channel=1,velocity=127, time=0))       #24
track.append(Message('note_off', note=48,channel=1, velocity=127, time=500))
track.append(Message('note_on', note=60, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=60,channel=1, velocity=127, time=250))
track.append(Message('note_on', note=57, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=57,channel=1, velocity=127, time=250))
track.append(Message('note_on', note=55, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=55,channel=1, velocity=127, time=250))
track.append(Message('note_on', note=53, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=53,channel=1, velocity=127, time=250))
track.append(Message('note_on', note=52, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=52,channel=1, velocity=127, time=250))
track.append(Message('note_on', note=50, channel=1,velocity=127, time=0))
track.append(Message('note_off', note=50,channel=1, velocity=127, time=250))
track.append(Message('note_on', note=48, channel=1,velocity=127, time=0))       #25
track.append(Message('note_off', note=48,channel=1, velocity=127, time=2000))




mid.save('./music/little_star.mid')


# def play_midi(file):
#    freq = 44100
#    bitsize = -16
#    channels = 2
#    buffer = 1024
#    pygame.mixer.init(freq, bitsize, channels, buffer)
#    pygame.mixer.music.set_volume(1)
#    clock = pygame.time.Clock()
#    try:
#        pygame.mixer.music.load(file)
#    except:
#        import traceback
#        print(traceback.format_exc())
#    pygame.mixer.music.play()
#    while pygame.mixer.music.get_busy():
#        clock.tick(30)