
N = 2  


estado_inicial = (0, 0)
estado_meta = (0, 1)


obstaculos = []


acciones = {
    "DERECHA": (0, 1),
    "ABAJO": (1, 0)
}

def mover(estado, accion):
    x, y = estado
    dx, dy = acciones[accion]
    nuevo_estado = (x + dx, y + dy)

    if 0 <= nuevo_estado[0] < N and 0 <= nuevo_estado[1] < N:
        if nuevo_estado not in obstaculos:
            return nuevo_estado
    return estado  

estado_actual = estado_inicial
print(f"Inicio en: {estado_actual}")


estado_actual = mover(estado_actual, "DERECHA")
print(f"Después de moverse DERECHA: {estado_actual}")


if estado_actual == estado_meta:
    print("¡Meta alcanzada en (0,1)!")



obstaculos = [(0,1)]
estado_actual = estado_inicial
print("\nProbando con obstáculo en (0,1)")
estado_actual = mover(estado_actual, "DERECHA")
print(f"Intento moverse DERECHA: {estado_actual}")

if estado_actual == estado_meta:
    print("¡Meta alcanzada!")
else:
    print("El camino está bloqueado")
