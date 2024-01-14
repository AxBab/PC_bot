import speech_recognition as sr

from os import system, chdir
from webbrowser import open

from bot_prhases import make_prhase, say
from invoker_mode import invoker_mode
from clock import timer
from action_with_folders import create_folder, remove_folder
from settings import bot_name, user_name


make_prhase(f"Хорошо {user_name}", "yes_master")
make_prhase("Эй ты че совсем офигел кожаный мешок? Сам ты дурак тупой, хахахахахахахахахахахаха", "daring_answer")
make_prhase(f"До встречи {user_name}", "goodbye")

r = sr.Recognizer()
mic = sr.Microphone()
sr.LANGUAGE = 'ru-RU'


while True:
    with mic as source:
        print("Скажите что-нибудь...")

        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language='ru-RU')
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

        
        

