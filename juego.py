import random
import json


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y



class Comando:
    def __init__(self):
        self.receptor = None

class Abrir(Comando):
    
    def __init__(self):
        super.__init__()

    def ejecutar(self, alguien):
        self.receptor.abrir()


class Entrar(Comando):

    def ejecutar(self,alguien):
        self.receptor.entrar(alguien)

class ElementoMapa:
    def __init__(self):
        self.comandos = []

    def entrar(self):
        pass

    def entrar(self, alguien):
        pass

    def esArmario(self):
        pass

    def esBomba(self):
        pass

    def esHabitacion(self):
        pass

    def esLaberinto(self):
        pass

    def esPared(self):
        pass

    def esPuerta(self):
        pass

    def recorrer(self, unBloque):
        unBloque(self)

    def __str__(self):
        return "ElementoMapa"
    
    def aceptar(self, unVisitor):
        pass

    def agregarComando(self, unComando):
        self.comandos.append(unComando)

    def calcularPosicionDesdeEn(self, unaForma, unPunto):
        pass
    
    def eliminarComando(self, unComando):
        try:
            self.comandos.remove(unComando)
        except ValueError:
            print("No existe ese comando")

    def obtenerComandos(self):
        return self.comandos
    

class Contenedor(ElementoMapa):
    def __init__(self):
        super().__init__()
        self.hijos = []


    def getextent(self):
        return self.forma.extent
    
    def setextent(self, unPunto):
        self.forma.extent = unPunto

    def getpunto(self):
        return self.forma.punto
    
    def setpunto(self, unPunto):
        self.forma.punto = unPunto

    def agregarHijo(self, unEM):
        unEM.padre = self
        self.hijos.append(unEM)

    def agregarOrientacion(self, unaOr):
        self.forma.agregarOrientacion(unaOr)

    def eliminarHijo(self, unEM):
        try:
            self.hijos.remove(unEM)

        except ValueError:
            print(f"No existe ese objeto hijo")

    def entrar(self,alguien):
        alguien.posicion = self
        print(f"{alguien} ha entrado en {self}")
        alguien.buscarTunel()
    
    def irAlEste(self,alguien):
        self.forma.irAlEste(alguien)

    def irAlOeste(self,alguien):
        self.forma.irAlOeste(alguien)

    def irAlNorte(self,alguien):
        self.forma.irAlNorte(alguien)

    def irAlSur(self,alguien):
        self.forma.irAlSur(alguien)

    def irAlNoroeste(self, alguien):
        self.forma.irAlNoroeste(alguien)

    def irAlNoreste(self, alguien):
        self.forma.irAlNoreste(alguien)

    def irAlSuroeste(self, alguien):
        self.forma.irAlSuroeste(alguien)

    def irAlSureste(self, alguien):
        self.forma.irAlSureste(alguien)

    def obtenerElementoOr(self,unaOr):
        return self.forma.obtenerElementoOr(unaOr)
    
    def obtenerOrientacion(self):
        return self.forma.obtenerOrientacion()
    
    def obtenerOrientaciones(self):
        return self.forma.obtenerOrientaciones()

    def ponerEnOr(self, unaOr, unEM):
        self.forma.ponerEnOr(unaOr, unEM)

    def recorrer(self, unBloque):
        unBloque(self)

        for each in self.hijos:
            each.recorrer(unBloque)

        for each in self.obtenerOrientaciones():
            each.recorrer(unBloque, self.forma)

    def __str__(self):
        return "Contenedor"
    
    def aceptar(self, unVisitor):
        self.visitarContenedor(unVisitor)
        for each in self.hijos:
            each.aceptar(unVisitor)

    def calcularPosicion(self):
        self.forma.calcularPosicion()

    def visitarContenedor(self, unVisitor):
        pass

class Armario(Contenedor):

    def __init__(self):
        super().__init__()

    def esArmario(self):
        return True

class Habitacion(Contenedor):

    def __init__(self):
        super().__init__()
        self.num = None
        
    
    def esHabitacion(self):
        return True

    def __str__(self):
        return f"Habitacion {self.num}"
    
    def visitarContenedor(self, unVisitor):
        unVisitor.visitarContenedor(self)
        print("--------------------")   
  

class Laberinto(Contenedor):
    def __init__(self):
        super().__init__()

    def abrirPuertas(self):
        self.recorrer(lambda each: each.abrir() if each.esPuerta() and not each.estaAbierta() else None)
        print("Todas las puertas han sido abiertas")

    def aceptar(self, unVisitor):
        for each in self.hijos:
            each.aceptar(unVisitor)

    def cerrarPuertas(self):
        self.recorrer(lambda each: each.cerrar() if each.esPuerta() and each.estaAbierta() else None)

    def entrar(self,alguien):
        hab1 = self.obtenerHabitacion(1)
        hab1.entrar(alguien)
        return "Entraste en un  laberinto"
    
    def esLaberinto(self):
        return True
    
    def agregarHabitacion(self, unaHabitacion):
        self.hijos.append(unaHabitacion)

    def eliminarHabitacion(self, unaHabitacion):
        try:
            self.hijos.remove(unaHabitacion)

        except ValueError:
            print(f"No existen las  habitaciones")

    def obtenerHabitacion(self, unNum):
        for habitacion in self.hijos:
            if habitacion.num == unNum:
                return habitacion
        return None
    
    def recorrer(self, unBloque):
        unBloque(self)
        for hijo in self.hijos:
            hijo.recorrer(unBloque)

    def printOn(self, aStream):
        print(f"{aStream} Laberinto")

    def __str__(self):
        return "Laberinto"

