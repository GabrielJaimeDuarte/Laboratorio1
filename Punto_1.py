import heapq

estado_final = [[1, 2, 3],
                [8, 0, 4],
                [7, 6, 5]]

estado_inicial = [[2, 8, 3],
                  [1, 6, 4],
                  [7, 0, 5]]

def convertir_a_tuple(estado):
    return tuple(num for fila in estado for num in fila)

def heuristica_manhattan(estado):
    distancia = 0
    for i in range(3):
        for j in range(3):
            valor = estado[i][j]
            if valor != 0:  # ignoramos el hueco
                pos_i, pos_j = divmod(estado_final_lineal.index(valor), 3)
                distancia += abs(i - pos_i) + abs(j - pos_j)
    return distancia

def encontrar_hueco(estado):
    for i in range(3):
        for j in range(3):
            if estado[i][j] == 0:
                return i, j

def generar_vecinos(estado):
    vecinos = []
    x, y = encontrar_hueco(estado)
    movimientos = [(-1,0),(1,0),(0,-1),(0,1)]  
    for dx, dy in movimientos:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            nuevo_estado = [fila[:] for fila in estado]
            # intercambiar hueco con la ficha
            nuevo_estado[x][y], nuevo_estado[nx][ny] = nuevo_estado[nx][ny], nuevo_estado[x][y]
            vecinos.append(nuevo_estado)
    return vecinos

def resolver(estado_inicial):
    lista_abierta = []
    heapq.heappush(lista_abierta, (0, estado_inicial, []))
    visitados = set()

    while lista_abierta:
        costo, estado, camino = heapq.heappop(lista_abierta)
        estado_tuple = convertir_a_tuple(estado)

        if estado == estado_final:
            return camino + [estado]

        if estado_tuple in visitados:
            continue
        visitados.add(estado_tuple)

        for vecino in generar_vecinos(estado):
            heapq.heappush(lista_abierta, (
                len(camino) + 1 + heuristica_manhattan(vecino),
                vecino,
                camino + [estado]
            ))

    return None

estado_final_lineal = [num for fila in estado_final for num in fila]

solucion = resolver(estado_inicial)

if solucion:
    print("Solución encontrada en", len(solucion)-1, "movimientos:")
    for paso in solucion:
        for fila in paso:
            fila_str = ["h" if x == 0 else str(x) for x in fila]  
            print(fila_str)
        print()
