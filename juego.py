import random

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
        self.padre = None
    
    def recorrer(self, func):
        func(self)

    def entrar(self, alguien):
        pass

    def esPuerta(self):
        return False

    def aceptar(self, unVisitor):
        pass

    def calcularPosicionDesde(self,forma):
        pass
    def calcularPosicion(self):
        pass
    def calcularPosicionDesdeEn(self,forma, punto):
        pass
    def __str__(self):
        return "Soy un ElementoMapa"
    

class Contenedor(ElementoMapa):
    def __init__(self):
        super().__init__()
        self.hijos = []
        self.forma = None

    def agregar_hijo(self, hijo):
        hijo.padre = self
        self.hijos.append(hijo)

    def eliminar_hijo(self, hijo):
        self.hijos.remove(hijo)

    def agregarOrientacion(self, orientacion):
        self.forma.agregarOrientacion(orientacion)

    def eliminarOrientacion(self, orientacion):
        self.forma.eliminarOrientacion(orientacion)

    def ponerElementoEnOrientacion(self, elemento, orientacion):
        self.forma.ponerElementoEnOrientacion(elemento, orientacion)

    def recorrer(self, func):
        func(self)
        for hijo in self.hijos:
            hijo.recorrer(func)
        self.forma.recorrer(func)

    def obtenerElementoEnOrientacion(self, orientacion):
        return self.forma.obtenerElementoEnOrientacion(orientacion)
    
    def caminarAleatorio(self, bicho):
        self.forma.caminarAleatorio(bicho)

    def aceptar(self, unVisitor):
        self.visitarContenedor(unVisitor)
        for hijo in self.hijos:
            hijo.aceptar(unVisitor)
        self.forma.aceptar(unVisitor)

class Armario(Contenedor):

    def __init__(self):
        super().__init__()

    def esArmario(self):
        return True

class Habitacion(Contenedor):
    def __init__(self, num):
        super().__init__()
        self.num = num

    def entrar(self, alguien):
        print(f"Entrando en la habitación {self.num}")
        alguien.posicion=self

    def visitarContenedor(self, unVisitor):
        unVisitor.visitarHabitacion(self)
    def calcularPosicion(self):
        self.forma.calcularPosicion()
    def __str__(self):
        return "Soy una habitacion"

    def conectar(self, direccion, elemento):
       
        setattr(self, direccion, elemento)
   
    def mostrar(self):
        # Muestra las conexiones (puertas y paredes) de la habitación
        print(f"Habitación {self.num}:")
        print(f"  Norte: {self.norte.__class__.__name__ if self.norte else 'Ninguno'}")
        print(f"  Sur: {self.sur.__class__.__name__ if self.sur else 'Ninguno'}")
        print(f"  Este: {self.este.__class__.__name__ if self.este else 'Ninguno'}")
        print(f"  Oeste: {self.oeste.__class__.__name__ if self.oeste else 'Ninguno'}")
        print("--------------------")   
  

class Laberinto(Contenedor):
    def __init__(self):
        super().__init__()        

    def entrar(self,alguien):
        print("Entrando en el laberinto")
        hab1=self.obtenerHabitacion(1)
        hab1.entrar(alguien)

    def __str__(self):
        return "Soy un laberinto"

    def agregarHabitacion(self, habitacion):
        self.hijos.append(habitacion)

    def obtenerHabitacion(self, num):
        for habitacion in self.hijos:
            if habitacion.num == num:
                return habitacion
        return None
    
    def recorrer(self, func):
        func(self)
        for hijo in self.hijos:
            hijo.recorrer(func)

    def entrar(self, alguien):        
        hab1=self.obtenerHabitacion(1)
        hab1.entrar(alguien)
        print(f"{alguien} entra en el laberinto")
    
    def aceptar(self, unVisitor):
        #unVisitor.visitarContenedor(self)
        for hijo in self.hijos:
            hijo.aceptar(unVisitor)
        #self.forma.aceptar(unVisitor)
        
    def mostrar(self):
      
        for habitacion in self.habitaciones:
            habitacion.mostrar()    



class Hoja(ElementoMapa):
    def __init__(self):
        super().__init__()
    



class Decorator(Hoja):
    def __init__(self, em):
        super().__init__()
        self.em = em

    def __str__(self):
        return "Soy un decorator"
  


class Bomba(Decorator):
    def __init__(self, em):
        super().__init__(em)
        self.activa = False

    def esBomba(self):
        return True

    def aceptar(self, unVisitor):
        unVisitor.visitarBomba(self)
    
    def __str__(self):
        return "Soy una bomba"
    


class Tunel(Hoja):
    def __init__(self, laberinto):
        super().__init__()
        self.laberinto = None

    def puedeClonarLaberinto(self,alguien):
        self.laberinto = alguien.juego.clonarLaberinto()
        self.laberinto.entrar(self)

    def aceptar(self, unVisitor):
        unVisitor.visitarTunel(self)

    def entrar(self, alguien):
        if self.laberinto is None:
            alguien.clonarLaberinto(self)            
        else:
            self.laberinto.entrar(alguien)



class Pared(ElementoMapa):
    def __init__(self):
        super().__init__()

    def entrar(self,alguien):
        print("chocando en una pared")

    def __str__(self):
        return "Soy una pared"


class ParedBomba(Pared):
    def __init__(self):
        super().__init__()
        self.activa = False

    def entrar(self):
        print("Entrando en una pared bomba")

    def __str__(self):
        return "Soy una pared bomba"


class Puerta(ElementoMapa):
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2
        self.visitada = False
        self.estadoPuerta = Cerrada()

    def entrar(self, alguien):
        self.estadoPuerta.entrar(self, alguien)

    def puedeEntrar(self, alguien):
        print("Entrando en una puerta")
        if alguien.posicion == self.lado1:
            self.lado2.entrar(alguien)
        else:
            self.lado1.entrar(alguien)

    def abrir(self):
        print("Abriendo puerta")
        self.estadoPuerta.abrir(self)

    def cerrar(self):
        print("Cerrando puerta")
        self.estadoPuerta.cerrar(self)

    def esPuerta(self):
        return True
    
    def aceptar(self, unVisitor):
        unVisitor.visitarPuerta(self)

    def calcularPosicionDesdeEn(self,forma, punto):
        print("punto: ", punto.x, punto.y)
        if self.visitada:
            return
        self.visitada = True
        if self.lado1.num == forma.num:
            self.lado2.forma.punto=punto
            self.lado2.calcularPosicion()
        else:
            self.lado1.forma.punto=punto
            self.lado1.calcularPosicion()
    
    def __str__(self):
        return "Soy una puerta"


class Ente:
    def __init__(self):
        self.vidas = None
        self.poder = None
        self.posicion = None
        self.juego = None
        self.estadoEnte = Vivo()

    def clonarLaberinto(self,tunel):
        pass

    def esAtacadoPor(self, atacante):
        print(f"Ataque: {self}  es atacado")
        self.vidas -= atacante.poder
        print(f"Vidas restantes: {self.vidas}")
        if self.vidas <= 0:
            print(f"El ente ha muerto")
            self.estadoEnte.morir(self)

class Personaje(Ente):
    def __init__(self, vidas, poder, juego, nombre):
        super().__init__()
        self.nombre = nombre
        self.vidas = vidas
        self.juego = juego

    def clonarLaberinto(self,tunel):
        tunel.puedeClonarLaberinto()

    def atacar(self):
        self.juego.buscarBicho()

    def __str__(self):
        return self.nombre
    

class Arma:
 def usar(self, personaje):
  raise NotImplementedError("Este método debe ser implementado por las subclases")
 

class Arco(Arma):
 def usar(self, personaje):
  personaje.poder += 3
  print(f"{personaje.nombre} ha equipado un arco. Poder aumentado a {personaje.poder}")


