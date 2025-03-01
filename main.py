# Importamos las clases necesarias
from main import Juego, Creator, CreatorB

# Crear una instancia de juego y un Creator por defecto
juego = Juego()
creator = Creator()

# Crear un laberinto con 2 habitaciones
laberinto_simple = juego.crear_laberinto_2_habitaciones()
print("Laberinto con 2 habitaciones")
laberinto_simple.mostrar()
print("Laberinto creado!")

laberinto3=juego.crear_laberinto_2_habitaciones_fm(creator)
print("Laberinto con 2 habitaciones usando Factory Method")
laberinto3.mostrar()
print("Laberinto creado!")

# Crear un laberinto con 4 habitaciones con bichos agresivos y perezosos
laberinto2=juego.crear_laberinto_4_habitaciones()
print("Laberinto con 4 habitaciones y bichos")
laberinto2.mostrar()
print("Laberinto creado!")

# Crear un laberinto usando Factory Method para generar paredes bomba
juego2 = Juego()
creator_b = CreatorB()
laberinto_bombas = juego2.crear_laberinto_2_habitaciones_fmd(creator_b)
print("Laberinto con paredes bomba")
laberinto_bombas.mostrar()
print("Laberinto con paredes bomba listo!")

#creamos un laberinto con 4 habitaciones y bichos con fm
juego3 = Juego()
creator2 = Creator()
laberinto_bichos = juego3.crear_laberinto_4_habitaciones_bichos_fm(creator2)
print("Laberinto con 4 habitaciones y bichos con fm")
laberinto_bichos.mostrar()
print("Laberinto creado")
