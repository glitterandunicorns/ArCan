from enum import Enum


class Lang(Enum):
    ENGLISH = 0
    SPANISH = 1
    FRENCH = 2
    ITALIAN = 3
    GERMAN = 4


#english by default
language = Lang.ENGLISH


def setLanguage(l):
    l = l.lower()

    if l == "english" or l == "eng":
        language = Lang.ENGLISH
    elif l == "spanish" or l == "español":
        language = Lang.SPANISH
    elif l == "frech" or "francaise":
        language = Lang.FRENCH
    elif l == "italian" or "italiano":
        language = Lang.ITALIAN
    elif l == "german":
        language = Lang.GERMAN



pressKey = {
    Lang.ENGLISH: r"Press Enter to continue",
    Lang.SPANISH: r"Pulsa la tecla Intro"}

inputOption = {
    Lang.ENGLISH: r"Input your option: ",
    Lang.SPANISH: r"Introduce una opción: "}

def getText(text):
    return text.__getitem__(language)