class Cofre(Contenedor):
    def __init__(self):
        super().__init__()
        self.objetos = [  Arco(),
            Espada(),
            PocionVida(),
            Armadura(),
            PocionVenenosa()]


    def mostrarObjetos(self):
        print("Objetos en el cofre:")
        for i, obj in enumerate(self.objetos, 1):
            print(f"{i}. {obj}")

    def elegirObjeto(self, indice, personaje):
        if 0 <= indice < len(self.objetos):
            objeto = self.objetos.pop(indice)
            print(f"{personaje.nombre} ha cogido {objeto} del cofre.")
            personaje.inventario.agregar(objeto)
        else:
            print("Índice de objeto inválido.")

    def es_cofre(self):
        return True
    
    def esTunel(self):
        return False
    
    def recorrer(self, unBloque):
        unBloque(self)
    
    def __str__(self):
     return "Cofre"
    


class Hoja(ElementoMapa):
    def __init__(self):
        super().__init__()
    



class Decorator(Hoja):
        
        def __init__(self):
            super().__init__()
            self.em = None

        def __str__(self):
            return f"Decorator"
        
  


class Bomba(Decorator):

    def entrar(self,alguien):
        if self.activa:
            print(f"{alguien} ha pisao una bomba")
        else:
            self.em.entrar(alguien)

    def esBomba(self):
        return True
    
    def esTunel(self):
        return False

    def __init__(self):
        super().__init__()
        self.activa = False

    def __str__(self):
        return f"Bomba {self.activa}"
    
    def aceptar(self, unVisitor):
        unVisitor.visitarBomba(self)

    def activar(self):
        self.activa = True
        print("Bomba activada")


class Tunel(Hoja):

    def esTunel(self):
        return True
    
    def aceptar(self, unVisitor):
        unVisitor.visitarTunel(self)

    def crearNuevoLaberinto(self, alguien):
        self.laberinto = alguien.juegoClonaLaberinto()
        print(f"{alguien} crea un nuevo laberinto")



class Pared(ElementoMapa):
    
    def entrar(self,alguien):
         print(f"{alguien} se ha chocado con una pared")

    def esPared(self):
        return True

    def __str__(self):
        return "Pared"


class ParedBomba(Pared):

    def __init__(self):
        super().__init__()
        self.activa = False

    def __str__(self):
        return "Soy una pared bomba"


class Puerta(ElementoMapa):

    def abrir(self):
        self.estado.abrir(self)
        print(f"{self} ha sido abierta.")

    def cerrar(self):
        self.estado.cerrar(self)
        print(f"{self} ha sido cerrada.")

    def entrar(self, alguien):
        self.estado.entrar(alguien,self)

    def esPuerta(self):
        return True

    def __init__(self):
        super().__init__()
        self.estado = Cerrada()
        self.visitada = False

    def estaAbierta(self):
        return self.estado.estaAbierta()
    
    def calcularPosicionDesde(self, unCont, unPunto):
        if getattr(self, 'visitada', False):
            return self
        self.visitada = True

        if unCont.num == self.lado1.num:
            self.lado2.punto = unPunto
            self.lado2.calcularPosicion()
        else:
            self.lado1.punto = unPunto
            self.lado1.calcularPosicion()

    def puedeEntrar(self, alguien):
        if alguien.posicion == self.lado1:
            self.lado2.entrar(alguien)
        else:
            self.lado1.entrar(alguien)
    
    def __str__(self):
        return f"Puerta - {self.lado1.num} - {self.lado2.num} - {self.estado}"

class Ente:
    def __init__(self):
        self.vidas = None
        self.poder = None
        self.estadoEnte = Vivo()

    def esAtacadoPor(self,alguien):
        print(f"{self} es atacado por {alguien}")
        self.vidas -= alguien.poder
        print(f"Vidas: {self.vidas}")
        if self.vidas <= 0:
            self.heMuerto()

    def estaVivo(self):
        return self.vidas > 0
    
    def heMuerto(self):
        self.estadoEnte = Muerto()
        # Si es boss, avisar con self
        if  self.modo.esBoss():
            self.modo.avisar(self)
        else:
            self.avisar()

    def __str__(self):
        return "Ente"
    
    def atacar(self):
        self.estadoEnte.atacar(self)

    def avisar(self):
        pass

    def buscarTunel(self):
        pass

    def crearNuevoLaberinto(self):
        pass

    def juegoClonaLaberinto(self):
        return self.juego.clonarLaberinto()
    
    def puedeAtacar(self):
        pass

class Arma:
 def usar(self, personaje):
  raise NotImplementedError("Este método debe ser implementado por las subclases")
 

class Arco(Arma):
    def usar(self, personaje):
        personaje.poder += 3
        print(f"{personaje.nombre} ha equipado un arco. Poder aumentado a {personaje.poder}")

    def __str__(self):
        return "Arco"

class Espada(Arma):
    def usar(self, personaje):
        personaje.poder += 5
        print(f"{personaje.nombre} ha equipado una espada. Poder aumentado a {personaje.poder}")

    def __str__(self):
        return "Espada"

class PocionVida(Arma):
    def usar(self, personaje):
        personaje.vidas += 10
        print(f"{personaje.nombre} ha usado una poción de vida. Vidas aumentadas a {personaje.vidas}")

    def __str__(self):
        return "Poción de Vida"
    
class Armadura(Arma):
    def usar(self, personaje):
        personaje.vidas*=2
        print(f"{personaje.nombre} ha equipado una armadura. Vidas aumentadas a {personaje.vidas}")

    def __str__(self):
        return "Armadura"
    
class PocionVenenosa(Arma):
    def usar(self, personaje):
        personaje.poder -= 5
        personaje.vidas -= 5
        print(f"{personaje.nombre} ha usado una poción venenosa. Vidas reducidas a {personaje.vidas}")

    def __str__(self):
        return "Poción de Vida"



class Bicho(Ente):
    def __init__(self):
        self.modo = None
        self.poder = None
        self.vidas = None
        self.posicion = None

    def actua(self):
        while self.estaVivo():
            self.modo.actuar(self)

    def ini_agresivo(self):
        self.modo = Agresivo()
        self.poder = 10
        self.vidas = 5

    def ini_perezoso(self):
        self.poder = 1
        self.vidas = 5

    def atacar(self):
        self.juego.buscarPersonaje(self)
    def caminar(self):
        self.posicion.caminarAleatorio(self)
    
    def avisar(self):
        self.juego.terminarBicho(self)

    def buscarTunel(self):
        self.modo.buscarTunelBicho(self)
        
    def puedeActuar(self):
        self.modo.actua(self)

    def puedeAtacar(self):
        self.juego.buscarPersonaje(self)

    def heMuerto(self):
        self.estadoEnte = Muerto()
        if hasattr(self.modo, "esBoss") and self.modo.esBoss():
            self.modo.avisar(self)
        else:
            self.avisar()

    def __str__(self):
        return "Soy un bicho"+self.modo.__str__()

