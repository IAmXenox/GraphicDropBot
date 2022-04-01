from Checker import *
from src.Interface.InterfaceMenu import *


# Création du menu

menu = InterfaceMenu()


def debut():
    # Lancement du menu
    menu.window()
    # Instanciation de la classe Checker et lancement de la méthode Checking
    checker1 = Checker(menu.listOfCgActivated)
    checker1.Checking()


if __name__ == '__main__':
    debut()
