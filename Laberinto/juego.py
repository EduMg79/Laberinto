from Factory_Method.creator import *
class ElementoMapa:
    def __init__(self,padre):
        self.padre = padre
        pass
    
    def entrar(self):
        pass

    def entrar(self,alguien):
        pass

    def esBomba(self):
        return False
    
    def esPared(self):
        return False
    
    def esPuerta(self):
        return False
    
    def esHabitacion(self):
        return False
    
    def esLaberinto(self):
        return False

class Orientacion:
    def __init__(self):
        pass

    def obtenerElementoOrEn(self, unContenedor):
        pass

    def ponerElemento(self, unEm, unContenedor):
        pass

class Norte(Orientacion):
    def ponerElemento(self, em, unContenedor):
        unContenedor.norte = em

    def obtenerElementoOREn(self, unContenedor):
        return unContenedor.norte

class Sur(Orientacion):
    def ponerElemento(self, em, unContenedor):
        unContenedor.sur = em

    def obtenerElementoOREn(self, unContenedor):
        return unContenedor.sur

class Este(Orientacion):
    def ponerElemento(self, em, unContenedor):
        unContenedor.este = em

    def obtenerElementoOREn(self, unContenedor):
        return unContenedor.este

class Oeste(Orientacion):
    def ponerElemento(self, em, unContenedor):
        unContenedor.oeste = em

    def obtenerElementoOREn(self, unContenedor):
        return unContenedor.oeste
    
class Hoja(ElementoMapa):
    def __init__(self):
        super().__init__()

class Decorator(Hoja):
    def __init__(self,em):
        super().__init__()
        self.em = em
        pass

class Bomba(Decorator):
    def __init__(self,em):
        super().__init__(em)
        self.activa = False
    
    def entrar(self):
        if self.activa:
            print("¡Te has chocado con una bomba!")
        else:
            self.em.entrar()

    def esBomba(self):
        return True

class Bicho:
    def __init__(self, modo, posicion):
        self.vidas = 5
        self.poder = 1
        self.modo = modo
        self.posicion = posicion
        

    def esAgresivo(self):
        return self.modo.esAgresivo()
    
    def esPerezoso(self):
        return self.modo.esPerezoso()
    
    def esBoss(self):
        return self.modo.esBoss()

    def iniAgresivo(self):
        self.modo = Agresivo()
        self.poder = 10
        self.vidas = 5

    def iniPerezoso(self):
        self.modo = Perezoso()
        self.poder = 1
        self.vidas = 5

    def iniBoss(self):
        self.modo = Boss()
        self.poder = 20
        self.vidas = 10

class Modo:
    def __init__(self):
        pass

    def actua(self, unBicho):
        self.camina(unBicho)

    def camina(self, unBicho):
        "self subclassResponsibility."
        "definir un caminar predeterminado"

    def esAgresivo(self):
        return False
    
    def esPerezoso(self):
        return False
    
    def esBoss(self):
        return False

class Agresivo(Modo):
    def __init__(self):
        super().__init__()

    def esAgresivo(self):
        return True

class Perezoso(Modo):
    def __init__(self):
        super().__init__()

    def esPerezoso(self):
        return True

class Boss(Modo):
    def __init__(self):
        super().__init__()

    def esBoss(self):
        return True

class Contenedor(ElementoMapa):
    def __init__(self):
        super().__init__()
        self.hijos = []
        self.orientaciones = []

    def agregarHijo(self, em):
        em.padre = self
        self.hijos.append(em)

    def eliminarHijo(self, em):
        self.hijos.remove(em)

    def agregarOrientacion(self, orientacion):
        self.orientaciones.append(orientacion)
        
    def obtenerElementoOR(self, orientacion):
        return orientacion.obtenerElementoOR(self)

    def ponerEnOr(self, orientacion, em):
        orientacion.ponerElemento(em, self)

class Pared(ElementoMapa):
    def __init__(self):
        super().__init__()

    def entrar(self):
        print("¡Te has chocado con una pared")

    def esPared(self):
        return True

class ParedBomba(Pared):
    def __init__(self):
        super().__init__()
        self.activa = False

    def entrar(self):
        print("Te has chocado con una Pared Bomba")
        
class Puerta(ElementoMapa):
    def __init__(self, lado1, lado2):
        super().__init__()
        self.abierta = False
        self.lado1 = lado1
        self.lado2 = lado2

    def entrar(self):
        if self.abierta:
            print("La puerta está abierta")
        else:
            print("La puerta está cerrada")

    def abrir(self):
        self.abierta = True

    def cerrar(self):
        self.abierta = False

    def esPuerta(self):
        return True

class Habitación(Contenedor):
    def __init__(self, num, norte, sur, este, oeste):
        super().__init__()
        self.num = num
        self.norte = norte
        self.sur = sur
        self.este = este
        self.oeste = oeste
        
    def entrar(self):
        print(f"Estás en una habitación{self.num}")

    def esHabitacion(self):
        return True

class Laberinto(Contenedor):
    def __init__(self):
        super().__init__()

    def agregar_habitacion(self, unaHabitacion):
        self.hijos.append(unaHabitacion)

    def eliminar_habitacion(self, unaHabitacion):
        self.hijos.remove(unaHabitacion)

    def obtener_habitacion(self, num):
        for hijo in self.hijos:
            if hijo.num == num:
                return hijo

        return None

    def entrar(self):
        print("Estás en un laberinto")

    def esLaberinto(self):
        return True
    

