def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                # Intercambio
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Ejemplo de uso
datos = [34, 12, 5, 67, 1, 89]
print("Lista original:", datos)
print("Lista ordenada (Burbuja):", bubble_sort(datos))
