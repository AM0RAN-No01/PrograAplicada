# #### Get A Key
# # Puedes acceder a los valores de un diccionario proporcionando la clave.

# Definimos un diccionario con los edificios más altos y sus alturas en metros.
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}

# Se imprime la altura de "Burj Khalifa", que es 828 metros.
print(building_heights["Burj Khalifa"]) # Prints 828

# Se imprime la altura de "Ping An", que es 599 metros.
print(building_heights["Ping An"]) # Prints 599

# Definimos un diccionario que asocia elementos zodiacales con los signos correspondientes.
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

# Se imprime la lista de signos de "earth".
print(zodiac_elements["earth"])

# Se imprime la lista de signos de "fire".
print(zodiac_elements["fire"])

# ## Get an Invalid Key

# Aquí, intentamos acceder a una clave que no existe en el diccionario "building_heights".
# Esto generará un error KeyError si se ejecuta.
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}

# Esto generará un error porque "Landmark 81" no es una clave válida en el diccionario.
print(building_heights["Landmark 81"])

# ## Una forma de evitar este error es comprobar primero si la clave existe en el diccionario.
key_to_check = "Landmark 81"

# Si la clave "Landmark 81" existe en el diccionario, se imprime su valor.
if key_to_check in building_heights:
  print(building_heights["Landmark 81"])

# Ahora, añadimos una nueva clave llamada "energy" al diccionario "zodiac_elements" con un valor que no corresponde a un signo zodiacal.
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
zodiac_elements["energy"] = "Not a Zodiac element"

# Comprobamos si la clave "energy" existe en el diccionario, y si es así, la imprimimos.
if "energy" in zodiac_elements:
  print(zodiac_elements["energy"])

# ##Safely Get a Key
# Utilizando el método get() se puede obtener el valor de una clave sin riesgo de error, ya que no lanzará un error si la clave no existe.

# Definimos nuevamente el diccionario "building_heights".
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}

# Utilizamos el método get() para obtener el valor de "Shanghai Tower", que es 632.
# Este método es más seguro que usar corchetes, ya que no lanza un error si la clave no existe.
print(building_heights.get("Shanghai Tower"))

# Ahora intentamos obtener el valor de "My House", que no existe en el diccionario.
# El método get() devuelve None cuando la clave no se encuentra.
print(building_heights.get("My House"))

# Creamos un diccionario de "user_ids" con algunos identificadores de usuario.
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

# Comprobamos si el "teraCoder" está en el diccionario "user_ids" y asignamos un valor de ID.
# Si no está, se asigna un valor predeterminado (1000 en este caso).
tc_id = user_ids.get("teraCoder") if user_ids.get("teraCoder") else 1000

# Imprimimos el ID de "teraCoder".
print(tc_id)

# Comprobamos si "superStackSmash" existe en "user_ids".
# Si no, asignamos un valor predeterminado (100000 en este caso).
if user_ids.get("superStackSmash") == None:
    stack_id = 100000

# Imprimimos "stack_id".
print(stack_id)

# ###Delete a Key
# El método pop() elimina una clave específica y devuelve su valor. Si la clave no existe, puede proporcionar un valor predeterminado.

# Creamos un diccionario de premios de una rifa.
raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}

# Eliminamos la clave 320291, que corresponde a "Gift Basket", y la imprimimos.
print(raffle.pop(320291, "No Prize"))  # Prints "Gift Basket"

# Imprimimos el diccionario después de la eliminación.
print(raffle)  # Prints {223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}

# Intentamos eliminar una clave que no existe (100000). Se imprime el valor predeterminado "No Prize".
print(raffle.pop(100000, "No Prize"))  # Prints "No Prize"

# Imprimimos el diccionario después de la eliminación.
print(raffle)  # Prints {223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}

# Eliminamos la clave 872921, que corresponde a "Concert Tickets", y la imprimimos.
print(raffle.pop(872921, "No Prize"))  # Prints "Concert Tickets"

# Imprimimos el diccionario después de la eliminación.
print(raffle)  # Prints {223842: "Teddy Bear", 412123: "Necklace", 298787: "Pasta Maker"}

# Creamos un diccionario con objetos disponibles en un juego y puntos de salud.
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

# Aumentamos los puntos de salud utilizando el valor de "stamina grains" y "power stew" del diccionario, eliminándolos con pop().
health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)

# Intentamos añadir "mystic bread", que no está en el diccionario. El valor predeterminado es 0.
health_points += available_items.pop("mystic bread", 0)

# Imprimimos los objetos restantes y los puntos de salud actuales.
print(available_items)
print(health_points)

# ##Get All Keys
# Para obtener todas las claves de un diccionario, usamos el método keys().

# Creamos un diccionario con los puntajes de los estudiantes.
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}

# Imprimimos todas las claves (nombres de los estudiantes).
print(list(test_scores))  # Prints ["Grace", "Jeffrey", "Sylvia", "Pedro", "Martin", "Dina"]

# Recorremos las claves del diccionario y las imprimimos.
for student in test_scores.keys():
  print(student)

# Obtenemos las claves de "user_ids" y "num_exercises".
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

# Imprimimos las claves de ambos diccionarios.
users = user_ids.keys()
lessons = num_exercises.keys()

print(users)
print(lessons)

##Get All Values
# Para obtener todos los valores de un diccionario, usamos el método values().

# Recorremos y mostramos los valores de "test_scores".
for score_list in test_scores.values():
  print(score_list)

# Calculamos el total de ejercicios en el diccionario "num_exercises".
total_exercises = 0
for exercises in num_exercises.values
