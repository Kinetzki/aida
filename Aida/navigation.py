import keyboard as kb


def switch(command):
    if 'tab' in command:
        kb.press_and_release('ctrl + tab')
    if 'window' in command:
        kb.press_and_release('alt + tab')


def type_(command):
    kb.write(command)
