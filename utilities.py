from os import system, name
import i18n

def clearScreen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def pressKey():
    """
    :return:
    """
    input(i18n.getText(i18n.pressKey))

def menu(menu, options):
    """
    Shows a menu in the screen
    :param menu:
    :param options:
    :return: 
        None if error 
        Otherwise it returns the Function selected
    """



    print(menu)
    print("=" * len(menu) + "\n")

    for option in options:
        print("{0}. {1}".format(option[0], option[1]))

    selection = input(i18n.getText(i18n.inputOption))
    for function in options:
        if function[0] == selection:
            return function[2]
    return None