class EstadoEnte:
    def __init__(self):
        pass

    def vivir(self, ente):
        pass

    def morir(self, ente):
        pass


class Vivo(EstadoEnte):
    def __init__(self):
        super().__init__()

    def actua(self, unBicho):
     unBicho.puedeActuar()

    def atacar(self, alguien):
        alguien.puedeAtacar()

   


class Muerto(EstadoEnte):
    def __init__(self):
        super().__init__()

    def vivir(self, ente):
        print("El ente vive")
        ente.estadoEnte = Vivo()

    def morir(self, ente):
        print("El ente ya está muerto")
        ente.juego.terminarJuego()

class EstadoPuerta:
    def __init__(self):
        pass

    def abrir(self, puerta):
        pass

    def cerrar(self, puerta):
        pass

    def entrar(self, puerta, alguien):
        pass


class Abierta(EstadoPuerta):

    def abrir(self, unaPuerta):
        "ya abierta"

    def cerrar(self, unaPuerta):
        unaPuerta.estado = Cerrada()
        print(f"{unaPuerta} se ha cerrado")

    def entrar(self, alguien, unaPuerta):
        unaPuerta.puedeEntrar(alguien)


    def estaAbierta(self):
        return True
    
    def __str__(self):
        return "Abierta"

class Cerrada(EstadoPuerta):
     def abrir(self, unaPuerta):
       
        unaPuerta.estado = Abierta()
        print(f"{unaPuerta} se ha abierto")

     def cerrar(self, unaPuerta):
        "ya cerrada"

     def estaAbierta(self):
        return False

     def entrar(self, alguien, unaPuerta):
        print(f"{alguien} ha chocado con una puerta")

     def __str__(self):
        return "Cerrada"


class Forma:
    def __init__(self):
        self.orientaciones = []

    def agregarOrientacion(self, unaOr):
        self.orientaciones.append(unaOr)

    def __init__(self):
        self.orientaciones = []

    def irAlEste(self, alguien):
        pass

    def irAlOeste(self, alguien):
        pass

    def irAlNorte(self, alguien):
        pass

    def irAlSur(self, alguien):
        pass

    def obtenerElementoOr(self, unaOr):
        return unaOr.obtenerElementoOrEn(self)
    
    def obtenerOrientacion(self):
        ind = random.randint(0, len(self.orientaciones)-1)
        return self.orientaciones[ind]
    
    def obtenerOrientaciones(self):
        return self.orientaciones
    
    def ponerEnOr(self, unaOr, unEM):
        unaOr.ponerElemento(unEM, self)
    
    def __str__(self):
        return "Forma"
    
    def calcularPosicion(self):
        for orientation in self.obtenerOrientaciones():
            orientation.calcularPosicionDesde(self)



class Cuadrado(Forma):
    def __init__(self):
        super().__init__()
        self.norte = None 
        self.este = None
        self.sur = None
        self.oeste = None

    def irAlEste(self, unEnte):
        self.este.entrar(unEnte)

    def irAlNorte(self, unEnte):
        self.norte.entrar(unEnte)

    def irAlOeste(self, unEnte):
        self.oeste.entrar(unEnte)

    def irAlSur(self, unEnte):
        self.sur.entrar(unEnte)

    def __str__(self):
        return f"Cuadrado"
    
class Rombo(Forma):
    def __init__(self):
        super().__init__()
        self.noreste = None
        self.noroeste = None
        self.sureste = None
        self.suroeste = None

    def irAlNoreste(self, unEnte):
        self.noreste.entrar(unEnte)

    def irAlNoroeste(self, unEnte):
        self.noroeste.entrar(unEnte)
        
    def irAlSureste(self, unEnte):
        self.sureste.entrar(unEnte)

    def irAlSur(self, unEnte):
        self.sur.entrar(unEnte)

    def irAlSuroeste(self, unEnte):
        self.suroeste.entrar(unEnte)

    def __str__(self):
        return "Rombo"  


class Hexagono(Forma):
    def __init__(self):
        super().__init__()
        self.norte = None
        self.noreste = None
        self.sureste = None
        self.sur = None
        self.suroeste = None
        self.noroeste = None

    def irAlNorte(self, unEnte):
        self.norte.entrar(unEnte)

    def irAlNoreste(self, unEnte):
        self.noreste.entrar(unEnte)

    def irAlSureste(self, unEnte):
        self.sureste.entrar(unEnte)

    def irAlSur(self, unEnte):
        self.sur.entrar(unEnte)

    def irAlSuroeste(self, unEnte):
        self.suroeste.entrar(unEnte)

    def irAlNoroeste(self, unEnte):
        self.noroeste.entrar(unEnte)

    def __str__(self):
        return "Hexágono"
    
class Triangulo(Forma):
    def __init__(self):
        super().__init__()
        self.norte = None
        self.sureste = None
        self.suroeste = None

    def irAlNorte(self, unEnte):
        self.norte.entrar(unEnte)

    def irAlSureste(self, unEnte):
        self.sureste.entrar(unEnte)

    def irAlSuroeste(self, unEnte):
        self.suroeste.entrar(unEnte)

    def __str__(self):
        return "Triángulo"








class Modo:
    def __init__(self):
        pass

    def actuar(self, bicho):
        self.dormir(bicho)
        self.caminar(bicho)
        self.atacar(bicho)

    def dormir(self, bicho):
        pass

    def caminar(self, bicho):
        bicho.caminar()

    def atacar(self, bicho):
        bicho.atacar()

    def esBoss(self):
        return False

    def __str__(self):
        return "Soy un modo"

