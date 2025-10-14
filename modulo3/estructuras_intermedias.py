matriz = [ [10, 15, 20], [3, 7, 14] ]

cantantes = [
   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
   {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
   "México": ["Ciudad de México", "Guadalajara", "Cancún"],
   "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
   {"latitud": 8.2588997, "longitud": -84.9399704}
]

costa_rica = {
   "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
   "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

print("1. ACTUALIZAR VALORES \n")

print("Estructuras ANTES de actualizar:")
print(f"Matriz: {matriz}")
print(f"Cantantes: {cantantes}")
print(f"Ciudades: {ciudades}")
print(f"Coordenadas: {coordenadas}\n")


# 1.1 Cambiar el valor 3 en matriz por 6
matriz[1][0] = 6

# 1.2 Cambiar el nombre del primer cantante
cantantes[0]["nombre"] = "Enrique Martin Morales"

# 1.3 Reemplazar "Cancún" por "Monterrey" en ciudades
ciudades["México"][2] = "Monterrey"

# 1.4 Cambiar la latitud en coordenadas
coordenadas[0]["latitud"] = 9.9355431

print("Estructuras DESPUÉS de actualizar:")
print(f"Matriz: {matriz}")
print(f"Cantantes: {cantantes}")
print(f"Ciudades: {ciudades}")
print(f"Coordenadas: {coordenadas}\n")


print("2. RECORRER LISTA DE DICCIONARIOS \n")

print("Recorrido:")
for cantante in cantantes:
    print(f"{cantante['nombre']} - {cantante['pais']}")

print("\nRecorrido BONUS:")
for cantante in cantantes:
    print(f"nombre - {cantante['nombre']}, pais - {cantante['pais']}")

print()

print("3. OBTENER VALORES ESPECÍFICOS \n")

print("Todos los nombres:")
for cantante in cantantes:
    print(cantante["nombre"])

print("\nTodos los países:")
for cantante in cantantes:
    print(cantante["pais"])
    
print()


print("4. RECORRER DICCIONARIO CON LISTAS COMO VALORES \n")


# Recorrer cada clave y su lista asociada
for clave, lista in costa_rica.items():
    print(f"{len(lista)} elementos en {clave.upper()}:")
    for elemento in lista:
        print(f"  - {elemento}")
    
    print()
    