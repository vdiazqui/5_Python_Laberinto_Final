# Laberinto_1

## Laberinto y Búsqueda de Camino
Este código Python resuelve el problema de encontrar un camino en un laberinto desde la esquina superior izquierda hasta la esquina inferior derecha. El laberinto se representa como una matriz bidimensional donde ' ' denota un camino libre y 'X' representa un muro.

### Instrucciones
#### Definir el Laberinto:
Se especifican las coordenadas de las casillas con muro utilizando una tupla llamada muro.
El número de filas y columnas del laberinto se establece en las variables filas y columnas.
Se crea el laberinto inicializando una lista de listas, donde todas las casillas comienzan como espacios en blanco.
#### Búsqueda del Camino:
La función encontrar_camino toma el laberinto como entrada y utiliza una pila para realizar una búsqueda en profundidad.
Comienza desde la esquina superior izquierda y explora las direcciones posibles (Abajo, Derecha, Arriba, Izquierda) hasta llegar a la esquina inferior derecha.
La función devuelve una lista de movimientos que representan el camino encontrado.
Este código imprimirá el laberinto y, si existe un camino desde la entrada hasta la salida, mostrará la secuencia de movimientos.
