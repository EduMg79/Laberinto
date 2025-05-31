# Importamos las clases necesarias
from juego import Director, Juego, Creator, CreatorB,Arco

def main():

    arco= Arco()
    director = Director()
    director.procesar(ruta)
    juego= director.obtenerJuego()
    juego.agregarPersonaje("Joselu")
    personaje=juego.person
    personaje.poder = 2  # Asignamos un poder al personaje
    juego.abrirPuertas()
    juego.lanzarBichos()
    b1=juego.bichos[0]
    b2=juego.bichos[1]
    b1.poder=10
    juego.buscarBicho()
    juego.buscarPersonaje(b1)
    personaje.irAlSur()
    personaje.irAlEste()
    personaje.irAlNorte()
    personaje.irAlOeste()
    arco.usar(personaje)
    personaje.atacar()
    personaje.atacar()
    juego.estanTodosLosBichosMuertos()
    personaje.irAlSur()
    personaje.atacar()
    personaje.atacar()
    personaje.atacar()
    personaje.irAlNorte()
    juego.buscarBicho()
    juego.estanTodosLosBichosMuertos()
    

   


    print(f"\nEstado del personaje:")
    print(f"Nombre: {personaje.nombre}")
    print(f"Vidas: {personaje.vidas}")
    print(f"Poder: {getattr(personaje, 'poder', 1)}")
    
    print(f"Posición actual: Habitación {personaje.posicion.num}")
 
   


if __name__ == "__main__":
    ruta="C:\\Users\\Usuario\\Desktop\\3º\\lab2H1B.json"
    main()