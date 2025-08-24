
estado_inicial = (0, 0)
estado_meta = (2, 2)

def acciones_disponibles(estado):
    return ["ARRIBA", "ABAJO", "DERECHA", "IZQUIERDA"]

def cambiar_estado(estado, accion):
    x, y = estado
    if accion == "ARRIBA" and x > 0:
        return (x - 1, y)
    elif accion == "ABAJO" and x < 2:
        return (x + 1, y)
    elif accion == "DERECHA" and y < 2:
        return (x, y + 1)
    elif accion == "IZQUIERDA" and y > 0:
        return (x, y - 1)
    return estado  

estado_actual = estado_inicial
print(f"El pirata inicia en la posición: {estado_actual}")

secuencia_acciones = ["ABAJO", "ABAJO", "DERECHA", "DERECHA"]

for accion in secuencia_acciones:
    estado_actual = cambiar_estado(estado_actual, accion)
    print(f"Después de moverse {accion}, está en: {estado_actual}")

if estado_actual == estado_meta:
    print("¡El pirata encontró el tesoro!")

