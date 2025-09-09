print("el programa tiene como objetivo determinar si un numero ingrsado es par o impar, para finalizar el programa oprima Ctrl+c\n")
while True:
    try:
        numero = input("Ingresa un número entero: ")
        numero_int = int(numero)
        
        if numero_int % 2 == 0:
            print(f"PAR")
        else:
            print(f"IMPAR")
            
    except ValueError:
        print("Error: Ingresa solo números enteros")
    except KeyboardInterrupt:
        print("\n¡Adiós!")
        break
    #9/septiembre Clase 8-10 Am +1 DECIMA primer corte 
