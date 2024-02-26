# Online Libraries in the Main app
import os
import sys
import speech_recognition as sr
from playsound import playsound
import random
import time

# Written Modules
from talk import say
import greet
import define
from answer_wiki import search_
import solve
import google_search
import check_time
import covid
import site_opener
import navigation

r = sr.Recognizer()
r.energy_threshold = 500

keywords_wiki = [
    'what',
    'who',
    'when',
    'why',
    'where',
    'how'
]


invalid_commands = [
    'Your command is not valid',
    'Command not recognized',
    'Unknown command'
]


def open_tutorial():
    os.system('start commands_.txt')


def respond(command):
    key = command.split(' ')[0]
    if key in keywords_wiki:
        say(search_(command))
    if key == 'switch' and command.split(' ')[1] == 'tab':
        say('Switching tab now')
        navigation.switch(command)
    if key == 'switch' and command.split(' ')[1] == 'window':
        say('Switching window now')
        navigation.switch(command)
    if key == 'type':
        navigation.type_(command.split('type ')[1])
    if "define" in command:
        say(define.define_(command))
    if command == 'time':
        x, day = check_time.time_check()
        say("Today is")
        say(day)
        say(x)
    if "search" in command:
        say(google_search.search_google(command))
    if 'open' in command:
        command = command.split('open ')[1]
        site_opener.open_site(command)
    if 'cases' in command:
        total_cases, total_deaths, total_recovered = covid.pandemic()
        say(f'Total Covid 19 cases, {total_cases}')
        say(f'Total deaths as of today: {total_deaths}')
        say(f'Total recoveries: {total_recovered}')
    elif "solve" in command:
        command = command.split('solve ')[1]
        if "derivative" in command:
            say(solve.derivative(command))
        elif "square root" in command:
            say(solve.square_root(command))
        elif "what is" in command:
            say(solve.math_(command))


def main():
    playsound('POPOUT_LONG.wav')
    with sr.Microphone() as voice:
        say('system initialized')
        while True:
            audio = r.listen(voice)
            try:
                voice_data = r.recognize_google(audio)
                if 'ada' in voice_data:
                    greet.greeting()
                    command0 = voice_data.split('ada ')[1]
                    command0 = command0.replace('ada ', '')
                    respond(command0)
                if 'aida' in voice_data:
                    greet.greeting()
                    command0 = voice_data.split('aida ')[1]
                    command0 = command0.replace('aida ', '')
                    respond(command0)
                if 'ada exit' in voice_data:
                    say('Shutting Down...')
                    sys.exit()
                if 'ada help' in voice_data:
                    say('Here is the list of available commands')
                    open_tutorial()
                else:
                    pass
            except sr.UnknownValueError:
                pass
            except IndexError:
                say(random.choice(invalid_commands))
            except sr.RequestError:
                say('No internet connection')
                say('Please connect to the internet')
                pass
            time.sleep(0.3)


if __name__ == '__main__':
    main()