import time
class Agresivo(Modo):
       
    def buscarTunelBicho(self, unBicho):
        pos = unBicho.posicion
        tunel = next((each for each in pos.hijos if each.esTunel()), None)
        if tunel is not None:
            tunel.entrar(unBicho)

    def dormir(self, unBicho):
        print(f"{unBicho} duerme")
        time.sleep(1)

    def __init__(self):
        super().__init__()

    def esAgresivo(self):
        return True
    
    def __str__(self):
        return "Agresivo"

 

class Perezoso(Modo):

    def buscarTunelBicho(self, unBicho):
        pos = unBicho.posicion
        tunel = next((each for each in pos.hijos if each.esTunel()), None)
        if tunel is not None:
            tunel.entrar(unBicho)

    def dormir(self, unBicho):
        print(f"{unBicho} duerme")
        time.sleep(3)

    def __init__(self):
        super().__init__()

    def esPerezoso(self):
        return True
    
    def __str__(self):
        return "Perezoso"
    
class BichoBoss(Modo):
    def __init__(self):
        super().__init__()
        self.modo = Agresivo()  # O el modo que prefieras
        self.vidas = 200
        self.poder = 10

    def buscarTunelBicho(self, unBicho):
        pos = unBicho.posicion
        tunel = next((each for each in pos.hijos if each.esTunel()), None)
        if tunel is not None:
            tunel.entrar(unBicho)

    def esBoss(self):
        return True
    
    def avisar(self,bicho):
        # Cuando el boss muere, el personaje gana la partida
        print("¡Has derrotado al BOSS!")
        if hasattr(bicho, 'juego'):
            bicho.juego.ganaPersonaje()

    def __str__(self):
        return "Boss"
    


class Inventario:
    def __init__(self):
        self.objetos = []

    def agregar(self, objeto):
        self.objetos.append(objeto)
        print(f"Objeto {objeto} añadido al inventario.")

    def mostrar(self):
        print("Inventario:")
        for i, obj in enumerate(self.objetos, 1):
            print(f"{i}. {obj}")

    def usar(self, indice, personaje):
        if 0 <= indice < len(self.objetos):
            objeto = self.objetos.pop(indice)
            print(f"Usando {objeto}...")
            objeto.usar(personaje)
        else:
            print("Índice de objeto inválido.")

