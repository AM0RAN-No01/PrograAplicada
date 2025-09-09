print("Verificador de números primos - Ctrl+C para salir")

try:
    while True:
        try:
            n = int(input("\nNúmero: "))
            
            if n <= 0:
                print("Solo números positivos")
                continue
                
            if n == 1:
                print("1 no es primo")
                continue
            
            primo = True
            for i in range(2, int(n**0.5)+1):
                if n % i == 0:
                    primo = False
                    break
            
            print("PRIMO" if primo else "NO primo")
            
        except ValueError:
            print("Ingresa un número válido")
            
except KeyboardInterrupt:
    print("\n¡Hasta pronto!")
#9/septiembre Clase 8-10 Am +1 DECIMA primer corte 
