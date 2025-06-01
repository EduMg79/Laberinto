from juego import Director, Mago, Luchador, PocionVenenosa

def main():
    director = Director()
    ruta = "C:\\Users\\Usuario\\Desktop\\Git\\PruebaJsonPersonajePierde"
    director.procesar(ruta)
    juego = director.obtenerJuego()
    pocion=PocionVenenosa()

    # Elige el tipo de personaje (puedes cambiar a Luchador() si quieres)
    tipo = Luchador()  # Menos vidas y poder para perder más fácil
    juego.agregarPersonaje("Joselu")
    personaje = juego.person
    personaje.tipo = tipo
    personaje.vidas = tipo.vidas
    personaje.poder = tipo.poder
    personaje.inventario.agregar(pocion) 
    personaje.inventario.mostrar()
    personaje.inventario.usar(0, personaje)


    juego.abrirPuertas()

    # Coloca al personaje en la habitación 1 (donde hay bichos y bomba)
    personaje.irAlEste()
    

    print(f"Estado inicial: {personaje.nombre}, vidas: {personaje.vidas}, poder: {personaje.poder}")

    while personaje.estaVivo():
     for bicho in juego.bichos:
        bicho.posicion = personaje.posicion  # Asegura que todos están en la misma habitación
        print(f"{bicho} ataca a {personaje.nombre}")
        personaje.esAtacadoPor(bicho)
        personaje.atacar()
        if  personaje.vidas<=0:
            print(f"{personaje.nombre} ha muerto.")
            break

 
        
    print(f"Fin del juego, {personaje.nombre} ha perdido.")
if __name__ == "__main__":
    main()