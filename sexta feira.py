import speech_recognition as sr
import pyttsx3
from random import randint

rec = sr.Recognizer()
with sr.Microphone() as fonte:
    print('diga algo:...')

    frase = rec.listen(fonte)

    texto = rec.recognize_google(frase, language='pt-BR')

    try:
        print('você disse: ' + texto)
        nome = 'sexta-feira'

        if texto == nome:

            en = pyttsx3.init()
            en.setProperty('voice', b'brazil')
            en.setProperty('rate', 180)
            apresentacao = ['olá', 'sim', 'pois não?']
            uso = randint(0, 2)
            en.say(apresentacao[uso])

            en.runAndWait()

    except:
        print('erro')
