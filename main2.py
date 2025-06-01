from juego import Director, Mago, Luchador

def main():
    director = Director()
    ruta = "C:\\Users\\Usuario\\Desktop\\Git\\PruebaPersonajeGana"
    director.procesar(ruta)
    juego = director.obtenerJuego()

    # Elige el tipo de personaje (puedes cambiar a Luchador() si quieres)
    tipo = Mago()
    juego.agregarPersonaje("Joselu")
    personaje = juego.person
    personaje.tipo = tipo
    personaje.vidas = tipo.vidas
    personaje.poder = tipo.poder


    juego.abrirPuertas()

    # Coloca al personaje en la habitación 3 (donde está el boss y el cofre)
    personaje.irAlSureste()

    # Abrir todas las puertas
   
      # Buscar y abrir el cofre
    cofre = next((h for h in personaje.posicion.hijos if hasattr(h, "es_cofre") and h.es_cofre()), None)
    if cofre:
        print("\n¡Has encontrado un cofre!")
        cofre.mostrarObjetos()
        # Ejemplo: coger el primer objeto del cofre
        cofre.elegirObjeto(0, personaje)
        personaje.inventario.mostrar()
        personaje.inventario.usar(0, personaje)  # Usar el primer objeto del inventario
    else:
        print("\nNo hay cofre en esta habitación.")

    

    # Buscar al boss en la habitación 3
    boss = next((b for b in juego.bichos if hasattr(b.modo, "esBoss") and b.modo.esBoss()), None)
    if boss:
        boss.posicion = personaje.posicion  # Asegura que el boss está en la misma habitación
        print("¡Combate contra el Boss!")
        while boss.estaVivo() and personaje.estaVivo():
            personaje.atacar()
            personaje.esAtacadoPor(boss)  # El personaje ataca al boss (puedes cambiar el método si tienes uno específico)
            if boss.estaVivo():
                boss.esAtacadoPor(personaje)  # El boss ataca al personaje (puedes cambiar el método si tienes uno específico)
              
    else:
        print("No se encontró al boss.")

  

    print(f"\nEstado final: {personaje.nombre}, vidas: {personaje.vidas}, poder: {personaje.poder}")

if __name__ == "__main__":
    main()