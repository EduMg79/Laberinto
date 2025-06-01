import unittest
from juego import Cofre, Personaje, Arco, Espada, PocionVida, Armadura, PocionVenenosa

class CofreTest(unittest.TestCase):
    def setUp(self):
        self.cofre = Cofre()
        self.personaje = Personaje("Tester")
        self.personaje.vidas = 100
        self.personaje.poder = 1

    def test_mostrar_objetos(self):
        # Solo verifica que no lanza excepción y muestra los objetos
        self.cofre.mostrarObjetos()

    def test_elegir_objeto_valido(self):
        objetos_iniciales = len(self.cofre.objetos)
        self.cofre.elegirObjeto(0, self.personaje)
        self.assertEqual(len(self.cofre.objetos), objetos_iniciales - 1)
        self.assertEqual(len(self.personaje.inventario.objetos), 1)

    def test_elegir_objeto_invalido(self):
        # Índice fuera de rango
        self.cofre.elegirObjeto(99, self.personaje)  # No debe lanzar excepción

    def test_es_cofre(self):
        self.assertTrue(self.cofre.es_cofre())

    def test_es_tunel(self):
        self.assertFalse(self.cofre.esTunel())

    def test_objeto_usar(self):
       
        self.cofre.elegirObjeto(0, self.personaje)
        self.personaje.inventario.usar(0, self.personaje)
        

if __name__ == "__main__":
    unittest.main()