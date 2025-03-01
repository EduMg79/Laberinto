from Juego_Laberinto.Laberinto.juego import ParedBomba
from Juego_Laberinto.Factory_Method.creator import Creator
class CreatorB(Creator):
    def fabricarPared(self):
        return ParedBomba()