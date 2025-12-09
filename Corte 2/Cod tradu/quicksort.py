def swap(a, b):
    """Intercambia dos números - equivalente a swap en C"""
    temp = a[0]
    a[0] = b[0]
    b[0] = temp

def partition(arr, low, high):
    """Particiona el arreglo usando el último elemento como pivote - equivalente a partition en C"""
    pivot = arr[high]   # elegimos el último elemento como pivote
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            # Usamos listas de un elemento para simular punteros
            swap([arr[i]], [arr[j]])

    swap([arr[i + 1]], [arr[high]])
    return i + 1   # nueva posición del pivote

def quickSort(arr, low, high):
    """Implementación recursiva de QuickSort - equivalente a quickSort en C"""
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)   # izquierda
        quickSort(arr, pi + 1, high)  # derecha

def printArray(arr, size):
    """Imprime un arreglo - equivalente a printArray en C"""
    for i in range(size):
        print(arr[i], end=" ")
    print()

def main():
    """Función principal - equivalente a main en C"""
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)

    print("Arreglo original:")
    printArray(arr, n)

    quickSort(arr, 0, n - 1)

    print("Arreglo ordenado:")
    printArray(arr, n)

# Llamar a la función principal
if __name__ == "__main__":
    main()