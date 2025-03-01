from Laberinto.juego import ParedBomba
from Factory_Method.creator import Creator
class CreatorB(Creator):
    def fabricarPared(self):
        return ParedBomba()