class Juego:

    def abrirPuertas(self):
        self.laberinto.abrirPuertas()

    def agregarBicho(self, unBicho):
        self.bichos.append(unBicho)
        unBicho.juego = self

    def agregarPersonaje(self, unaCadena,tipo=None):
        self.person= Personaje(unaCadena)
        self.person.juego = self
        self.laberinto.entrar(self.person)
   

    def buscarBicho(self):
        posPerson = self.person.posicion
        bicho = next((b for b in self.bichos if b.estaVivo() and b.posicion == posPerson), None)
        if bicho != None:
            bicho.esAtacadoPor(self.person)
            print(f"{self.person} ataca a {bicho} en la habitacion {posPerson.num}")
        else:
            print(f"{self.person} no hay bichos en la habitacion {posPerson.num}")

    def buscarPersonaje(self, unBicho):
        posBicho = unBicho.posicion
        posPersonaje = self.person.posicion
        if posBicho == posPersonaje:
            self.person.esAtacadoPor(unBicho)
                    
    def cerrarPuertas(self):
        self.laberinto.cerrarPuertas()
        import copy

    def clonarLaberinto(self):
        import copy
        return copy.deepcopy(self.prototipo)

    def crearLaberinto2Habitaciones(self):

        hab1 = Habitacion()
        hab1.num = 1
        hab1.este = Pared()
        hab1.norte = Pared()
        hab1.oeste = Pared()

        hab2 = Habitacion()
        hab2.num = 2
        hab2.sur = Pared()
        hab2.este = Pared()
        hab2.oeste = Pared()

        puerta = Puerta()
        puerta.lado1 = hab1
        puerta.lado2 = hab2

        hab1.sur = puerta
        hab2.norte = puerta

        laberinto = Laberinto()
        laberinto.agregarHabitacion(hab1)
        laberinto.agregarHabitacion(hab2)
        return laberinto

    def crearLaberinto2HabitacionesFM(self):

        unFM = Creator()

        hab1 = unFM.fabricarHabitacion(1)
        hab2 = unFM.fabricarHabitacion(2)

        puerta = unFM.fabricarPuerta()
        puerta.lado1 = hab1
        puerta.lado2 = hab2

        hab1.sur = puerta
        hab2.norte = puerta

        self.laberinto = unFM.fabricarLaberinto()
        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)

        return self.laberinto
    
    def crearLaberinto2HabitacionesFM(self, unFM):

        hab1 = unFM.fabricarHabitacion(1)
        hab2 = unFM.fabricarHabitacion(2)

        puerta = unFM.fabricarPuerta()

        puerta.lado1 = hab1
        puerta.lado2 = hab2

        hab1.ponerEnOr(unFM.fabricarSur(), puerta)
        hab2.ponerEnOr(unFM.fabricarNorte(), puerta)    

        self.laberinto = unFM.fabricarLaberinto()
        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)

        return self.laberinto
    
    def crearLaberinto2HabitacionesFMD(self, unFM):
        
        hab1 = unFM.fabricarHabitacion(1)
        hab2 = unFM.fabricarHabitacion(2)

        bomba1 = unFM.fabricarBomba()
        bomba1.em = unFM.fabricarPared()
        hab1.este=bomba1

        bomba2 = unFM.fabricarBomba()
        bomba2.em = unFM.fabricarPared()
        hab2.este=bomba2

        puerta = unFM.fabricarPuerta()
        puerta.lado1 = hab1
        puerta.lado2 = hab2

        hab1.sur = puerta
        hab2.norte = puerta

        self.laberinto = unFM.fabricarLaberinto()
        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)

        return self.laberinto
    
    def crearLaberinto4H4BFM(self,unFM):

        norte = unFM.fabricarNorte()
        sur = unFM.fabricarSur()
        este = unFM.fabricarEste()
        oeste = unFM.fabricarOeste()


        hab1 = unFM.fabricarHabitacion(1)
        hab2 = unFM.fabricarHabitacion(2)
        hab3 = unFM.fabricarHabitacion(3)
        hab4 = unFM.fabricarHabitacion(4)

        puerta1 = unFM.fabricarPuerta()
        puerta2 = unFM.fabricarPuerta()
        puerta3 = unFM.fabricarPuerta()
        puerta4 = unFM.fabricarPuerta()

        puerta1.lado1 = hab1
        puerta1.lado2 = hab2
        puerta2.lado1 = hab1
        puerta2.lado2 = hab3
        puerta3.lado1 = hab2
        puerta3.lado2 = hab4
        puerta4.lado1 = hab3
        puerta4.lado2 = hab4

        hab1.ponerEnOr(sur, puerta1)
        hab2.ponerEnOr(norte, puerta1)
        hab1.ponerEnOr(este, puerta2)
        hab3.ponerEnOr(oeste, puerta2)
        hab2.ponerEnOr(este, puerta3)
        hab4.ponerEnOr(oeste, puerta3)
        hab3.ponerEnOr(sur, puerta4)
        hab4.ponerEnOr(norte, puerta4)

        bicho1 = unFM.fabricarBichoAgresivo()
        bicho2 = unFM.fabricarBichoAgresivo()
        bicho3 = unFM.fabricarBichoPerezoso()
        bicho4 = unFM.fabricarBichoPerezoso()

        self.laberinto = unFM.fabricarLaberinto()
        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)
        self.laberinto.agregarHabitacion(hab3)
        self.laberinto.agregarHabitacion(hab4)
        self.agregarBicho(bicho1)
        self.agregarBicho(bicho2)
        self.agregarBicho(bicho3)
        self.agregarBicho(bicho4)

        bicho1.posicion = hab1
        bicho2.posicion = hab3
        bicho3.posicion = hab2
        bicho4.posicion = hab4

        return self.laberinto
    
    def eliminarBichos(self, unBicho):
        try:
            self.bichos.remove(unBicho)

        except ValueError:
            print("No existe ese objeto bicho")

    def estanTodosLosBichosMuertos(self):
        bicho = next((each for each in self.bichos if each.estaVivo()), None)

        if bicho is None and self.person.estaVivo():
            self.ganaPersonaje()
        else:
            print("Aun hay bichos vivos")

    def ganaPersonaje(self):
        print(f"Fin del juego, {self.person} ha ganado")

    def __init__(self):
        self.laberinto = None
        self.person = None
        self.bichos = []
        self.hilos = {}

    def obtenerHabitacion(self, num):
        return self.laberinto.obtenerHabitacion(num)
    
    def lanzarBicho(self, unBicho):
        print(f"{unBicho} se activa")
        def proceso():
            while unBicho.estaVivo():
              unBicho.actua()
        from threading import Thread
        proceso_hilo = Thread(target=proceso, daemon=True)
        proceso_hilo.start()
        self.hilos[unBicho] = proceso_hilo
        
    def lanzarBichos(self):
        for each in self.bichos:
            self.lanzarBicho(each)


    def muerePersonaje(self):
        print(f"Fin del juego, {self.person} ha muerto")
        self.terminarBichos()

    def terminarBicho(self, unBicho):
        unBicho.vidas = 0
        print(f"{unBicho} ha muerto")

    def terminarBichos(self):
        for each in self.bichos:
            self.terminarBicho(each)

    def obtenerHabitacion(self,unNum):
        return self.laberinto.obtenerHabitacion(unNum)
    

    def __str__(self):
        return "Juego"

class Personaje(Ente):

    def __init__(self,unaCadena,tipo=None):
        super().__init__()
        self.vidas = 100
        self.nombre = unaCadena
        self.inventario = Inventario()
        self.tipo = tipo
        if tipo is not None:
            self.vidas = tipo.vidas
            self.poder = tipo.poder
        else:
            self.vidas = 100
            self.poder = 5

    def puedeAtacar(self):
        self.juego.buscarBicho()

    def irAlEste(self):
        self.posicion.irAlEste(self)

    def irAlNorte(self):
        self.posicion.irAlNorte(self)

    def irAlOeste(self):
        self.posicion.irAlOeste(self)
    
    def irAlSur(self):
        self.posicion.irAlSur(self)

    def irAlNoroeste(self):
        self.posicion.irAlNoroeste(self)

    def irAlNoreste(self):
        self.posicion.irAlNoreste(self)

    def irAlSuroeste(self):
        self.posicion.irAlSuroeste(self)
    
    def irAlSureste(self):
        self.posicion.irAlSureste(self)

    def avisar(self):
        self.juego.muerePersonaje()

    def heMuerto(self):
        print(f"Fin del juego, {self.nombre} ha perdido.")

    def crearNuevoLaberinto(self,unTunel):
        unTunel.crearNuevoLaberinto(self)

    def obtenerComandos(self):
        lista = []
        self.posicion.recorrer(lambda each: lista.extend(each.obtenerComandos()))
        return lista

    def __str__(self):
        return f"Personaje {self.nombre}"

class TipoPersonaje:
    def __init__(self, vidas, poder):
        self.vidas = vidas
        self.poder = poder

class Luchador(TipoPersonaje):
    def __init__(self):
        super().__init__(vidas=50, poder=10)
    def __str__(self):
        return "Luchador"
    

class Mago(TipoPersonaje):
    def __init__(self):
        super().__init__(vidas=30, poder=20)
    def __str__(self):
        return "Mago"

  
    

class Orientacion:

    def caminar(self, unBicho):
        pass

    def ponerElemento(self, unEM, unContenedor):
        pass

    def obtenerElementoOrEn(self, unContenedor):
        pass

    def recorrer(self, unBloque, unContenedor):
        pass

    def calcularPosicionDesde(self, unaForma):
        pass


