def invoker_mode(mic, r):
    print("Вы вошли в инвокер мод")

    from invoker_skills_list import check_list

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

        text = text.lower()

        check_list(text)

        if text == "выйти из мода":
            print("Вы вышли из мода инвокер")
            break
