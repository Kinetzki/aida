from talk import say
import random

greetings = [
    'Command received',
    'Copy that sir',
    'Initialized',
    'Processing',
    'Roger that',
    'Registered'
]


def greeting():
    say(random.choice(greetings))
