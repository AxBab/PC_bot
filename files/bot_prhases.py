from os import chdir
import pygame.mixer
from gtts import gTTS
from settings import user_name, programm_dir

def make_prhase(content, file_name):
    tts = gTTS(content, lang='ru')
    chdir(f"{programm_dir}/files")
    tts.save(f"{file_name}.mp3")


def say(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(f"{filename}.mp3")
    pygame.mixer.music.play()