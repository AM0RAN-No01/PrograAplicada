def merge(arr, l, m, r):
    """Función que mezcla (merge) dos subarreglos ordenados:
       arr[l..m] y arr[m+1..r] - equivalente a merge en C"""
    i = 0
    j = 0
    k = 0
    n1 = m - l + 1  # tamaño del subarreglo izquierdo
    n2 = r - m      # tamaño del subarreglo derecho

    # arreglos temporales
    L = [0] * n1
    R = [0] * n2

    # copiar datos a L[] y R[]
    for i in range(n1):
        L[i] = arr[l + i]

    for j in range(n2):
        R[j] = arr[m + 1 + j]

    # mezclar los subarreglos L[] y R[] en arr[l..r]
    i = 0      # índice inicial de L[]
    j = 0      # índice inicial de R[]
    k = l      # índice inicial de arr[]

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # copiar los elementos restantes de L[], si hay
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # copiar los elementos restantes de R[], si hay
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, l, r):
    """MergeSort recursivo - equivalente a mergeSort en C"""
    if l < r:
        m = l + (r - l) // 2  # punto medio (división entera)

        # ordenar primera y segunda mitad
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)

        # mezclar las dos mitades ordenadas
        merge(arr, l, m, r)

def main():
    """Función principal - equivalente a main en C"""
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)

    mergeSort(arr, 0, n - 1)

    print("Arreglo ordenado:")
    for i in range(n):
        print(arr[i], end=" ")
    print()

# Llamar a la función principal
if __name__ == "__main__":
    main()