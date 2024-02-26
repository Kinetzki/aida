import wikipedia as wiki
import define

words = [
    'is',
    'what',
    'who',
    'when',
    'why',
    'where',
    'how',
    'the'
]


def search_(audio_string):
    try:
        str1 = audio_string.split(' ')
        text = ''
        for string in str1:
            if string in words:
                continue
            else:
                text += string
                text += ' '
        return wiki.summary(text, sentences=2)
    except wiki.exceptions.PageError:
        return define.define_('text')
