# Diccionario de sensores con nombres de habitaciones y su respectiva temperatura
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22} 

# Diccionario de cámaras con el nombre del área y la cantidad de cámaras
num_cameras = {"backyard": 6, "garage": 2, "driveway": 1} 

# Muestra el diccionario de sensores
# print(sensors) 

# Muestra el diccionario de cámaras
# print(num_cameras) 

# Diccionario de traducciones de palabras en inglés a un lenguaje ficticio
translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch"} 

# Muestra el diccionario de traducciones
# print(translations) 

## Verificando un error con diccionarios: claves no válidas
# El siguiente código intenta usar listas como claves, pero esto generará un error porque las listas no son inmutables en Python y no pueden ser usadas como claves en diccionarios
# powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3} 

# Muestra el diccionario de poderes
# print(powers) 

# Diccionario de niños pertenecientes a dos familias
children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"], "Corleone": ["Sonny", "Fredo", "Michael"]} 

# Muestra el diccionario de niños
# print(children) 

# Diccionario vacío inicializado
my_empty_dictionary = {} 

# Muestra el diccionario vacío
# print(my_empty_dictionary) 

# Diccionario con el menú de desayuno y sus respectivos precios
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2} 

# Muestra el menú antes de agregar un nuevo ítem
# print("Before: ", menu) 

# Agrega un nuevo ítem al diccionario (cheesecake con precio 8)
menu["cheesecake"] = 8 

# Muestra el menú después de agregar el nuevo ítem
# print("After", menu) 

# Diccionario de animales en un zoológico, inicialmente vacío
animals_in_zoo = {"dinosaurs": 0} 

# Añade animales a un diccionario (por ejemplo, caballos)
animals_in_zoo = {"horses": 2} 

# Muestra el diccionario con los animales
# print(animals_in_zoo) 

## Agregar múltiples claves a un diccionario con el método `update()`
# El siguiente código agrega tres nuevas habitaciones con temperaturas
# sensors.update({"pantry": 22, "guest room": 25, "patio": 34})

# Muestra el diccionario de sensores después de agregar las habitaciones
# print("After", sensors) 

# Diccionario de IDs de usuarios
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238} 

# Muestra el diccionario de IDs de usuarios
# print(user_ids) 

# Actualiza el diccionario de IDs de usuarios con nuevos usuarios
user_ids.update({"theLooper": 138475, "stringQueen": 85739}) 

# Muestra el diccionario de IDs actualizado
# print(user_ids) 

## Sobrescribir valores de un diccionario
# Aquí se muestra cómo sobrescribir el valor de una clave existente
# La clave "oatmeal" se actualiza de 3 a 5
# menu["oatmeal"] = 5 

# Muestra el menú antes de la actualización
# print("Before: ", menu) 

# Muestra el menú después de la actualización
# print("After", menu) 

# Diccionario de ganadores de premios Oscar en diversas categorías
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"} 

# Muestra el diccionario de ganadores antes de actualizaciones
# print("Before", oscar_winners) 
# print() 

# Agrega una nueva categoría (Supporting Actress)
oscar_winners.update({"Supporting Actress": "Viola Davis"}) 

# Muestra el diccionario de ganadores después de agregar la nueva categoría
# print("After1", oscar_winners) 
# print() 

# Cambia el valor de la categoría "Best Picture" de "La La Land" a "Moonlight"
oscar_winners["Best Picture"] = "Moonlight" 

# Muestra el diccionario de ganadores después del cambio
# print("After2", oscar_winners) 

### Diccionarios con comprensión (Dict Comprehensions)
# Si tenemos dos listas, una de nombres de estudiantes y otra de alturas,
# podemos combinarlas en un diccionario usando la comprensión de diccionarios

# Listas de estudiantes y sus alturas
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

# Usamos la función zip() para combinar ambas listas en pares
zipStudents = zip(names, heights) 

# Muestra el resultado de la función zip
# print("zipStudents: ", zipStudents) 

# Creamos un diccionario a partir de esos pares utilizando dict comprehension
students = {key: value for key, value in zip(names, heights)} 

# Muestra el diccionario de estudiantes
# print(students) 

# La función zip() combina dos listas en un iterador de tuplas
# dict comprehension {clave: valor for clave, valor in zip(...)} crea un diccionario a partir de esas tuplas

# Otra aplicación de dict comprehension con listas de bebidas y su contenido de cafeína
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

# Usamos zip() para combinar las listas
zipped_drinks = zip(drinks, caffeine) 

# Muestra el resultado de la función zip para bebidas y cafeína
# print(zipped_drinks) 

# Creamos un diccionario de bebidas y su cafeína usando dict comprehension
drinks_to_caffeine = {key: value for key, value in zipped_drinks} 

# Muestra el diccionario de bebidas y cafeína
# print(drinks_to_caffeine) 

# ==============================
# Diccionarios en Python
# ==============================
# Creamos dos listas: canciones y cantidad de reproducciones
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

# Combina ambas listas en pares (canción, cantidad de reproducciones) usando zip()
# y crea un diccionario con dict comprehension
plays = {key: value for key, value in zip(songs, playcounts)} 

# Muestra el diccionario de canciones y reproducciones
print("diccionario inicial de plays:", plays) 

# Resultado esperado:
# {'Like a Rolling Stone': 78, 'Satisfaction': 29, 'Imagine': 44, 
#  'What's Going On': 21, 'Respect': 89, 'Good Vibrations': 5} 

# ======================================
# Agregar elementos a un diccionario
# ======================================
# Usamos el método .update() para agregar una nueva canción con su conteo de reproducciones
plays.update({"Purple Haze": 1}) 

# Ahora el diccionario tiene una nueva canción: "Purple Haze" con 1 reproducción
# Mostramos el diccionario después de la actualización
# print(plays)

# ======================================
# Modificar valores existentes
# ======================================
# Si usamos update() con una clave que ya existe, su valor se sobrescribe
plays.update({"Respect": 94}) 

# Antes "Respect": 89, ahora "Respect": 94
# Mostramos el diccionario después de la modificación
print("Despues de agregar y modificar: ", plays)

# Resultado esperado:
# {'Like a Rolling Stone': 78, 'Satisfaction': 29, 'Imagine': 44,
#  'What's Going On': 21, 'Respect': 94, 'Good Vibrations': 5, 'Purple Haze': 1} 

# ======================================
# Diccionarios anidados
# ======================================
# Podemos tener diccionarios dentro de diccionarios
# Aquí creamos un diccionario llamado "library" con canciones y un diccionario vacío para "Sunday Feelings"
library = {"The Best Songs": plays,  # Diccionario con todas las canciones y sus reproducciones
           "Sunday Feelings": {}}    # Diccionario vacío (puede llenarse más adelante)

# Muestra el diccionario anidado
# print("Diccionario anidado (library):", library)

# ==============================
# Resumen de métodos usados
# ==============================
# 1. zip(lista1, lista2) -> Une elementos en pares (tuplas).
# 2. {k:v for k,v in zip(...)} -> Crea un diccionario usando dict comprehension.
# 3. dict.update({clave: valor}) -> Agrega o modifica pares clave:
