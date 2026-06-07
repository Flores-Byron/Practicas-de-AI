class UnionFind:
    def __init__(self, nodos):
        self.padre = {nodo: nodo for nodo in nodos}
        self.rango = {nodo: 0 for nodo in nodos}

    def find(self, nodo):
        if self.padre[nodo] != nodo:
            self.padre[nodo] = self.find(self.padre[nodo])
        return self.padre[nodo]

    def union(self, nodo1, nodo2):
        raiz1, raiz2 = self.find(nodo1), self.find(nodo2)
        if raiz1 == raiz2:
            return False
        if self.rango[raiz1] < self.rango[raiz2]:
            self.padre[raiz1] = raiz2
        elif self.rango[raiz1] > self.rango[raiz2]:
            self.padre[raiz2] = raiz1
        else:
            self.padre[raiz2] = raiz1
            self.rango[raiz1] += 1
        return True

def kruskal(nodos, aristas, modo="minimo"):
    # Ordenar aristas por peso (ascendente para mínimo, descendente para máximo)
    aristas_ordenadas = sorted(aristas, key=lambda x: x[2], reverse=(modo=="maximo"))
    uf = UnionFind(nodos)
    mst = []
    costo_total = 0
    paso = 1

    for u, v, peso in aristas_ordenadas:
        if uf.union(u, v):
            mst.append((u, v, peso))
            costo_total += peso
            print(f"Paso {paso}: Añadiendo arista ({u}-{v}) con peso {peso}")
            paso += 1

    print(f"\nÁrbol de {'Máximo' if modo=='maximo' else 'Mínimo'} coste (Kruskal): {mst}")
    print("Costo total:", costo_total)
    return mst, costo_total

# Ejemplo de uso
nodos = ['A', 'B', 'C', 'D', 'E']
aristas = [
    ('A', 'B', 2),
    ('A', 'C', 3),
    ('B', 'C', 1),
    ('B', 'D', 4),
    ('C', 'D', 5),
    ('C', 'E', 6),
    ('D', 'E', 7)
]

print("=== Árbol de Mínimo Coste ===")
mst_min, costo_min = kruskal(nodos, aristas, modo="minimo")

print("\n=== Árbol de Máximo Coste ===")
mst_max, costo_max = kruskal(nodos, aristas, modo="maximo")
