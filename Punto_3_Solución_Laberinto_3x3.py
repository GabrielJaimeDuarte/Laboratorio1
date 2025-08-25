from collections import deque

# -------------------------
# Laberinto 3x3 con BFS
# -------------------------

# Tamaño del mundo
N = 3  

# Inicio y meta
estado_inicial = (0, 0)
estado_meta = (2, 2)

# Obstáculos
obstaculos = [(1,1)]   # ejemplo: bloqueamos el centro

# Acciones disponibles con sus movimientos
acciones = {
    "ARRIBA": (-1, 0),
    "ABAJO": (1, 0),
    "IZQUIERDA": (0, -1),
    "DERECHA": (0, 1)
}

# Función para mover al agente
def mover(estado, accion):
    x, y = estado
    dx, dy = acciones[accion]
    nuevo_estado = (x + dx, y + dy)

    # Validar que esté dentro del tablero y no en obstáculo
    if 0 <= nuevo_estado[0] < N and 0 <= nuevo_estado[1] < N:
        if nuevo_estado not in obstaculos:
            return nuevo_estado
    return None  # movimiento inválido

# Algoritmo BFS para encontrar el camino más corto
def bfs(inicio, meta):
    cola = deque([(inicio, [])])
    visitados = set()

    while cola:
        estado, camino = cola.popleft()
        if estado == meta:
            return camino + [estado]

        if estado in visitados:
            continue
        visitados.add(estado)

        for accion in acciones:
            nuevo_estado = mover(estado, accion)
            if nuevo_estado and nuevo_estado not in visitados:
                cola.append((nuevo_estado, camino + [estado]))

    return None  # no hay camino

# Ejecutar búsqueda
solucion = bfs(estado_inicial, estado_meta)

# Mostrar solución paso a paso
if solucion:
    print("Camino encontrado hasta la meta 🎯:")
    for paso in solucion:
        print(paso)
else:
    print("No hay camino disponible 🚧")
