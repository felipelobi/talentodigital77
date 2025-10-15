
print()
print("1. ACTUALIZAR VALORES EN DICCIONARIOS Y LISTAS")
print()

# Definir estructuras de datos originales
matriz = [[10, 15, 20], [3, 7, 14]]
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

print("ANTES de actualizar:")
print(f"Matriz: {matriz}")
print(f"Cantantes: {cantantes}")
print(f"Ciudades: {ciudades}")
print(f"Coordenadas: {coordenadas}\n")

# 1.1 Cambiar 3 por 6 en matriz
matriz[1][0] = 6

# 1.2 Cambiar nombre de primer cantante
cantantes[0]["nombre"] = "Enrique Martin Morales"

# 1.3 Cambiar "Cancún" por "Monterrey"
ciudades["México"][2] = "Monterrey"

# 1.4 Cambiar latitud
coordenadas[0]["latitud"] = 9.9355431

print("DESPUÉS de actualizar:")
print(f"Matriz: {matriz}")
print(f"Cantantes: {cantantes}")
print(f"Ciudades: {ciudades}")
print(f"Coordenadas: {coordenadas}\n")


print()
print("2. ITERAR A TRAVÉS DE UNA LISTA DE DICCIONARIOS")
print()

def iterarDiccionario(lista):
    for diccionario in lista:
        for clave, valor in diccionario.items():
            print(f"{clave} - {valor}", end="")
            # Agregar coma y espacio si no es el último elemento
            if clave != list(diccionario.keys())[-1]:
                print(", ", end="")
        print()

# Crear lista de cantantes
cantantes_lista = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

print("Llamada: iterarDiccionario(cantantes_lista)\n")
iterarDiccionario(cantantes_lista)
print()

print()
print("3. OBTENER VALORES DE UNA LISTA DE DICCIONARIOS")
print()

def iterarDiccionario2(llave, lista):
    """
    Recibe una cadena con el nombre de una clave y una lista de diccionarios.
    Imprime el valor almacenado para esa clave en cada diccionario.
    """
    for diccionario in lista:
        # Verificar si la clave existe en el diccionario
        if llave in diccionario:
            print(diccionario[llave])

print("Llamada: iterarDiccionario2('nombre', cantantes_lista)\n")
iterarDiccionario2("nombre", cantantes_lista)

print("\nLlamada: iterarDiccionario2('pais', cantantes_lista)\n")
iterarDiccionario2("pais", cantantes_lista)
print()

print()
print("4. ITERAR DICCIONARIO CON VALORES DE LISTA")
print()

def imprimirInformacion(diccionario):
    """
    Recibe un diccionario donde los valores son listas.
    Imprime el nombre de cada clave (en mayúsculas), el tamaño de su lista,
    y todos los elementos de esa lista.
    """
    for clave, lista in diccionario.items():
        print(f"{len(lista)} {clave.upper()}")
        for elemento in lista:
            print(elemento)
        
        print()

# Crear diccionario de Costa Rica
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

print("Llamada: imprimirInformacion(costa_rica)\n")
imprimirInformacion(costa_rica)
print()