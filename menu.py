import utilities


def load():
    print("MENU LOAD")

def learning():
    print("MENU LEARNING")

def test():
    print("MENU TEST")

def exit():
    print("MENU EXIT")
    exit()



functions = (
    ["1", "Cargar fichero|Load file", load],
    ["2", "Aprendizaje|Learning", learning],
    ["3", "Prueba|Test", test],

    ["0", "Salir|Exit", exit])


if __name__ == "__main__":
    function = utilities.menu("Main|Principal", functions)
    function()

