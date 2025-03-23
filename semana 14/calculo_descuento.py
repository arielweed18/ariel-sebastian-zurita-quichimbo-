# Función que calcula el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento


# Función que muestra el resumen de la compra
def mostrar_resumen(monto_total, porcentaje_descuento=10):
    descuento = calcular_descuento(monto_total, porcentaje_descuento)
    total_pagar = monto_total - descuento
    print("--------------- RESUMEN DE COMPRA ---------------")
    print(f"Monto total de la compra: ${monto_total}")
    print(f"Porcentaje de descuento aplicado: {porcentaje_descuento}%")
    print(f"Descuento obtenido: ${descuento}")
    print(f"Total a pagar después del descuento: ${total_pagar}")
    print("------------------------------------------------\n")


# Programa principal
def main():
    # Primera llamada (usando el porcentaje por defecto)
    monto1 = 1200
    mostrar_resumen(monto1)

    # Segunda llamada (con porcentaje indicado por el usuario)
    monto2 = 2000
    porcentaje2 = 20
    mostrar_resumen(monto2, porcentaje2)

    # Llamadas opcionales: permitir que el usuario ingrese datos
    print("Ahora ingresa tus propios datos:")
    try:
        monto_usuario = float(input("Ingresa el monto total de tu compra: "))
        porcentaje_usuario = float(input("Ingresa el porcentaje de descuento (si no sabes, pon 10): "))
        mostrar_resumen(monto_usuario, porcentaje_usuario)
    except ValueError:
        print("Por favor ingresa solo números.")


# Ejecución del programa principal
if __name__ == "__main__":
    main()
