import random

def jugar():
    opciones = ['piedra', 'papel', 'tijeras']

    # El usuario elige una opción
    print("Elige una opción: piedra, papel o tijeras")
    eleccion_usuario = input().lower()

    # Verificar si la opción del usuario es válida
    while eleccion_usuario not in opciones:
        print("Opción no válida. Por favor, elige piedra, papel o tijeras")
        eleccion_usuario = input().lower()

    # La computadora elige una opción al azar
    eleccion_computadora = random.choice(opciones)

    # Mostrar las elecciones
    print("Tu elección:", eleccion_usuario)
    print("La elección de la computadora:", eleccion_computadora)

    # Determinar el resultado del juego
    if eleccion_usuario == eleccion_computadora:
        print("¡Empate!")
    elif (eleccion_usuario == 'piedra' and eleccion_computadora == 'tijeras') or \
         (eleccion_usuario == 'papel' and eleccion_computadora == 'piedra') or \
         (eleccion_usuario == 'tijeras' and eleccion_computadora == 'papel'):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")

# Función para agradecer al jugador
def agradecer():
    print("¡Gracias por jugar!")

# Función principal para iniciar el juego
def main():
    jugar()

    # Preguntar al usuario si desea volver a jugar
    while True:
        print("¿Quieres jugar de nuevo? (sí/no)")
        respuesta = input().lower()
        if respuesta != 'sí' and respuesta != 'si':
            break
        jugar()

    # Agradecer al jugador al salir del bucle
    agradecer()

if __name__ == "__main__":
    main()
