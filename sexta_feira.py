import speech_recognition as sr
import pyttsx3
from random import randint
import os
import requests


def ouvir():
    while True:
        try:
            frase = rec.listen(fonte, timeout=3)
            texto = rec.recognize_google(frase, language='pt-BR')
            return str(texto)

        except:
            print('erro no reconhecimento')
            break


def comandos(texto1):
    google = ['Abra o Google', 'Abra o navegador', 'Inicie o navegador', 'Inicie o Google']
    if texto1 in google:
        os.startfile('Chrome.exe')
        en.say('certo, iniciando o google')
        en.runAndWait()

    elif texto1 == 'Abra o YouTube':
        os.startfile('https://www.youtube.com/?gl=BR&tab=r1')
        en.say('certo, iniciando o YouTube')
        en.runAndWait()

    elif texto1 == 'consultar filme':
        en.say('certo diga-me o nome do filme')
        print('certo diga-me o nome do filme...')
        en.runAndWait()  # falar

        filme = ouvir()
        print(filme)
        try:
            request = requests.get(f"http://www.omdbapi.com/?t={filme}&apikey=6620801a")

            print('Title: {}\nano: {} \ngenero: {} \ntempo de filme: {} \nPoster: {}'
                  .format(request.json()['Title'],request.json()['Year'],request.json()['Genre'],
                  request.json()['Runtime'],request.json()['Poster']))

            en.say('o filme {} foi lançado em {}'.format(request.json()['Title'], request.json()['Year']))
            en.runAndWait()  # falar

        except:
            en.say('titulo não encontrado')
            en.runAndWait()  # falar

            print('titulo não encontrado')


rec = sr.Recognizer()
with sr.Microphone() as fonte:
    while True:
        print('Diga algo1:...')  # tests

        try:
            frase = rec.listen(fonte, timeout=1)  # ouvir da fonte
            texto = rec.recognize_google(frase, language='pt-BR')

        except:
            continue

        print('você disse: ' + texto)  # tests
        nome = 'sexta-feira'

        if texto == nome:

            en = pyttsx3.init()
            en.setProperty('voice', b'brazil')  # idioma
            en.setProperty('rate', 170)  # velocidade de fala

            apresentacao = ['olá', 'sim', 'pois não?']
            uso = randint(0, 2)  # escolher uma apresentação
            en.say(apresentacao[uso])
            en.runAndWait()  # falar

            print('diga algo:...')
            texto1 = ouvir()

            print('você disse: ' + str(texto1))

            if str(texto1 is not None):
                comandos(texto1)
            else:
                continue

        else:
            continue
