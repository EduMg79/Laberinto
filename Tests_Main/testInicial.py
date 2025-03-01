import unittest
from Juego_Laberinto.Laberinto.juego import *
from Juego_Laberinto.Factory_Method.creator import *    

class TestIniciales(unittest.TestCase):

    def setUp(self):
        super().setUp()  # Llamar al setUp de la superclase
        self.juego = Juego()
        self.fm = Creator()
        self.juego.crearLaberinto2HabitacionesFM(self.fm)

    def test_iniciales(self):
        self.assertIsNotNone(self.juego)
        self.assertIsNotNone(self.juego.laberinto)
        num_hab = len(self.juego.laberinto.hijos)  # Asumiendo que "hijos" es una lista en Python
        self.assertEqual(num_hab, 2)

if __name__ == "__main__":
    unittest.main()