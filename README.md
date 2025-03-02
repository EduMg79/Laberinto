#  Juego Laberinto Python Diseño SW

En este repositorio tenemos la version **Python** del proyecto **Juego Laberinto** que hemos trabajado en clase con Smalltalk.

![Image](https://github.com/user-attachments/assets/e7ac8ae8-00a1-463a-868e-c6125958afd0)


##  Estructura del Proyecto

Las clases del juego son:

- **`Elemento Mapa`**  
  - Clase principal para definir los métodos de las clases `Habitación`  `Puerta` y `Pared`.
  - Implementa los métodos (`es_habitacion`, `es_puerta` y `es_pared`) para comprobar si un objeto es una habitación, una puerta o una pared, estos metodos seran heredados.


- **`Bomba`**  
  - Subclase de `Decorador`.
  - Coloca bombas inicialmente sin activar y nos avisa si nos hemos chocado con una bomba.

- **`Pared`**  
  - subclase de `Elemento Mapa`.
  - Representa una pared dentro del laberinto.
  - Hereda el método `esHabitacion()`.

- **`ParedBomba`**  
  - subclase de `Pared`.
  - Funciona igual que una pared pero con una bomba que si esta activada nos avisa si nos hemos chocado.

- **`Puerta`**  
  - Subclase de `Elemento Mapa`.
  - tiene dos lados y puede estar abierta o cerrada.
  - Hereda el método `entrar()` que nos avisa si la puerta esta abierta o cerrada.
  - Hereda el método `esPuerta()`.



- **`Habitacion`**   
  - Subclase de `Contenedor`.
  - Tiene 4 paredes representadas con las variables de orientacion `norte`, `sur`, `este` y `oeste`.
  - Hereda el método `esHabitacion()`.
  - Los métodos `conectar()` y `mostrar()` son añadidos solo en python para ayudar a la implementacion y mostrar la solucion.

- **`Bicho`**  
  - Representa los enemigos del laberinto.
  - Tiene de atributos `vidas`, `poder`  `modo` (agresivo o perezoso) y `posicion`.
  - Dependiendo del modo de los bichos sus atributos varían (mas vida y mas poder).
  - Solo puede haber un bicho en una `Habitacion`.

- **`Modo`** 
  - Define si el modo de un bicho es `agresivo` o `perezoso`.

- **`Juego`** 
  - Define los métodos para crear diferentes `Laberintos`.
  - Podemos crearlos tambien utilizando el patron **`Factory Method`** y el **`Decorador`**.

- **`Laberinto`** 
  - Subclase de `Contenedor`.
  - Contiene los metodos `agregarHabitacion()` , `eliminarHabitacion()`, `obtenerHabitacion()` y `esLaberinto()`.
  - Representa un laberinto con una coleccion de `Habitaciones`.
  - En python tiene el método `mostrar()` para mostrar el laberinto de la misma forma que en Smalltalk.

- **`Creator`**  
  - Utiliza **`Factory Method`** para instanciar los elementos  `Habitacion`, `Pared`, `Puerta` y `Bomba` para asi poder crear un laberinto.
  - `CreatorB` crea  `ParedBomba` en vez de `Pared`.
  
---

## Patrones de Diseño de Smalltalk

###  Factory Method
- Define las clases `Creator` y `CreatorB`.
- Permite fabricar otros tipos de `Laberinto`:
- Crea `Habitaciones`, `Paredes` y `Puertas` y con `CreatorB` crea `ParedesBomba`.

###  Decorator
- El decorador principal es la clase `Bomba`, que es subclase de `Hoja` y `ElementoMapa` de las cuales heredamos el metodo `entrar()`.
- Permite modificar comportamiento de una bomba sin modificar la clase original.

### Strategy
- Lo utilizamos en la clase `Modo` y sus subclases `Agresivo` y `Perezoso`.
- Cada `Bicho` tiene un  `modo` para definir tanto la inicializacion de sus atributos como su comportamiento con los metodos `actua()`y `caminar()`.    

---

## Ejecuccion del programa

- He incluido un archivo `main.py` para poder ejecutar el programa y ver los resultados de forma similar al Playground de Smalltalk.
- Para ello hemos utilizados los diferentes métodos de la clase `Juego` para poder crear diferentes tipos de laberintos.
- El archivo es de libre interpretacion y puede ser ejecutado por cualquier persona a su gusto.
- El método `mostrar()` es el nuevo método implementado que se añadió en la clase `Habitacion` para mostrar
la estructura del laberinto en una forma similar a la de Smalltalk asi que recomiendo utilizarlo para ver el resultado de la creación del laberinto.



