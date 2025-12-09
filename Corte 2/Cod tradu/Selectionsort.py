def selectionSort(arr, n):
    """Implementación de Selection Sort - equivalente a selectionSort en C"""
    i = 0
    j = 0
    minIndex = 0
    temp = 0

    for i in range(n - 1):
        minIndex = i  # asumimos que el menor está en i

        # buscar el menor en el resto del arreglo
        for j in range(i + 1, n):
            if arr[j] < arr[minIndex]:
                minIndex = j

        # si encontramos un menor, intercambiamos
        if minIndex != i:
            temp = arr[i]
            arr[i] = arr[minIndex]
            arr[minIndex] = temp

def printArray(arr, n):
    """Imprime un arreglo - equivalente a printArray en C"""
    for i in range(n):
        print(arr[i], end=" ")
    print()

def main():
    """Función principal - equivalente a main en C"""
    arr = [5, 3, 6, 1, 4]
    n = len(arr)

    print("Arreglo original:")
    printArray(arr, n)

    selectionSort(arr, n)

    print("Arreglo ordenado:")
    printArray(arr, n)

# Llamar a la función principal
if __name__ == "__main__":
    main()