def bubbleSort(arr, n):
    """Implementación de Bubble Sort - equivalente a bubbleSort en C"""
    i = 0
    j = 0
    temp = 0
    
    for i in range(n - 1):                    # FOR EXTERNO
        for j in range(n - i - 1):            # FOR INTERNO
            if arr[j] > arr[j + 1]:           # CONDICIÓN DE INTERCAMBIO
                temp = arr[j]                 # INTERCAMBIO
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

def printArray(arr, n):
    """Imprime un arreglo - equivalente a printArray en C"""
    i = 0
    for i in range(n):
        print(arr[i], end=" ")
    print()

def main():
    """Función principal - equivalente a main en C"""
    arr = [5, 1, 4, 2, 8]
    n = len(arr)
    print(f"Tamaño del arreglo: {n}")

    print("Arreglo original:")
    printArray(arr, n)

    bubbleSort(arr, n)

    print("Arreglo ordenado:")
    printArray(arr, n)

# Llamar a la función principal
if __name__ == "__main__":
    main()