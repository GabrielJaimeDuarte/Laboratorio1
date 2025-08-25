Laboratorio 1: Resolución de Problemas con Espacios de Estados y Algoritmos de Búsqueda

Este repositorio contiene las soluciones en Python para los problemas del Laboratorio 1, que se centra en la implementación de algoritmos utilizando espacios de estados, acciones y estrategias de búsqueda. Los problemas incluyen la resolución del 8-puzzle, el modelado de sistemas simples como una lámpara, una mascota virtual y la búsqueda de un tesoro por un pirata, y la navegación en laberintos de 2x2 y 3x3.

1. Solucionador del 8-Puzzle
Archivo: Punto_1.py

Descripción: Implementa un algoritmo de búsqueda A* para resolver el problema del 8-puzzle. Este problema consiste en deslizar fichas numeradas en una cuadrícula de 3x3 para transformar una configuración inicial en una configuración final. El algoritmo utiliza la heurística de la distancia de Manhattan para guiar la búsqueda.

Estado Inicial:
[[2, 8, 3],
[1, 6, 4],
[7, 0, 5]]

Estado Final:
[[1, 2, 3],
 [8, 0, 4],
 [7, 6, 5]]

Características Principales:
Utiliza una cola de prioridad (heapq) para la búsqueda A*.
Calcula la distancia de Manhattan como heurística.
Genera estados vecinos válidos moviendo la casilla vacía (0).
Muestra el camino paso a paso hacia la solución.

Cómo Ejecutar:
python Punto_1.py


2. Sistemas Basados en Espacios de Estados y Acciones
Esta sección incluye tres problemas que modelan sistemas simples utilizando espacios de estados, acciones y transiciones de estado.

2.1 Problema de la Lámpara
Archivo: Punto_2_Solución_Ejemplo.py
Descripción: Modela una lámpara que puede estar en dos estados: ENCENDIDA o APAGADA. El objetivo es pasar de APAGADA a ENCENDIDA utilizando la acción PRENDER.

Características Principales:
Define estados, acciones y una función de transición de estado.
Simula el cambio de estado y verifica si se alcanza el estado meta.

Cómo Ejecutar:
python Punto_2_Solución_Ejemplo.py

2.2 Mascota Virtual
Archivo: Punto_2_Solución_Mascota.py
Descripción: Modela una mascota virtual que puede estar CONTENTA o TRISTE. El objetivo es hacerla feliz dándole una recompensa (RECIBIR UN PREMIO).

Características Principales:
Estructura similar al problema de la lámpara, con estados y acciones definidos.
Transiciona la mascota de TRISTE a CONTENTA mediante una recompensa.

Cómo Ejecutar:
python Punto_2_Solución_Mascota.py

2.3 Búsqueda del Tesoro del Pirata
Archivo: Punto_2_Solución_Pirata.py

Descripción: Modela un pirata que navega en una cuadrícula de 3x3 desde la posición (0,0) para encontrar un tesoro en (2,2). Puede moverse hacia arriba, abajo, izquierda o derecha (ARRIBA, ABAJO, IZQUIERDA, DERECHA).

Características Principales:
Utiliza una representación de estado basada en coordenadas.
Aplica una secuencia predefinida de acciones para alcanzar la meta.
Valida los movimientos para mantenerse dentro de la cuadrícula.

Cómo Ejecutar:
python Punto_2_Solución_Pirata.py

3. Navegación en Laberintos
Esta sección incluye dos problemas de laberintos, uno para una cuadrícula de 2x2 y otro para una de 3x3.

3.1 Laberinto 2x2
Archivo: Punto_3_Solución_Laberinto_2x2.py
Descripción: Implementa la navegación en una cuadrícula de 2x2 desde (0,0) hasta (0,1) con las acciones DERECHA y ABAJO. Prueba dos escenarios: uno sin obstáculos y otro con un obstáculo en (0,1).

Características Principales:
Función de transición de estado simple para manejar movimientos.
Verifica obstáculos y límites de la cuadrícula.
Demuestra el efecto de un obstáculo que bloquea la meta.

Cómo Ejecutar:
python Punto_3_Solución_Laberinto_2x2.py

3.2 Laberinto 3x3 con BFS
Archivo: Punto_3_Solución_Laberinto_3x3.py

Descripción: Utiliza la búsqueda en anchura (BFS) para encontrar el camino más corto en una cuadrícula de 3x3 desde (0,0) hasta (2,2) con un obstáculo en (1,1). Soporta cuatro acciones: ARRIBA, ABAJO, IZQUIERDA, DERECHA.

Características Principales:
Implementa BFS usando una cola (deque) para explorar estados.
Registra estados visitados para evitar ciclos.
Muestra el camino paso a paso hacia la meta o indica si no hay camino.

Cómo Ejecutar:
Python Punto_3_Solución_Laberinto_3x3.py

