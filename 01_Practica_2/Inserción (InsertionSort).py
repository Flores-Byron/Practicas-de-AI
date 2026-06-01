def insertion_sort(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista

# Ejemplo de uso
datos = [23, 4, 15, 8, 42, 16]
print("Lista original:", datos)
print("Lista ordenada (Inserción):", insertion_sort(datos))