class Norte(Orientacion):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def ponerElemento(self, unEM, unContenedor):
        unContenedor.norte = unEM

    def recorrer(self, func, contenedor):
        if contenedor.norte is not None:
            func(contenedor.norte)

    def __str__(self):
        return "Soy la orientacion norte"

    def obtenerElementoOr(self, unContenedor):
      return unContenedor.norte

    def caminarAleatorio(self, bicho, forma):
        forma.norte.entrar(bicho)

    def aceptar(self, unVisitor, forma):
        forma.norte.aceptar(unVisitor)
    def calcularPosicionDesde(self, forma):
        unPunto=Point(forma.punto.x,forma.punto.y-1)
        forma.norte.calcularPosicionDesdeEn(forma,unPunto)


class Oeste(Orientacion):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def ponerElemento(self, unEM, unContenedor):
        unContenedor.oeste = unEM

    def recorrer(self, func, contenedor):
        if contenedor.oeste is not None:
            func(contenedor.oeste)

    def __str__(self):
        return "Soy la orientacion oeste"

    def obtenerElementoOr(self, unContenedor):
      return unContenedor.oeste

    def caminarAleatorio(self, bicho, forma):
        forma.oeste.entrar(bicho)

    def aceptar(self, unVisitor, forma):
        forma.oeste.aceptar(unVisitor)
    def calcularPosicionDesde(self, forma):
        unPunto=Point(forma.punto.x-1,forma.punto.y)
        forma.oeste.calcularPosicionDesdeEn(forma,unPunto)


class Sur(Orientacion):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def ponerElemento(self, unEM, unContenedor):
     unContenedor.sur = unEM

    def recorrer(self, func, contenedor):
        if contenedor.sur is not None:
            func(contenedor.sur)

    def __str__(self):
        return "Soy la orientacion sur"

    def obtenerElementoOr(self, unContenedor):
     return unContenedor.sur

    def caminarAleatorio(self, bicho, forma):
        forma.sur.entrar(bicho)

    def aceptar(self, unVisitor, forma):
        forma.sur.aceptar(unVisitor)

    def calcularPosicionDesde(self, forma):
        unPunto=Point(forma.punto.x,forma.punto.y+1)
        forma.sur.calcularPosicionDesdeEn(forma,unPunto)



class Este(Orientacion):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def ponerElemento(self, unEM, unContenedor):
        unContenedor.este = unEM     

    def recorrer(self, func, contenedor):
        if contenedor.este is not None:
            func(contenedor.este)

    def __str__(self):
        return "Soy la orientacion este"

    def obtenerElementoOr(self, unContenedor):
      return unContenedor.oeste

    def caminarAleatorio(self, bicho, forma):
        forma.este.entrar(bicho)

    def aceptar(self, unVisitor, forma):
        forma.este.aceptar(unVisitor)
    def calcularPosicionDesde(self, forma):
        unPunto=Point(forma.punto.x+1,forma.punto.y)
        forma.este.calcularPosicionDesdeEn(forma,unPunto)

class Sureste(Orientacion):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def caminar(self, unBicho):
        pos = unBicho.posicion
        pos.irAlSureste(unBicho)

    def ponerElemento(self, unEM, unContenedor):
        unContenedor.sureste = unEM

    def obtenerElementoOrEn(self, unContenedor):
        return unContenedor.sureste

    def recorrer(self, unBloque, unContenedor):
        unContenedor.sureste.recorrer(unBloque)

    def calcularPosicionDesde(self, unaForma):
        unPunto = (unaForma.punto.x + 1, unaForma.punto.y + 1)
        unaForma.sureste.calcularPosicionDesde(unaForma, unPunto)

    def __str__(self):
        return f"Sureste"

class Suroeste(Orientacion):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def caminar(self, unBicho):
        pos = unBicho.posicion
        pos.irAlSuroeste(unBicho)

    def ponerElemento(self, unEM, unContenedor):
        unContenedor.suroeste = unEM

    def obtenerElementoOrEn(self, unContenedor):
        return unContenedor.suroeste

    def recorrer(self, unBloque, unContenedor):
        unContenedor.suroeste.recorrer(unBloque)

    def calcularPosicionDesde(self, unaForma):
        unPunto = (unaForma.punto.x - 1, unaForma.punto.y + 1)
        unaForma.suroeste.calcularPosicionDesde(unaForma, unPunto)

    def __str__(self):
        return f"Suroeste"
    

class Noreste(Orientacion):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance    

    def caminar(self, unBicho):
        pos = unBicho.posicion
        pos.irAlNoreste(unBicho)

    def ponerElemento(self, unEM, unContenedor):
        unContenedor.noreste = unEM

    def obtenerElementoOrEn(self, unContenedor):
        return unContenedor.noreste

    def recorrer(self, unBloque, unContenedor):
        unContenedor.noreste.recorrer(unBloque)

    def calcularPosicionDesde(self, unaForma):
        unPunto = (unaForma.punto.x + 1, unaForma.punto.y - 1)
        unaForma.noreste.calcularPosicionDesde(unaForma, unPunto)

    def __str__(self):
        return f"Noreste"
    


class Noroeste(Orientacion):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def caminar(self, unBicho):
        pos = unBicho.posicion
        pos.irAlNoroeste(unBicho)

    def ponerElemento(self, unEM, unContenedor):
        unContenedor.noroeste = unEM

    def obtenerElementoOrEn(self, unContenedor):
        return unContenedor.noroeste

    def recorrer(self, unBloque, unContenedor):
        unContenedor.noroeste.recorrer(unBloque)

    def calcularPosicionDesde(self, unaForma):
        unPunto = (unaForma.punto.x - 1, unaForma.punto.y - 1)
        unaForma.noroeste.calcularPosicionDesde(unaForma, unPunto)

    def __str__(self):
        return f"Noroeste"   



