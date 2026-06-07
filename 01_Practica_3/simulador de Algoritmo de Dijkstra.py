import heapq

def dijkstra(grafo, inicio):
    # Distancias iniciales: infinito para todos excepto el nodo de inicio
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    visitados = set()
    cola = [(0, inicio)]

    paso = 1
    while cola:
        distancia_actual, nodo_actual = heapq.heappop(cola)

        if nodo_actual in visitados:
            continue
        visitados.add(nodo_actual)

        print(f"Paso {paso}: Visitando {nodo_actual} con distancia {distancia_actual}")
        paso += 1

        for vecino, peso in grafo[nodo_actual].items():
            nueva_distancia = distancia_actual + peso
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                heapq.heappush(cola, (nueva_distancia, vecino))
                print(f"  -> Actualizando distancia de {vecino} a {nueva_distancia}")

    return distancias

# Ejemplo de grafo
grafo = {
    'A': {'B': 4, 'C': 2},
    'B': {'C': 5, 'D': 10},
    'C': {'E': 3},
    'D': {},
    'E': {'D': 4}
}

resultado = dijkstra(grafo, 'A')
print("\nDistancias finales:", resultado)
