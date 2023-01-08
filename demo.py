from tkinter.ttk import *
from tkinter import *

from pygame import mixer

# window
window = Tk()
window.title("")
window.geometry('350x150') 


def sound_alarm():
    mixer.music.load('La Casa De Papel - Bella Ciao (Money Heist).mp3')
    mixer.music.play()

mixer.init()
sound_alarm()
window.mainloop()
