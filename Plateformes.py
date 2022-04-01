from enum import Enum


# Enum contenant les différents plateformes, actives ou non
class Plateformes(Enum):
    __ordering__ = ['Twitter', 'Discord', 'Messenger', 'Desktop']
    Twitter = False
    Discord = True
    Messenger = True
    Desktop = False