class Juego:
    def __init__(self):
        self.laberinto = Laberinto()
        self.bichos = []

    def agregar_bicho(self, bicho):
        self.bichos.append(bicho)

    def eliminar_bicho(self, bicho):
        self.bichos.remove(bicho) 

    """ def iniciar_juego(self):
        print("¡Bienvenido al juego del laberinto!")
        # Aquí puedes agregar la lógica para iniciar el juego """

    def crearLaberinto2Habitaciones(self):
        laberinto = Laberinto()
        hab1 = Habitación(1)
        hab1.este = Pared()
        hab1.oeste = Pared()
        hab1.norte = Pared()

        hab2 = Habitación(2)
        hab2.sur = Pared()
        hab2.este = Pared()
        hab2.oeste = Pared()

        puerta = Puerta(hab1, hab2)
        puerta.lado1 = hab1
        puerta.lado2 = hab2

        hab1.sur = puerta
        hab2.norte = puerta

        laberinto.agregar_habitacion(hab1)
        laberinto.agregar_habitacion(hab2)
        return laberinto

    def crearLaberinto2HabitacionesFM(self):
        unFM = Creator()
        laberinto = unFM.fabricarLaberinto()
        hab1 = unFM.fabricarHabitacion(1)
        hab2 = unFM.fabricarHabitacion(2)
        puerta = unFM.fabricarPuerta()
        hab1.lado1 = puerta
        hab2.lado2 = puerta
        hab1.sur = puerta
        hab2.norte = puerta

        laberinto.agregar_habitacion(hab1)
        laberinto.agregar_habitacion(hab2)
        return laberinto
    
    def crearLaberinto2HabitacionesFM(self, unFM):
        laberinto = unFM.fabricarLaberinto()
        hab1 = unFM.fabricarHabitacion(1)
        hab2 = unFM.fabricarHabitacion(2)
        puerta = unFM.fabricarPuerta()
        hab1.lado1 = puerta
        hab2.lado2 = puerta

        hab1.ponerEnOr(puerta, unFM.fabricarSur())
        hab2.ponerEnOr(puerta, unFM.fabricarNorte())

        laberinto.agregar_habitacion(hab1)
        laberinto.agregar_habitacion(hab2)
        return laberinto
        
    
    def crearLaberinto2HabitacionesFMD(self, creator):
        laberinto = creator.fabricarLaberinto()
        hab1 = creator.fabricarHabitacion(1)
        hab2 = creator.fabricarHabitacion(2)

        pared1 = creator.fabricarPared()
        bomba1 = creator.fabricarBomba(pared1)
        hab1.este = bomba1

        pared2 = creator.fabricarPared()
        bomba2 = creator.fabricarBomba(pared2)
        hab2.oeste = bomba2

        puerta = creator.fabricarPuerta()
        hab1.lado1 = puerta
        hab2.lado2 = puerta
        hab1.sur = puerta
        hab2.norte = puerta

        laberinto.agregar_habitacion(hab1)
        laberinto.agregar_habitacion(hab2)
        return laberinto

    def crearLaberinto4H4BFM(self, unFM):
        # Crear orientaciones
        norte = unFM.fabricarNorte()
        sur = unFM.fabricarSur()
        este = unFM.fabricarEste()
        oeste = unFM.fabricarOeste()

        # Crear habitaciones
        hab1 = unFM.fabricarHabitacion(1)
        hab2 = unFM.fabricarHabitacion(2)
        hab3 = unFM.fabricarHabitacion(3)
        hab4 = unFM.fabricarHabitacion(4)

        # Crear puertas y asignar lados
        puerta1 = unFM.fabricarPuerta()
        hab1.lado1 = puerta1
        hab2.lado2 = puerta1
        puerta2 = unFM.fabricarPuerta()
        hab1.lado1 = puerta2
        hab3.lado2 = puerta2
        puerta3 = unFM.fabricarPuerta()
        hab2.lado1 = puerta3
        hab4.lado2 = puerta3
        puerta4 = unFM.fabricarPuerta()
        hab3.lado1 = puerta4
        hab4.lado2 = puerta4

        # Colocar las puertas en las habitaciones
        hab1.ponerEnOr(sur, puerta1)
        hab2.ponerEnOr(norte, puerta1)
        hab1.ponerEnOr(este, puerta2)
        hab3.ponerEnOr(oeste, puerta2)
        hab2.ponerEnOr(este, puerta3)
        hab4.ponerEnOr(oeste, puerta3)
        hab3.ponerEnOr(sur, puerta4)
        hab4.ponerEnOr(norte, puerta4)

        # Crear laberinto y agregar habitaciones
        self.laberinto = unFM.fabricarLaberinto()
        self.laberinto.agregar_habitacion(hab1)
        self.laberinto.agregar_habitacion(hab2)
        self.laberinto.agregar_habitacion(hab3)
        self.laberinto.agregar_habitacion(hab4)

        # Crear y agregar bichos
        self.agregar_bicho(unFM.fabricarBichoAgresivo(hab1))
        self.agregar_bicho(unFM.fabricarBichoAgresivo(hab2))
        self.agregar_bicho(unFM.fabricarBichoPerezoso(hab3))
        self.agregar_bicho(unFM.fabricarBichoPerezoso(hab4))

        return self.laberinto
    
    def obtenerHabitacion(self, num):
        return self.laberinto.obtener_habitacion(num)
    
    def crearLaberinto1H1BB(self, creator):
        laberinto = creator.fabricarLaberinto()
        hab1 = creator.fabricarHabitacion(1)
        bichoBoss = creator.fabricarBoss()
        laberinto.agregar_habitacion(hab1)
        self.agregar_bicho(bichoBoss)
        bichoBoss.posicion = hab1
        return laberinto