from unittest import TestCase

from juego import Director


class LaberintoBuilderTest(TestCase):
    def comprobarArmario(self, num, unCont):
        arm = next((each for each in unCont.hijos if each.esArmario()), None)
        self.assertIsNotNone(arm, "No se encontró un armario en el contenedor")
        self.assertTrue(arm.esArmario(), "El objeto encontrado no es un armario")
        return arm
    
    def comprobarBomba(self, unCont):
        bomba = next((each for each in unCont.hijos if each.esBomba()), None)
        self.assertIsNotNone(bomba, "No se encontró una bomba en el contenedor")
        self.assertTrue(bomba.esBomba(), "El objeto encontrado no es una bomba")

    def comprobarHabitacion(self, num):
        hab = self.juego.obtenerHabitacion(num)
        self.assertTrue(hab.num == num, "El número de la habitación no coincide")
        return hab
    
    def comprobarLaberintoRecursivo(self, unDic, padre):
        nada = True
        con = None

    # Contenedores
        if unDic.get('tipo') == 'habitacion':
            nada = False
            con = self.comprobarHabitacion(unDic.get('num'))
        if unDic.get('tipo') == 'armario':
            nada = False
            con = self.comprobarArmario(unDic.get('num'), padre)

    # Hojas
        if unDic.get('tipo') == 'bomba':
            nada = False
            self.comprobarBomba(padre)
        if unDic.get('tipo') == 'tunel':
            nada = False
            self.comprobarTunel(padre)

        lista = unDic.get('hijos', None)
        if lista is not None:
            for each in lista:
                self.comprobarLaberintoRecursivo(each, con)

        if nada:
            self.assertFalse(True, "No se reconoció el tipo de elemento en el diccionario")

    def comprobarPuerta(self, unNum, unaOr, otroNum, otraOr):
        
        unaHab = self.juego.obtenerHabitacion(unNum)
        otraHab = self.juego.obtenerHabitacion(otroNum)

        self.assertEqual(unaHab.num, unNum, "El número de la primera habitación no coincide")
        self.assertEqual(otraHab.num, otroNum, "El número de la segunda habitación no coincide")

        or1 = getattr(self.director.builder, f"fabricar{unaOr}")()
        or2 = getattr(self.director.builder, f"fabricar{otraOr}")()

        pt1 = unaHab.obtenerElementoOr(or1)
        pt2 = otraHab.obtenerElementoOr(or2)

        self.assertTrue(pt1.esPuerta(), "El elemento en la primera orientación no es una puerta")
        self.assertTrue(pt2.esPuerta(), "El elemento en la segunda orientación no es una puerta")

        self.assertEqual(pt1, pt2, "Las puertas no son iguales")
        self.assertFalse(pt1.estaAbierta(), "La puerta debería estar cerrada")


    def comprobarTunel(self, unCont):
    
        tunel = next((each for each in unCont.hijos if each.esTunel()), None)

        self.assertIsNotNone(tunel, "No se encontró un túnel en el contenedor")
        self.assertTrue(tunel.esTunel(), "El objeto encontrado no es un túnel")

    def setUp(self):
        super().setUp()
        self.director = Director()
        ruta = "C:\\Users\\Usuario\\Desktop\\3º\\lab2H1B.json"
        self.director.procesar(ruta)
        self.dict = self.director.dict
        self.juego = self.director.obtenerJuego()
        self.juego.agregarPersonaje('Joselu')

    def testBichoAtaca(self):
    
        hab1 = self.juego.obtenerHabitacion(1)
        bicho = self.juego.bichos[0]
        person = self.juego.person

        self.assertIsNotNone(bicho, "El bicho no debería ser None")
        self.assertIsNotNone(person, "El personaje no debería ser None")

        hab1.entrar(bicho)
        hab1.entrar(person)

        bicho.atacar()
        self.assertEqual(person.vidas, 0, "Las vidas del personaje deberían ser 0 después del ataque")

    def testIniciales(self):
    
        self.assertIsNotNone(self.juego, "El juego no debería ser None")
        self.assertIsNotNone(self.juego.laberinto, "El laberinto del juego no debería ser None")

    def testLaberinto(self):
    
        for each in self.dict.get('laberinto', []):
            self.comprobarLaberintoRecursivo(each, 'root')

        for cada in self.dict.get('puertas', []):
            self.comprobarPuerta(
               cada[0],  # Número de la primera habitación
              cada[1],  # Orientación de la primera habitación
              cada[2],  # Número de la segunda habitación
              cada[3]   # Orientación de la segunda habitación
            )

    def testPersonaje(self):
    
        self.assertIsNotNone(self.juego.person, "El personaje no debería ser None")

        hab = self.juego.obtenerHabitacion(1)

        self.assertEqual(self.juego.person.posicion, hab, "La posición del personaje no coincide con la habitación 1")

        self.assertEqual(self.juego.person.vidas, 5, "Las vidas del personaje deberían ser 5")

    def testPersonajeAtaca(self):
    
        hab1 = self.juego.obtenerHabitacion(1)
        bicho = self.juego.bichos[0]  # Asumiendo que los bichos están en una lista
        person = self.juego.person

        self.assertIsNotNone(bicho, "El bicho no debería ser None")
        self.assertIsNotNone(person, "El personaje no debería ser None")

        hab1.entrar(bicho)
        hab1.entrar(person)

        person.atacar()

        self.assertEqual(bicho.vidas, 4, "Las vidas del bicho deberían ser 4 después del ataque")