class Creator:

    def fabricarBichoAgresivo(self):
        bicho = Bicho()
        bicho.modo = Agresivo() 
        bicho.vidas = 5
        bicho.poder = 5
        return bicho
    
    def fabricarBichoAgresivoPos(self, posicion):
        bicho = Bicho()
        bicho.modo = Agresivo()
        bicho.vidas = 5
        bicho.poder = 5
        bicho.posicion = posicion
        return
    
    def fabricarBichoPerezoso(self):
        bicho = Bicho()
        bicho.modo = Perezoso() 
        bicho.vida = 1
        bicho.poder = 1
        return bicho
    
    def fabricarBichoPerezosoPos(self, posicion):
        bicho = Bicho()
        bicho.modo = Perezoso()
        bicho.vida = 1
        bicho.poder = 1
        bicho.posicion = posicion
        return
    
    def cambiarAModoAgresivo(self, bicho):
        bicho.modo = Agresivo()
        bicho.vida = 5
        bicho.poder = 10

    def cambiarAModoPerezoso(self, bicho):
        bicho.modo = Perezoso()
        bicho.vida = 1
        bicho.poder = 1

    def fabricarForma(self):
        return Forma()
    
    def fabricarBomba(self):
        return Bomba()
    
    def fabricarEste(self):
        return Este()
    
    def fabricarOeste(self):
        return Oeste()
    
    def fabricarNorte(self):
        return Norte()
    
    def fabricarSur(self):
        return Sur()
    
    def fabricarHabitacion(self, unNum):
        hab = Habitacion()
        hab.num= unNum
        hab.forma = self.fabricarForma()
        hab.agregarOrientacion(self.fabricarEste())
        hab.agregarOrientacion(self.fabricarOeste())
        hab.agregarOrientacion(self.fabricarNorte())
        hab.agregarOrientacion(self.fabricarSur())
        for each in hab.obtenerOrientaciones():
            hab.ponerEnOr( each, self.fabricarPared())
        return hab
    
    def fabricarPared(self):
        return Pared()
    
    def fabricarPuerta(self):
        return Puerta()
    
    def fabricarJuego(self):
        return Juego()
    
    def fabricarLaberinto(self):
        return Laberinto()
    
    def fabricarNorte(self):
        return Norte()
    def fabricarSur(self):  
        return Sur()
    def fabricarEste(self):
        return Este()
    def fabricarOeste(self):
        return Oeste()
    

class CreatorB(Creator):
   
    def fabricarPared(self):
        return ParedBomba()
    

class Visitor:
    def visitarHabitacion(self, habitacion):
        pass

    def visitarPared(self, pared):
        pass

    def visitarPuerta(self, puerta):
        pass

    def visitarBomba(self, bomba):
        pass

    def visitarTunel(self, tunel):
        pass



class visitorActivarBomba:
    def visitarBomba(self, bomba):
        bomba.activar()


class VisitorInventario:
    def visitarArmario(self, armario):
        print(f"{armario} ha sido visitado por el inventario")

    def visitarPuerta(self, puerta):
        print(f"{puerta} ha sido visitada por el inventario")

    def visitarTunel(self, tunel):
        print(f"{tunel} ha sido visitado por el inventario")

    def visitarPared(self, pared):
        print(f"{pared} ha sido visitada por el inventario")

    def visitarHabitacion(self, habitacion):
        print(f"{habitacion} ha sido visitada por el inventario")



class LaberintoBuilder:

    def __init__(self):
        self.laberinto = None
        self.juego = None

    def fabricarArmario(self, unNum, unContenedor):
    

        arm = Armario()
        arm.num = unNum
        arm.forma = self.fabricarForma()

        for each in arm.obtenerOrientaciones():
            arm.ponerEnOr(each, self.fabricarPared())

        unContenedor.agregarHijo(arm)
        return arm
    
    def fabricarBichoBoss(self):
     bicho=Bicho()
     bicho.modo = BichoBoss()
     bicho.vidas = 50  # O el valor que quieras para el boss
     bicho.poder = 10 
     return bicho
    
    def fabricarBichoBossPos(self, unaHab):
     bicho=Bicho()
     bicho.modo = BichoBoss()
     bicho.posicion = unaHab
     return bicho

    def fabricarBichoAgresivo(self):
        bicho = Bicho()
        bicho.modo = Agresivo()
        bicho.vidas = 5
        bicho.poder = 5
        return bicho
    
    def fabricarBichoAgresivoPos(self, unaHab):
        bicho = Bicho()
        bicho.modo = Agresivo()
        bicho.posicion = unaHab
        bicho.vidas = 5
        bicho.poder = 5
        return bicho
    
    def fabricarBichoPerezoso(self):
        bicho = Bicho()
        bicho.modo = Perezoso()
        bicho.vidas = 5
        bicho.poder = 1
        return bicho
    
    def fabricarBichoPerezosoPos(self, unaHab):
        bicho = Bicho()
        bicho.modo = Perezoso()
        bicho.posicion = unaHab
        bicho.vidas = 5
        bicho.poder = 1
        return bicho
    
    def fabricarBichoModo(self, strModo, unNum):
    
     
        hab = self.juego.obtenerHabitacion(unNum)
        bicho = getattr(self, f"fabricarBicho{strModo.capitalize()}")()
        hab.entrar(bicho)
        self.juego.agregarBicho(bicho)

    def fabricarBombaEn(self, unContenedor):
        bmb = Bomba()
        unContenedor.agregarHijo(bmb)

    def fabricarEste(self):
        return Este()
    
    def fabricarNorte(self):
        return Norte()
    
    def fabricarOeste(self):
        return Oeste()
    
    def fabricarSur(self):
        return Sur()
    
    
    def fabricarForma(self):
        forma = Cuadrado()
        forma.agregarOrientacion(self.fabricarNorte())
        forma.agregarOrientacion(self.fabricarEste())
        forma.agregarOrientacion(self.fabricarSur())
        forma.agregarOrientacion(self.fabricarOeste())
        return forma
    
    def fabricarHabitacion(self, unNum):
      hab = Habitacion()
      hab.num = unNum
      hab.forma = self.fabricarForma()
      hab.forma.num = unNum

      for each in hab.obtenerOrientaciones():
        hab.ponerEnOr(each, self.fabricarPared())

      self.laberinto.agregarHabitacion(hab)
      return hab
    
    def fabricarJuego(self):
        self.juego= Juego()
        self.juego.prototipo = self.laberinto
        self.juego.laberinto= self.juego.clonarLaberinto()

    def fabricarLaberinto(self):
           self.laberinto = Laberinto()

    def fabricarPuertaL1(self, num1, strOr1, num2, strOr2):
    
        hab1 = self.laberinto.obtenerHabitacion(num1)
        hab2 = self.laberinto.obtenerHabitacion(num2)

        objOr1 = getattr(self, f"fabricar{strOr1.capitalize()}")()  # Ejemplo: fabricarNorte
        objOr2 = getattr(self, f"fabricar{strOr2.capitalize()}")()

        pt = Puerta()
        pt.lado1 = hab1
        pt.lado2 = hab2

        hab1.ponerEnOr(objOr1, pt)
        hab2.ponerEnOr(objOr2, pt)

    def fabricarPared(self):
        return Pared()

    def fabricarTunelEn(self, unContenedor):
        tunel = Tunel()
        tunel.agregarComando(Entrar(receptor=tunel))
        unContenedor.agregarHijo(tunel)

    def obtenerJuego(self):
        return self.juego

    def fabricarCofreEn(self, unContenedor):
     cofre = Cofre()
     unContenedor.agregarHijo(cofre)

