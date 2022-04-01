from enum import Enum


# Enum contenant les différents plateformes, actives ou non
class Plateformes(Enum):
    __ordering__ = ['Twitter', 'Discord', 'Desktop']
    Twitter = True
    Discord = True
    Desktop = False
