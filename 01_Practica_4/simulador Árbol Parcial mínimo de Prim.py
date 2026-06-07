import heapq

def prim(grafo, inicio):
    visitados = set([inicio])
    aristas = [
        (peso, inicio, vecino) for vecino, peso in grafo[inicio].items()
    ]
    heapq.heapify(aristas)

    mst = []
    costo_total = 0
    paso = 1

    while aristas:
        peso, u, v = heapq.heappop(aristas)
        if v not in visitados:
            visitados.add(v)
            mst.append((u, v, peso))
            costo_total += peso
            print(f"Paso {paso}: Añadiendo arista ({u}-{v}) con peso {peso}")
            paso += 1

            for vecino, peso_vecino in grafo[v].items():
                if vecino not in visitados:
                    heapq.heappush(aristas, (peso_vecino, v, vecino))

    print("\nÁrbol Parcial Mínimo (MST):", mst)
    print("Costo total:", costo_total)
    return mst, costo_total

# Ejemplo de grafo
grafo = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 4},
    'C': {'A': 3, 'B': 1, 'D': 5, 'E': 6},
    'D': {'B': 4, 'C': 5, 'E': 7},
    'E': {'C': 6, 'D': 7}
}

mst, costo = prim(grafo, 'A')
