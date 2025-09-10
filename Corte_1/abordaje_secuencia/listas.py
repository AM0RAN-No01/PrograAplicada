#LISTAS#

my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']  # Se define una lista con varios colores
print(my_lista)  # Imprime la lista completa
print(type(my_lista))  # Imprime el tipo de la variable (será 'list')
print(my_lista[2])  # Imprime el elemento en el índice 2 (comienza desde 0)

print("my_lista size: ", len(my_lista))  # Imprime el tamaño de la lista
print(my_lista[0:2])  # Imprime una porción de la lista desde el índice 0 hasta el 2 (sin incluir 2)
print(my_lista[:2])  # Imprime una porción de la lista desde el inicio hasta el índice 2 (sin incluir 2)

my_lista.append('Blanco')  # Agrega 'Blanco' al final de la lista
print(my_lista)  # Imprime la lista actualizada

my_lista.insert(3, 'Negro')  # Inserta 'Negro' en la posición 3 de la lista
print(my_lista)  # Imprime la lista después de la inserción

my_lista.extend(['Marron', 'Gris'])  # Extiende la lista con los elementos 'Marron' y 'Gris'
print(my_lista)  # Imprime la lista actualizada

print(my_lista.index('Azul'))  # Imprime el índice del primer elemento 'Azul' encontrado

# my_lista.remove('Magenta')  # Esto causaría un error, ya que 'Magenta' no está en la lista
my_lista.remove('Marron')  # Elimina el primer elemento 'Marron' encontrado
print(my_lista)  # Imprime la lista después de la eliminación

# 'Magenta' no está en la lista, descomentar causaría un error
# my_lista.remove('Magenta')

my_lista.insert(8, 'Marron')  # Vuelve a insertar 'Marron' en la posición 8
print(my_lista)  # Imprime la lista después de la inserción

print(my_lista.pop())  # Elimina y devuelve el último elemento de la lista
size = len(my_lista)  # Calcula el tamaño de la lista
print("size = ", size)  # Imprime el tamaño de la lista

# 'pop(size)' causaría un error si 'size' es mayor al índice máximo
# print(my_lista.pop(size))  # Esto causaría un error si 'size' es mayor al índice

my_lista_3 = my_lista*3  # Multiplica la lista por 3, creando una nueva lista con 3 repeticiones
print("my_lista_3: ", my_lista_3)  # Imprime la lista repetida

print("Sort:")  # Muestra un encabezado
print()  # Salto de línea
my_listaSort = my_lista.sort()  # Ordena la lista 'my_lista' en su lugar (no devuelve nada)
print(my_listaSort)  # Imprime 'None' porque 'sort()' no devuelve un valor

my_NumList = [10, 9, 8, 7, 6 , 5 , 4, 3, 2, 1]  # Define una lista de números
print("Ordering my_NumList: ")  # Imprime un encabezado
my_NumList.sort()  # Ordena la lista de números de menor a mayor
print(my_NumList)  # Imprime la lista ordenada

# Ordena la lista 'my_NumList' de mayor a menor
my_NumList.sort(reverse=True)  # Ordena la lista en orden descendente
print("De mayor a menor: ", my_NumList)  # Imprime la lista ordenada de mayor a menor

#################TUPLAS####################
###########################################

# Las tuplas son estructuras similares a las listas, pero son inmutables (no se pueden modificar después de creadas)

print("###########################")  # Encabezado
print("###########################")  # Encabezado
print("###########################")  # Encabezado
print("############TUPLAS#########")  # Encabezado
my_tupla = tuple(my_lista)  # Convierte la lista 'my_lista' en una tupla llamada 'my_tupla'
print()  # Salto de línea
print("my_tuple: ", my_tupla)  # Imprime la tupla

print(my_tupla[0])  # Imprime el primer elemento de la tupla
print(my_tupla[2])  # Imprime el tercer elemento de la tupla

print('Rojo' in my_tupla)  # Verifica si 'Rojo' está en la tupla (devuelve un valor booleano)
print(my_tupla.count('Rojo'))  # Cuenta cuántas veces aparece 'Rojo' en la tupla

# Tupla con un solo elemento, nota que falta la coma al final para que sea una tupla
my_tupla_unitaria = ('Blanco')  # Esto no es una tupla, es solo un string
print(my_tupla_unitaria)  # Imprime el valor de 'my_tupla_unitaria'

# Empaquetado de tupla: sin paréntesis, la tupla se puede definir con valores separados por comas
my_tupla = 'Gaspar', 5, 8, 1999  # Crea una tupla sin paréntesis
print(my_tupla)  # Imprime la tupla

# Desempaquetado de tupla: asigna cada valor de la tupla a una variable correspondiente
nombre, dia, mes, año = my_tupla  # Asigna los valores de la tupla a variables
print(nombre)  # Imprime 'nombre'
print(dia)  # Imprime 'dia'
print(mes)  # Imprime 'mes'
print(año)  # Imprime 'año'

# Imprime los valores de la tupla de forma más legible
print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", año)

# Convierte la tupla 'my_tupla' en una lista y la imprime
my_lista2 = list(my_tupla)  # Convierte la tupla en una lista
print(my_lista2)  # Imprime la lista convertida
