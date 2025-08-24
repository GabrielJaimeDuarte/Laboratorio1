estados = ["CONTENTA" , "TRISTE"]

estado_actual = "TRISTE"
estado_meta = "CONTENTA"

def acciones_disponibles(estado):
    return ["RECIBIR UN PREMIO" , "NO RECIBE PREMIO"]

def cambiar_estado(estado, accion):
    if accion == "RECIBIR UN PREMIO":
        return "CONTENTA"
    elif accion == "TRISTE":
        return "TRISTE"
print(f"Estado inicial de la Mascota es: {estado_actual}")

accion = "RECIBIR UN PREMIO"
estado_actual = cambiar_estado(estado_actual, accion)
print(f"Después de {accion}, ahora esta: {estado_actual}")

if estado_actual == estado_meta:
    print("¡Meta alcanzada!")

    