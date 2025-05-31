from unittest import TestCase
from juego import Juego
from juego import Creator

class LaberintoTest(TestCase):

    def setUp(self):
        super().setUp()
        self.juego = Juego()
        self.fm = Creator()
        self.juego.crearLaberinto2HabitacionesFM(self.fm)

    def testHabitaciones(self):
        norte = self.fm.fabricarNorte()
        sur = self.fm.fabricarSur()
        este = self.fm.fabricarEste()
        oeste = self.fm.fabricarOeste()
        hab1 = self.juego.obtenerHabitacion(1)
        hab2 = self.juego.obtenerHabitacion(2)
        self.assertTrue(hab1.esHabitacion())
        self.assertTrue(hab2.esHabitacion())
        self.assertTrue(hab1.obtenerElementoOr(norte).esPared())
        self.assertTrue(hab1.obtenerElementoOr(sur).esPared())
        self.assertTrue(hab1.obtenerElementoOr(este).esPared())
        self.assertTrue(hab1.obtenerElementoOr(oeste).esPuerta())
        self.assertTrue(hab2.obtenerElementoOr(sur).esPared())
        self.assertTrue(hab2.obtenerElementoOr(este).esPuerta())
        self.assertTrue(hab2.obtenerElementoOr(oeste).esPared())
        pt12 = hab1.obtenerElementoOr(sur)
        self.assertTrue(pt12.esPuerta())
        self.assertTrue(hab2.obtenerElementoOr(norte).esPuerta())
        self.assertTrue( not (pt12.abierta()))

    def testIniciales(self):
        self.assertTrue((self.juego)!= None)
        self.assertTrue((self.juego.laberinto)!= None)
        numHab= len(self.juego.laberinto.hijos)
        self.assertTrue(numHab == 2)