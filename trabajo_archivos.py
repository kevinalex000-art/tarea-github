# trabajo_archivos.py
# Tarea: Trabajo con Archivos de Texto en Python

# Escritura de archivo
with open("my_notes.txt", "w") as archivo:
    archivo.write("Primera nota: revisar compatibilidad de hardware.\n")
    archivo.write("Segunda nota: optimizar formato de informe técnico.\n")
    archivo.write("Tercera nota: preparar presentación académica en PowerPoint.\n")

# Lectura de archivo
with open("my_notes.txt", "r") as archivo:
    print("Contenido del archivo my_notes.txt:\n")
    linea = archivo.readline()
    while linea:
        print(linea.strip())
        linea = archivo.readline()
