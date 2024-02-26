import PyDictionary

dictionary = PyDictionary.PyDictionary()


def define_(string):
    string = string.replace('define ', '')
    return dictionary.meaning(string)