class Espada(Arma):
 def usar(self, personaje):
  personaje.poder += 5
  print(f"{personaje.nombre} ha equipado una espada. Poder aumentado a {personaje.poder}")


class PocionVida(Arma):
 def usar(self, personaje):
  personaje.vidas += 10
  print(f"{personaje.nombre} ha usado una poción de vida. Vidas aumentadas a {personaje.vidas}")


class Bicho(Ente):
    def __init__(self):
        self.modo = None
        self.running = True
        self.poder = None
        self.vidas = None
        self.posicion = None

    def actua(self):
        while self.estaVivo():
            self.modo.actuar(self)

    def iniAgresivo(self):
        self.modo = Agresivo()
        self.poder = 10
        self.vidas = 5

    def iniPerezoso(self):
        self.poder = 1
        self.vidas = 5

    def atacar(self):
        self.juego.buscarPersonaje(self)
    def caminar(self):
        self.posicion.caminarAleatorio(self)

    def estaVivo(self):
        return self.vidas > 0

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

    def vivir(self, ente):
        print("El ente ya está vivo")

    def morir(self, ente):
        print("El ente muere")
        ente.estadoEnte = Muerto()


class Muerto(EstadoEnte):
    def __init__(self):
        super().__init__()

    def vivir(self, ente):
        print("El ente revive")
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
    def __init__(self):
        super().__init__()

    def abrir(self, puerta):
        print("La puerta ya está abierta")

    def cerrar(self, puerta):
        print("Cerrando la puerta")
        puerta.estadoPuerta = Cerrada()

    def entrar(self, puerta, alguien):
        puerta.puedeEntrar(alguien)


class Cerrada(EstadoPuerta):
    def __init__(self):
        super().__init__()

    def abrir(self, puerta):
        print("Abriendo la puerta")
        puerta.estadoPuerta = Abierta()

    def cerrar(self, puerta):
        print("La puerta ya está cerrada")

    def entrar(self, puerta, alguien):
        pass


class Forma:
    def __init__(self):
        self.orientaciones = []
        self.num=None
        self.punto=None
        self.extent=Point(0,0)

    def agregarOrientacion(self, orientacion):
        self.orientaciones.append(orientacion)

    def eliminarOrientacion(self, orientacion):
        self.orientaciones.remove(orientacion)

    def ponerElementoEnOrientacion(self, elemento, orientacion):
        orientacion.poner(elemento, self)

    def obtenerElementoEnOrientacion(self, orientacion):
        return orientacion.obtenerElemento(self)

    def recorrer(self, func):
        for orientacion in self.orientaciones:
            orientacion.recorrer(func, self)
    def calcularPosicion(self):
        for orientacion in self.orientaciones:
            orientacion.calcularPosicionDesde(self)
    def caminarAleatorio(self, bicho):
        orientacion=self.obtenerOrientacionAleatoria()
        print(f"Orientacion aleatoria: {orientacion}")
        orientacion.caminarAleatorio(bicho, self)

    def obtenerOrientacionAleatoria(self):
        return random.choice(self.orientaciones)

    def aceptar(self, unVisitor):
        for orientacion in self.orientaciones:
            orientacion.aceptar(unVisitor, self)   


class Cuadrado(Forma):
    def __init__(self):
        super().__init__()
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None
        self.orientaciones = []





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

    def __str__(self):
        return "Soy un modo"

import time
class Agresivo(Modo):
    def __init__(self):
        super().__init__()

    def dormir(self, bicho):
        print("Agresivo: Durmiendo un poco...")
        time.sleep(1)

    def __str__(self):
        return "-agresivo"

 

class Perezoso(Modo):
    def __init__(self):
        super().__init__()

    def dormir(self, bicho):
        print("Perezoso: Zzzzz...")
        time.sleep(3)

    def __str__(self):
        return "-perezoso"
    

