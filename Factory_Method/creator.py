from Juego_Laberinto.Laberinto.juego import Habitación, Pared, Puerta, Laberinto, Bomba, Bicho, Agresivo, Perezoso, Boss, Norte, Sur, Este, Oeste

class Creator:
    def __init__(self):
        pass

    def fabricarPared(self):
        return Pared()

    def fabricarPuerta(self):
        return Puerta()

    def fabricarHabitacion(self, num):
        hab = Habitación(num)
        hab.agregarOrientacion(Norte())
        hab.agregarOrientacion(Sur())
        hab.agregarOrientacion(Este())
        hab.agregarOrientacion(Oeste())

        for orientacion in hab.orientaciones:
            hab.ponerEnOr(self.fabricarPared(), orientacion)
        """ hab.norte = self.fabricarPared()
        hab.sur = self.fabricarPared()
        hab.este = self.fabricarPared()
        hab.oeste = self.fabricarPared()"""
        return hab

    def fabricarLaberinto(self):
        return Laberinto()
    
    def fabricarBomba(self,em):
        return Bomba(em)
    
    def cambiarAModoAgresivo(self, bicho):
        bicho.modo = Agresivo()
        bicho.poder = 5

    def fabricarBichoAgresivo(self):
        bicho = Bicho(Agresivo())
        bicho.vidas = 5
        bicho.poder = 5
        return bicho
    
    def fabricarBichoAgresivo(self, unaHab):
        bicho = Bicho(Agresivo())
        bicho.vidas = 5
        bicho.poder = 5
        bicho.posicion = unaHab
        return bicho
    
    def fabricarBichoPerezoso(self):
        bicho = Bicho(Perezoso())
        bicho.vidas = 1
        bicho.poder = 1
        return bicho
    
    def fabricarBichoPerezoso(self, unaHab):
        bicho = Bicho(Perezoso())
        bicho.vidas = 1
        bicho.poder = 1
        bicho.posicion = unaHab
        return bicho
    
    def fabricarBoss(self):
        bicho = Bicho(Boss())
        bicho.vidas = 10
        bicho.poder = 20
        return bicho
    
    def fabricarBoss(self, unaHab):
        bicho = Bicho(Boss())
        bicho.vidas = 10
        bicho.poder = 20
        bicho.posicion = unaHab
        return bicho
    
    def fabricarNorte(self):
        return Norte()
    
    def fabricarSur(self):
        return Sur()
    
    def fabricarEste(self):
        return Este()
    
    def fabricarOeste(self):
        return Oeste()