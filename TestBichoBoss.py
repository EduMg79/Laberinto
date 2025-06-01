import unittest
import io
import sys
from juego import Director, Juego, Personaje

class BichoBossTest(unittest.TestCase):
    def setUp(self):
        # Prepara un laberinto con un Boss en la habitación 1
        self.director = Director()
        self.director.procesar("C:\\Users\\Usuario\\Desktop\\Git\\PruebaBoss.json")
        self.juego=self.director.obtenerJuego()
        self.juego.agregarPersonaje("Tester")
        self.personaje =self.juego.person
        self.personaje.vidas = 100
        self.personaje.poder = 100  
        self.juego.abrirPuertas()

    def test_ganar_al_matar_boss(self):
        # Busca el boss
        boss = next((b for b in self.juego.bichos if hasattr(b.modo, "esBoss") and b.modo.esBoss()), None)
        self.assertIsNotNone(boss)
        # Mueve al personaje a la habitación del boss
        self.personaje.posicion = boss.posicion
        captured_output = io.StringIO()
        sys.stdout = captured_output
        # Ataca al boss
        self.personaje.atacar()
        # Comprueba que el juego ha sido ganado
        sys.stdout = sys.__stdout__  # Restaura la salida estándar

        # Comprueba que el mensaje de victoria está en la salida
        self.assertIn("Fin del juego, Personaje Tester ha ganado", captured_output.getvalue())

if __name__ == "__main__":
    unittest.main()