class Juego:

    def abrirPuertas(self):
        self.laberinto.abrirPuertas()

    def agregarBicho(self, unBicho):
        self.bichos.append(unBicho)
        unBicho.juego = self

    def agregarPersonaje(self, unaCadena):
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

    def __init__(self,nombre):
        super().__init__()
        self.vidas = 50
        self.nombre = nombre
        self.poder = 1

    def atacar(self):
        self.juego.buscar_bicho()
        print(f"{self.nombre} ataca")

    def he_muerto(self):
       self.juego.muere_personaje()
       print(f"{self.nombre} ha muerto")

    def ir_al_este(self):
        self.posicion.ir_al_este(self)
    
    
    def ir_al_oeste(self):
        self.posicion.ir_al_oeste(self)
    
        
    def ir_al_sur(self):
        self.posicion.ir_al_sur(self)

    def ir_al_norte(self):
     self.posicion.ir_al_norte(self)
    
    def crear_nuevo_laberinto(self, un_tunel):
      un_tunel.crear_nuevo_laberinto(self)

class Orientacion:
    def __init__(self):
        pass

    def poner(self, elemento, contenedor):
        pass

    def recorrer(self, func, forma):
        raise NotImplementedError

    def __str__(self):
        return "Soy una orientacion"

    def obtenerElemento(self, forma):
        raise NotImplementedError
    def caminarAleatorio(self, bicho, forma):
        raise NotImplementedError
    def aceptar(self, unVisitor, forma):
        raise NotImplementedError
    def calcularPosicionDesde(self, forma):
        raise NotImplementedError


class Norte(Orientacion):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def poner(self, elemento, contenedor):
        contenedor.norte = elemento

    def recorrer(self, func, contenedor):
        if contenedor.norte is not None:
            func(contenedor.norte)

    def __str__(self):
        return "Soy la orientacion norte"

    def obtenerElemento(self, forma):
        return forma.norte

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

    def poner(self, elemento, contenedor):
        contenedor.oeste = elemento

    def recorrer(self, func, contenedor):
        if contenedor.oeste is not None:
            func(contenedor.oeste)

    def __str__(self):
        return "Soy la orientacion oeste"

    def obtenerElemento(self, forma):
        return forma.oeste

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

    def poner(self, elemento, contenedor):
        contenedor.sur = elemento

    def recorrer(self, func, contenedor):
        if contenedor.sur is not None:
            func(contenedor.sur)

    def __str__(self):
        return "Soy la orientacion sur"

    def obtenerElemento(self, forma):
        return forma.sur

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

    def poner(self, elemento, contenedor):
        contenedor.este = elemento

    def recorrer(self, func, contenedor):
        if contenedor.este is not None:
            func(contenedor.este)

    def __str__(self):
        return "Soy la orientacion este"

    def obtenerElemento(self, forma):
        return forma.este

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
   #Clase creator de smalltalk
   #Creamos paredes normales, puertas y bichos 
    def fabricar_habitacion(self, num):
        hab = Habitacion(num)
       
        hab.este = self.fabricar_pared()
        hab.oeste = self.fabricar_pared()
        hab.norte = self.fabricar_pared()
        hab.sur = self.fabricar_pared()
        return hab

    def fabricar_juego(self):
        return Juego()
    
    def fabricar_laberinto(self):
        return Laberinto()
    
    def fabricar_pared(self):
        return Pared()
    
    def fabricar_puerta(self, lado1, lado2):
        return Puerta(lado1, lado2)
    
   
    def fabricar_bomba(self):
       
        return Bomba(None)

   
    def fabricar_bicho_agresivo(self):
        bicho = Bicho()
        bicho.ini_agresivo()
        return bicho
    
    def fabricar_bicho_perezoso(self):
        bicho = Bicho()
        bicho.ini_perezoso()
        return bicho
    
    def cambiar_a_modo_agresivo(self, bicho):
        bicho.ini_agresivo()


class CreatorB(Creator):
   
    def fabricar_pared(self):
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