import unittest
from juego import Personaje, Mago, Luchador

class TestTipoPersonaje(unittest.TestCase):
    def test_asignar_mago(self):
        tipo = Mago()
        personaje = Personaje("Merlin")
        personaje.tipo = tipo
        personaje.vidas = tipo.vidas
        personaje.poder = tipo.poder
        self.assertEqual(personaje.tipo.__class__.__name__, "Mago")
        self.assertEqual(personaje.vidas, 30)
        self.assertEqual(personaje.poder, 20)

    def test_asignar_luchador(self):
        tipo = Luchador()
        personaje = Personaje("Conan")
        personaje.tipo = tipo
        personaje.vidas = tipo.vidas
        personaje.poder = tipo.poder
        self.assertEqual(personaje.tipo.__class__.__name__, "Luchador")
        self.assertEqual(personaje.vidas, 50)
        self.assertEqual(personaje.poder, 10)

if __name__ == "__main__":
    unittest.main()