import unittest
from juego import Inventario, Personaje, Arco, Espada, PocionVida, Armadura, PocionVenenosa

class InventarioTest(unittest.TestCase):
    def setUp(self):
        self.inventario = Inventario()
        self.personaje = Personaje("Tester")
        self.personaje.vidas = 100
        self.personaje.poder = 1

    def test_agregar_objetos(self):
        arco = Arco()
        self.inventario.agregar(arco)
        self.assertIn(arco, self.inventario.objetos)

    def test_usar_arco(self):
        self.inventario.agregar(Arco())
        self.inventario.usar(0, self.personaje)
        self.assertEqual(self.personaje.poder, 4)  # 1 + 3

    def test_usar_espada(self):
        self.inventario.agregar(Espada())
        self.inventario.usar(0, self.personaje)
        self.assertEqual(self.personaje.poder, 6)  # 1 + 5

    def test_usar_pocion_vida(self):
        self.inventario.agregar(PocionVida())
        self.inventario.usar(0, self.personaje)
        self.assertEqual(self.personaje.vidas, 110)  # 100 + 10

    def test_usar_armadura(self):
        self.inventario.agregar(Armadura())
        self.inventario.usar(0, self.personaje)
        self.assertEqual(self.personaje.vidas, 200)  # 100 * 2

    def test_usar_pocion_venenosa(self):
        self.inventario.agregar(PocionVenenosa())
        self.inventario.usar(0, self.personaje)
        self.assertEqual(self.personaje.vidas, 95)  # 100 - 5

    def test_usar_indice_invalido(self):
        self.inventario.usar(99, self.personaje)  # No debe lanzar excepción

if __name__ == "__main__":
    unittest.main()