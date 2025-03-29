# Escritura en un archivo de texto

# Abrimos el archivo 'my_notes.txt' en modo escritura ('w')
# Si el archivo no existe, se creará automáticamente
with open("my_notes.txt", "w") as file:
    # Escribimos tres líneas de notas personales
    file.write("Hoy aprendí a trabajar con archivos en Python.\n")
    file.write("Es importante cerrar los archivos después de usarlos.\n")
    file.write("Los métodos write() y readline() son muy útiles.\n")

# Lectura del archivo de texto

# Abrimos el archivo 'my_notes.txt' en modo lectura ('r')
with open("my_notes.txt", "r") as file:
    # Leemos y mostramos el contenido línea por línea
    print("Contenido del archivo my_notes.txt:")
    line = file.readline()
    while line:
        print(line.strip())  # strip() elimina saltos de línea al final
        line = file.readline()

# Nota: Usar 'with open(...) as ...' asegura que el archivo se cierre automáticamente
