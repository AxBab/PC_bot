import speech_recognition as sr  # listen the microphone

from os import system, chdir # control the system
from webbrowser import open # open sites

from bot_prhases import make_prhase, say # manipulate a sound
from invoker_mode import invoker_mode # auto casting skills
from clock import timer # control time
from action_with_folders import create_folder, remove_folder # manipulate a folders
from settings import bot_name, user_name # have data about programm


make_prhase(f"Хорошо {user_name}", "yes_master")
make_prhase("Эй ты че совсем офигел кожаный мешок? Сам ты дурак тупой, хахахахахахахахахахахаха", "daring_answer")
make_prhase(f"До встречи {user_name}", "goodbye")

r = sr.Recognizer() # understand speech
mic = sr.Microphone() # listen microphone
sr.LANGUAGE = 'ru-RU' # language for understanding speech


while True: # start a infinity cycle for listen and execute a commands
    with mic as source:
        print("Скажите что-нибудь...")

        r.adjust_for_ambient_noise(source) # reduce a extra noise
        audio = r.listen(source)

    # construction for catch errors and continue a cycly
    try:
        text = r.recognize_google(audio, language='ru-RU') # translate speech from audio to word
    except:
        continue

    print(f'Вы сказали: {text}')
    
    if text.split()[0] == bot_name:
        text = " ".join(text.split()[1:]).lower()
        print(f'text после обработки: {text}')

        if text == "запусти dota":
            print(f"{bot_name} запустил доту")
            say("yes_master")
            open("steam://rungameid/570", new=0, autoraise=True)
        

        elif text == "выключи компьютер":
            say("goodbye")
            system("shutdown /s /t 2")


        elif "посчитай" in text:
            make_prhase(" ".join(text.split()[1:]) + " = " + str(eval(" ".join(text.split()[1:]).replace("х", "*"))), "task")
            say("task")
            print(" ".join(text.split()[1:]) + " = " + str(eval(" ".join(text.split()[1:]).replace("х", "*"))))


        elif "поставь таймер на" in text:
            say("yes_master")
            text = text.split()
            new = []
            for i in text:
                if i == "минуту" or i == "секунду":
                    new.append(i[:-1])
                    continue
                new.append(i)
            
            


        elif "ты дура" in text:
            say("daring_answer")


        if "папку" in text:
            if "создай" in text:
                say("yes_master")
                create_folder(text)

            elif "удали" in text:
                say("yes_master")
                remove_folder(text)


        elif text == "инвокер мод":
            say("yes_master")
            invoker_mode(mic, r)

        
        

