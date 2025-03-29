# Crear el diccionario con información ficticia
informacion_personal = {
    "nombre": "William Zurita",
    "edad": 55,
    "ciudad": "Quito",
    "profesion": "Ingeniero agronomo"
}
# aceder la informacion de la ciudidad y modificarla
informacion_personal["ciudad"] = "Pichincha"

# agregar uan telefono ficticio
informacion_personal["Telefono fijo"] = 3682098

#Verifica si la clave "telefono" existe en el diccionario. Si no existe, agrégala con un número de teléfono ficticio
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "098886747"

# eliminar informacion_persolnal (edad)
del informacion_personal["edad"]

# Imprimir el diccionario para ver el resultado
print(informacion_personal)

