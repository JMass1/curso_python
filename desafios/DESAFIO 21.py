from pygame import mixer

mixer.init()
mixer.music.load('peste.mp3')
mixer.music.play(loops=3)
input()