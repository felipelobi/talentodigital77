def calcular_descuento():
    # Entrada de datos
    cantidad_productos = int(input("Ingrese la cantidad de productos comprados: "))
    cliente_frecuente = int(input("Ingrese el número de compras previas realizadas: "))
    monto_compra = float(input("Ingrese el monto total de la compra en dólares: "))
    promocion_especial = input("¿Es día de promoción especial? (s/n): ").lower().strip()

    # Inicialización de descuento
    descuento_total = 0.0

    # Lógica de descuentos
    if cantidad_productos > 10:
        descuento_total += 10

    if cliente_frecuente > 5:
        descuento_total += 5

    if monto_compra > 500:
        descuento_total += 7

    if promocion_especial == 's':
        descuento_total += 15

    # Aplicar límite máximo del 30%
    if descuento_total > 30:
        descuento_total = 30

    # Mostrar resultado
    print(f"\nDescuento aplicado: {descuento_total}%")
    print(f"Monto final a pagar: ${monto_compra * (1 - descuento_total / 100):.2f}")

# Ejecutar la función principal
if __name__ == "__main__":
    calcular_descuento()