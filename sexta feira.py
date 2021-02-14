import speech_recognition as sr
import pyttsx3
from random import randint
import os


def ouvir():
    while True:
        try:
            frase = rec.listen(fonte, timeout=2)
            texto = rec.recognize_google(frase, language='pt-BR')
            return str(texto)

        except:
            print('erro no reconhecimento')
            break


def comandos(texto1):

    if texto1 == 'Abra o Google':
        os.startfile('Chrome.exe')
        en.say('certo, iniciando o google')
        en.runAndWait()

    elif texto1 == 'Abra o YouTube':
        os.startfile('https://www.youtube.com/?gl=BR&tab=r1')
        en.say('certo, iniciando o YouTube')
        en.runAndWait()

    else:
        en.say('desculpe, não entendi')
        en.runAndWait()


rec = sr.Recognizer()
with sr.Microphone() as fonte:
    while True:
        print('Diga algo:...')  #tests

        try:
            frase = rec.listen(fonte, timeout=1)  # ouvir da fonte
            texto = rec.recognize_google(frase, language='pt-BR')

        except:
            continue

        print('você disse: ' + texto)  #tests
        nome = 'sexta-feira'

        if texto == nome:

            en = pyttsx3.init()
            en.setProperty('voice', b'brazil')  # idioma
            en.setProperty('rate', 180)  # velocidade de fala

            apresentacao = ['olá', 'sim', 'pois não?']
            uso = randint(0, 2)  # escolher uma apresentação
            en.say(apresentacao[uso])
            en.runAndWait()  # falar

            print('diga algo:...')
            texto1 = ouvir()
            
            print('você disse: ' + str(texto1))

            if str(texto1 != None):
                comandos(texto1)
            else:
                continue
                
        else:
            continue
