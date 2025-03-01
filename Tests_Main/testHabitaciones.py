import unittest
from Juego_Laberinto.Laberinto.juego import *
from  Juego_Laberinto.Factory_Method.creator import *

class TestHabitaciones(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.juego = Juego()
        self.fm = Creator()
        self.juego.crearLaberinto2HabitacionesFM(self.fm)

    def test_habitaciones(self):
        norte = self.fm.fabricarNorte()
        sur = self.fm.fabricarSur()
        este = self.fm.fabricarEste()
        oeste = self.fm.fabricarOeste()

        hab1 = self.juego.laberinto.obtener_habitacion(1)
        hab2 = self.juego.laberinto.obtener_habitacion(2)

        self.assertTrue(hab1.esHabitacion())
        self.assertTrue(hab2.esHabitacion())

        self.assertTrue(hab1.obtenerElementoOR(norte).esPared())
        self.assertTrue(hab1.obtenerElementoOR(este).esPared())
        self.assertTrue(hab1.obtenerElementoOR(oeste).esPared())

        self.assertTrue(hab2.obtenerElementoOR(sur).esPared())
        self.assertTrue(hab2.obtenerElementoOR(este).esPared())
        self.assertTrue(hab2.obtenerElementoOR(oeste).esPared())

        pt12 = hab1.obtenerElementoOR(sur)
        self.assertTrue(pt12.esPuerta())
        self.assertTrue(hab2.obtenerElementoOR(norte).esPuerta())
        self.assertFalse(pt12.abierta)

if __name__ == "__main__":
    unittest.main()