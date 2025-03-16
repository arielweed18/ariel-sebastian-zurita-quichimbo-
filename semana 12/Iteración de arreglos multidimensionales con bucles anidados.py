def calcular_promedio_ciudad(datos):
    """
    Calcula el promedio de temperatura para cada ciudad a partir de datos organizados en 3 dimensiones:
    ciudades -> semanas -> días.

    Parámetros:
        datos (dict): Estructura anidada donde cada llave es el nombre de una ciudad. Cada ciudad es otro
                      diccionario en el que las llaves son las semanas (por ejemplo, "Semana1", "Semana2",
                      "Semana3") y los valores son listas con las temperaturas de cada día de esa semana.

    Retorna:
        dict: Un diccionario con el nombre de la ciudad y su temperatura promedio, calculada con todas las
              semanas y días.
    """
    promedios_ciudades = {}  # Diccionario para almacenar los promedios de cada ciudad

    for ciudad, semanas in datos.items():  # Itera sobre cada ciudad y sus semanas de datos
        suma_total = 0
        conteo_total = 0

        for semana, temperaturas in semanas.items():  # Itera sobre las semanas y sus temperaturas diarias
            suma_total += sum(temperaturas)  # Suma todas las temperaturas de la semana
            conteo_total += len(temperaturas)  # Cuenta cuántos valores hay en total

        # Cálculo del promedio evitando división por cero
        promedio = suma_total / conteo_total if conteo_total > 0 else None
        promedios_ciudades[ciudad] = promedio  # Almacena el promedio en el diccionario

    return promedios_ciudades  # Retorna el diccionario con los promedios de cada ciudad


# 🔹 Datos de ejemplo con temperaturas en grados centígrados
datos_ejemplo = {
    "Quito": {
        "Semana1": [14.2, 15.6, 16.1, 14.8, 17.3, 16.9, 15.2],
        "Semana2": [16.3, 14.9, 15.4, 15.1, 14.7, 16.8, 15.9],
        "Semana3": [15.4, 16.2, 14.7, 17.1, 15.5, 16.3, 14.9]
    },
    "Cuenca": {
        "Semana1": [11.8, 12.4, 13.0, 11.5, 13.7, 12.9, 12.2],
        "Semana2": [13.5, 12.3, 11.9, 13.8, 12.7, 11.6, 11.4],
        "Semana3": [12.8, 11.9, 13.6, 12.4, 12.3, 13.2, 11.8]
    },
    "Durán": {
        "Semana1": [28.5, 29.3, 27.9, 28.8, 30.2, 29.7, 28.6],
        "Semana2": [29.8, 28.4, 27.7, 30.5, 28.9, 29.2, 27.5],
        "Semana3": [28.7, 27.6, 29.1, 30.4, 29.3, 28.5, 27.8]
    }
}

# 🔹 Llamada a la función y visualización de resultados
resultados = calcular_promedio_ciudad(datos_ejemplo)
print("📊 **Temperaturas Promedio en °C:**")
for ciudad, promedio in resultados.items():
    print(f"🌍 {ciudad}: {promedio:.2f}°C")
