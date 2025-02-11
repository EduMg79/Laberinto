class ElementoMapa:
    """Clase base para los elementos del laberinto."""
    pass

class Pared(ElementoMapa):
    """Representa una pared en el laberinto."""
    def __str__(self):
        return "Pared"

class Puerta(ElementoMapa):
    """Representa una puerta que conecta dos habitaciones."""
    def __init__(self, lado1, lado2, abierta=False):
        self.lado1 = lado1
        self.lado2 = lado2
        self.abierta = abierta

    def abrir(self):
        """Abre la puerta si está cerrada."""
        self.abierta = True

    def cerrar(self):
        """Cierra la puerta."""
        self.abierta = False

    def __str__(self):
        return "Puerta abierta" if self.abierta else "Puerta cerrada"

class Habitacion(ElementoMapa):
    """Representa una habitación dentro del laberinto."""
    def __init__(self, num):
        self.num = num
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None

    def establecer_lados(self, norte, sur, este, oeste):
        """Asigna los lados de la habitación."""
        self.norte = norte
        self.sur = sur
        self.este = este
        self.oeste = oeste

    def __str__(self):
        return f"Habitación {self.num}"

class Laberinto(ElementoMapa):
    """Representa el laberinto, que contiene varias habitaciones."""
    def __init__(self):
        self.habitaciones = {}

    def agregar_habitacion(self, habitacion):
        """Añade una habitación al laberinto."""
        self.habitaciones[habitacion.num] = habitacion

    def obtener_habitacion(self, num):
        """Devuelve la habitación con el número especificado."""
        return self.habitaciones.get(num, None)

class Juego:
    """Clase principal que gestiona el juego y el laberinto."""
    def __init__(self):
        self.laberinto = self.crear_laberinto()

    def crear_laberinto(self):
        """Crea un laberinto simple con habitaciones y conexiones."""
        laberinto = Laberinto()

        # Crear habitaciones
        hab1 = Habitacion(1)
        hab2 = Habitacion(2)

        # Crear una puerta entre hab1 y hab2
        puerta = Puerta(hab1, hab2)

        # Asignar paredes y puertas a las habitaciones
        hab1.establecer_lados(Pared(), puerta, Pared(), Pared())
        hab2.establecer_lados(Pared(), Pared(), Pared(), puerta)

        # Agregar habitaciones al laberinto
        laberinto.agregar_habitacion(hab1)
        laberinto.agregar_habitacion(hab2)

        return laberinto

    def jugar(self):
        """Simula el juego, permitiendo moverse entre habitaciones."""
        habitacion_actual = self.laberinto.obtener_habitacion(1)

        while True:
            print(f"\nEstás en {habitacion_actual}")
            print("Opciones de movimiento:")
            if isinstance(habitacion_actual.norte, Puerta):
                print("- Norte: " + str(habitacion_actual.norte))
            if isinstance(habitacion_actual.sur, Puerta):
                print("- Sur: " + str(habitacion_actual.sur))
            if isinstance(habitacion_actual.este, Puerta):
                print("- Este: " + str(habitacion_actual.este))
            if isinstance(habitacion_actual.oeste, Puerta):
                print("- Oeste: " + str(habitacion_actual.oeste))

            mov = input("¿A dónde quieres ir? (n/s/e/o) o 'salir': ").lower()

            if mov == 'salir':
                print("¡Juego terminado!")
                break
            elif mov == 'n' and isinstance(habitacion_actual.norte, Puerta):
                if habitacion_actual.norte.abierta:
                    habitacion_actual = habitacion_actual.norte.lado2
                else:
                    print("La puerta está cerrada.")
            elif mov == 's' and isinstance(habitacion_actual.sur, Puerta):
                if habitacion_actual.sur.abierta:
                    habitacion_actual = habitacion_actual.sur.lado1
                else:
                    print("La puerta está cerrada.")
            else:
                print("Movimiento no válido o bloqueado por una pared.")

# Iniciar el juego
if __name__ == "__main__":
    juego = Juego()
    juego.jugar()
