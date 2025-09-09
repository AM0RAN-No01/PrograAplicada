print("el programa tiene como objetivo determinar si un numero ingrsado es par o impar, para finalizar el programa oprima Ctrl+c")

while True:
    try:
        # Solicitar número al usuario
        numero = input("\nIngresa un número: ")
        
        # Convertir a entero y verificar
        numero_int = int(numero)
        
        if numero_int % 2 == 0:
            print(f"El número {numero_int} es PAR")
        else:
            print(f"El número {numero_int} es IMPAR")
            
    except ValueError:
        print("Error: Por favor ingresa un número válido")
    
    except KeyboardInterrupt:
        print("\n\nPrograma finalizado con Ctrl+C. Hasta luego")
        break
    #9/septiembre Clase 8-10 am PONER DECIMA de primer corte
