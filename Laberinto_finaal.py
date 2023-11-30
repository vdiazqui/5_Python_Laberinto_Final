# Tupla con las coordenadas de las casillas donde hay muro
muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))

# Número de filas y columnas del laberinto
filas = 5
columnas = 5

# Creamos una lista de listas que será nuestro laberinto y todas las casillas empiezan en blanco
laberinto = [[' ' for _ in range (columnas)] for _ in range (filas)]

# Asignamos que en cada coordenada de nuestra lista muro ponga x
for coordenada in muro:
    fila, columna = coordenada
    laberinto[fila][columna] = 'X'

#Imprimimos nuestro laberinto
for fila in laberinto:
    print(' '.join(fila))

def encontrar_camino(laberinto):
    filas = len(laberinto)
    columnas = len(laberinto[0])

    # Coordenadas de la entrada y salida
    entrada = (0, 0)
    salida = (filas - 1, columnas - 1)

    # Pila para almacenar la información del camino
    pila = [((0, 0), [])]

    while pila:
        (fila, columna), camino_actual = pila.pop()

        # Verificar si hemos llegado a la salida
        if (fila, columna) == salida:
            return camino_actual

        # Marcar la celda actual como visitada
        laberinto[fila][columna] = 'V'

        # Explorar las direcciones posibles: Abajo, Derecha, Arriba, Izquierda
        direcciones = [(1, 0, 'Abajo'), (0, 1, 'Derecha'), (-1, 0, 'Arriba'), (0, -1, 'Izquierda')]

        for df, dc, direccion in direcciones:
            nueva_fila, nueva_columna = fila + df, columna + dc

            # Verificar si la nueva posición está dentro del laberinto y no es un muro ni ha sido visitada
            if (
                0 <= nueva_fila < filas
                and 0 <= nueva_columna < columnas
                and laberinto[nueva_fila][nueva_columna] not in ('X', 'V')
            ):
                # Agregar la dirección actual al camino
                nuevo_camino = camino_actual + [direccion]

                # Agregar la nueva posición y el nuevo camino a la pila
                pila.append(((nueva_fila, nueva_columna), nuevo_camino))

    # Si no se encuentra un camino
    return None

laberinto = [
    [' ', 'X', 'X', 'X', 'X'],
    [' ', 'X', ' ', ' ', ' '],
    [' ', 'X', ' ', 'X', ' '],
    [' ', ' ', ' ', 'X', ' '],
    ['X', 'X', 'X', 'X', 'S']
]

camino = encontrar_camino(laberinto)

# Finalmente, imprimimos el resultado
if camino:
    print("Camino encontrado:")
    print(camino)
else:
    print("No hay camino encontrado.")

