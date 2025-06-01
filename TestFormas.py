import unittest
from juego import Director

class FormasLaberintoTest(unittest.TestCase):
    def setUp(self):
        # Estructura mínima para cada forma
        self.base_dict = {
            "laberinto": [
                {"tipo": "habitacion", "num": 1, "hijos": []}
            ],
            "bichos": []
        }

    def test_cuadrado(self):
        director = Director()
        director.dict = dict(self.base_dict)
        director.dict["forma"] = "cuadrado"
        director.iniBuilder()
        self.assertEqual(director.builder.__class__.__name__, "LaberintoBuilder")
        director.fabricarLaberinto()
        director.fabricarJuego()
        self.assertIsNotNone(director.builder.juego.laberinto)

    def test_rombo(self):
        director = Director()
        director.dict = dict(self.base_dict)
        director.dict["forma"] = "rombo"
        director.iniBuilder()
        self.assertEqual(director.builder.__class__.__name__, "LaberintoBuilderRombo")
        director.fabricarLaberinto()
        director.fabricarJuego()
        self.assertIsNotNone(director.builder.juego.laberinto)

    def test_hexagono(self):
        director = Director()
        director.dict = dict(self.base_dict)
        director.dict["forma"] = "hexagono"
        director.iniBuilder()
        self.assertEqual(director.builder.__class__.__name__, "LaberintoBuilderHexagono")
        director.fabricarLaberinto()
        director.fabricarJuego()
        self.assertIsNotNone(director.builder.juego.laberinto)

    def test_triangulo(self):
        director = Director()
        director.dict = dict(self.base_dict)
        director.dict["forma"] = "triangulo"
        director.iniBuilder()
        self.assertEqual(director.builder.__class__.__name__, "LaberintoBuilderTriangulo")
        director.fabricarLaberinto()
        director.fabricarJuego()
        self.assertIsNotNone(director.builder.juego.laberinto)

if __name__ == "__main__":
    unittest.main()