class LaberintoBuilderRombo(LaberintoBuilder):
   
    def __init__(self):
      super().__init__()
   
    def fabricarForma(self):
     forma = Rombo()
     forma.agregarOrientacion(self.fabricarNoroeste())
     forma.agregarOrientacion(self.fabricarSuroeste())
     forma.agregarOrientacion(self.fabricarSureste())
     forma.agregarOrientacion(self.fabricarNoroeste())
     return forma 
    
    def fabricarNoroeste(self):
        return Noroeste()
    def fabricarSuroeste(self):
        return Suroeste()
    def fabricarSureste(self):
        return Sureste()
    def fabricarNoreste(self):
        return Noreste()
    


class LaberintoBuilderHexagono(LaberintoBuilder):
    def fabricarForma(self):
        forma = Hexagono()
        forma.agregarOrientacion(self.fabricarNorte())
        forma.agregarOrientacion(self.fabricarNoreste())
        forma.agregarOrientacion(self.fabricarSureste())
        forma.agregarOrientacion(self.fabricarSur())
        forma.agregarOrientacion(self.fabricarSuroeste())
        forma.agregarOrientacion(self.fabricarNoroeste())
        return forma

    def fabricarNoreste(self):
        return Noreste()

    def fabricarSureste(self):
        return Sureste()

    def fabricarSuroeste(self):
        return Suroeste()

    def fabricarNoroeste(self):
        return Noroeste()

class LaberintoBuilderTriangulo(LaberintoBuilder):
    def fabricarForma(self):
        forma = Triangulo()
        forma.agregarOrientacion(self.fabricarNorte())
        forma.agregarOrientacion(self.fabricarSureste())
        forma.agregarOrientacion(self.fabricarSuroeste())
        return forma

    def fabricarSureste(self):
        return Sureste()

    def fabricarSuroeste(self):
        return Suroeste()
    
    def fabricarNorte(self):
        return Norte()
    
class Director:

    def __init__(self):
        self.builder = None
        self.dict = None

    def fabricarBichos(self):
        bichos = self.dict.get('bichos', None)
        if bichos is None:
            return  

        for each in bichos:
            self.builder.fabricarBichoModo(
                each.get('modo'),  # Modo del bicho
                each.get('posicion')  # Posición del bicho
            )

    def fabricarJuego(self):
        self.builder.fabricarJuego()

    def fabricarLaberinto(self):
          self.builder.fabricarLaberinto()
    # Recorrer la colección de habitaciones/armarios/etc.
          laberinto = self.dict.get('laberinto', [])
          for each in laberinto:
           self.fabricarLaberintoRecursivo(each, 'root')
    # Recorrer la colección de puertas para poner las puertas
          puertas = self.dict.get('puertas', [])
          for each in puertas:
           self.builder.fabricarPuertaL1(each[0], each[1], each[2], each[3])

    def fabricarLaberintoRecursivo(self, unDic, padre):
      con = None
    # Contenedores
      if unDic.get('tipo') == 'habitacion':
          con = self.builder.fabricarHabitacion(unDic.get('num'))
      elif unDic.get('tipo') == 'armario':
         con = self.builder.fabricarArmario(unDic.get('num'), padre)
     # Hojas: hay que indicar el contenedor donde va la hoja
      if unDic.get('tipo') == 'bomba':
        self.builder.fabricarBombaEn(padre)
      elif unDic.get('tipo') == 'tunel':
        self.builder.fabricarTunelEn(padre)
      elif unDic.get('tipo') == 'cofre':
        self.builder.fabricarCofreEn(padre)
    # Recursividad para los hijos
      hijos = unDic.get('hijos', None)
      if hijos is not None:
        for each in hijos:
            self.fabricarLaberintoRecursivo(each, con)

    def iniBuilder(self):

        if self.dict.get('forma') == 'cuadrado':
            self.builder = LaberintoBuilder()
        elif self.dict.get('forma') == 'rombo':
            self.builder = LaberintoBuilderRombo()
        elif self.dict.get('forma') == 'hexagono':
         self.builder = LaberintoBuilderHexagono()
        elif self.dict.get('forma') == 'triangulo':
           self.builder = LaberintoBuilderTriangulo()
       

    def leerArchivo(self, unArchivoJSON):
    
        with open(unArchivoJSON, 'r') as readStream:
            self.dict = json.load(readStream)

    def obtenerJuego(self):
        return self.builder.obtenerJuego()
    
    def procesar(self, unArchivoJSON):
        self.leerArchivo(unArchivoJSON)
        self.iniBuilder()
        self.fabricarLaberinto()
        self.fabricarJuego()
        self.fabricarBichos()