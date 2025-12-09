def insertionSort(arr, n):
    """Implementación de Insertion Sort - equivalente a insertionSort en C"""
    i = 0
    key = 0
    j = 0

    for i in range(1, n):
        key = arr[i]      # valor que vamos a insertar
        j = i - 1

        # mover los elementos mayores que key hacia la derecha
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # insertar la key en el hueco que quedó
        arr[j + 1] = key

def printArray(arr, n):
    """Imprime un arreglo - equivalente a printArray en C"""
    for i in range(n):
        print(arr[i], end=" ")
    print()

def main():
    """Función principal - equivalente a main en C"""
    arr = [5, 2, 4, 6, 1]
    n = len(arr)

    print("Arreglo original:")
    printArray(arr, n)

    insertionSort(arr, n)

    print("Arreglo ordenado:")
    printArray(arr, n)

# Llamar a la función principal
if __name__ == "__main__":
    main()