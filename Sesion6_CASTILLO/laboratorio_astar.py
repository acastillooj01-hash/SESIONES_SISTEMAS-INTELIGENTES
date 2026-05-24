import heapq

# Definición del Grafo y la Heurística
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

heuristica = {
    'A': 6, 'B': 4, 'C': 2, 'D': 3, 'E': 1, 'F': 0
}

# Implementación de A*
def a_star(inicio, objetivo):
    cola = [(0 + heuristica[inicio], 0, inicio)] # (f(n), g(n), nodo)
    costos = {inicio: 0}
    padres = {inicio: None}
    visitados = set()

    while cola:
        f_actual, g_actual, actual = heapq.heappop(cola)

        if actual in visitados:
            continue
        visitados.add(actual)

        if actual == objetivo:
            break

        for vecino, costo in grafo[actual]:
            nuevo_costo_g = costos[actual] + costo # g(n)
            
            if vecino not in costos or nuevo_costo_g < costos[vecino]:
                costos[vecino] = nuevo_costo_g
                f_total = nuevo_costo_g + heuristica[vecino] # f(n) = g(n) + h(n)
                heapq.heappush(cola, (f_total, nuevo_costo_g, vecino))
                padres[vecino] = actual

    # Reconstrucción del camino para que sea fácil de leer
    camino = []
    nodo = objetivo
    while nodo is not None:
        camino.append(nodo)
        nodo = padres.get(nodo)
    camino.reverse()
    
    return camino, costos.get(objetivo, float('inf'))

# Ejecutar búsqueda original
camino_original, costo_original = a_star('A', 'F')
print(f"Camino encontrado: {camino_original}")
print(f"Costo total del camino: {costo_original}")

# Modificamos la heurística para "asustar" al algoritmo de ir por la ruta C
heuristica['C'] = 10 

camino_mod, costo_mod = a_star('A', 'F')
print(f"NUEVO Camino modificando heurística: {camino_mod}")
print(f"NUEVO Costo total: {costo_mod}")

# Restauramos el valor original para la siguiente prueba
heuristica['C'] = 2

camino_desde_b, costo_desde_b = a_star('B', 'F')
print(f"Camino desde B hasta F: {camino_desde_b}")
print(f"Costo total desde B: {costo_desde_b}")