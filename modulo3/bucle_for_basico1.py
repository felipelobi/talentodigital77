
def ejercicio_basico():
    """Imprime todos los números enteros del 0 al 100"""
    print("=== 1. Números del 0 al 100 ===")
    for i in range(101):
        print(i)

def ejercicio_multiplos_2():
    """Imprime todos los números múltiplos de 2 entre 2 y 500"""
    print("\n=== 2. Múltiplos de 2 entre 2 y 500 ===")
    for i in range(2, 501, 2):
        print(i)

def ejercicio_vanilla_ice():
    """Imprime números del 1 al 100 con reemplazos especiales"""
    print("\n=== 3. Contando Vanilla Ice ===")
    for i in range(1, 101):
        if i % 10 == 0:
            print("baby")
        elif i % 5 == 0:
            print("ice ice")
        else:
            print(i)

def ejercicio_suma_gigante():
    """Suma los números pares del 0 al 500,000"""
    print("\n=== 4. Número gigante a la vista!! ===")
    suma_pares = 0
    for i in range(0, 500001, 2):
        suma_pares += i
    print(f"La suma total es: {suma_pares}")

def ejercicio_regresame_3():
    """Imprime números positivos en cuenta regresiva de 3 en 3"""
    print("\n=== 5. Regrésame al 3 ===")
    inicio = int(input("Ingresa el número inicial para la cuenta regresiva: "))
    print(f"Cuenta regresiva desde {inicio} restando 3:")
    for i in range(inicio, 0, -3):
        if i > 0:
            print(i)

def ejercicio_contador_dinamico():
    """Imprime múltiplos dentro de un rango específico"""
    print("\n=== 6. Contador dinámico ===")
    numInicial = int(input("Ingresa el número inicial: "))
    numFinal = int(input("Ingresa el número final: "))
    multiplo = int(input("Ingresa el múltiplo: "))
    
    print(f"Números múltiplos de {multiplo} entre {numInicial} y {numFinal}:")
    for i in range(numInicial, numFinal + 1):
        if i % multiplo == 0:
            print(i)


def menu_principal():
    """MENU: Selecciona el ejercicio que quieres ejecutar"""
    while True:
        print("\n" + "="*50)
        print("           MENÚ PRINCIPAL - BUCLES FOR")
        print("="*50)
        print("1. Básico (0-100)")
        print("2. Múltiplos de 2")
        print("3. Vanilla Ice")
        print("4. Suma gigante de pares")
        print("5. Regrésame al 3")
        print("6. Contador dinámico")
        print("0. Salir")
        print("="*50)
        
        opcion = input("Selecciona un ejercicio (0-6): ")
        
        if opcion == "1":
            ejercicio_basico()
        elif opcion == "2":
            ejercicio_multiplos_2()
        elif opcion == "3":
            ejercicio_vanilla_ice()
        elif opcion == "4":
            ejercicio_suma_gigante()
        elif opcion == "5":
            ejercicio_regresame_3()
        elif opcion == "6":
            ejercicio_contador_dinamico()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona 0-6.")
        
        input("\nPresiona Enter para continuar...")

# Ejecutar el programa
if __name__ == "__main__":
    menu_principal()