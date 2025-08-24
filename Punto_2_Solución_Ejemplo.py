estados = ["ENCENDIDA" , "APAGADA"]

estado_actual = "APAGADA"
estado_meta = "ENCENDIDA"

def acciones_disponibles(estado):
    return ["PRENDER" , "APAGAR"]

def cambiar_estado(estado, accion):
    if accion == "PRENDER":
        return "ENCENDIDA"
    elif accion == "APAGAR":
        return "APAGADA"
print(f"Estado inicial: {estado_actual}")

accion = "PRENDER"
estado_actual = cambiar_estado(estado_actual, accion)
print(f"Después de {accion}: {estado_actual}")

if estado_actual == estado_meta:
    print("¡Meta alcanzada!")

    