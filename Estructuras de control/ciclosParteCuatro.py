#Matriz [fila][columna] y = filas, x = columnas
numeroPersonas = int(input("¿Cuántas personas quieres registrar? ")) #FILA - REGISTRO
numeroDeDatos = int(input("¿Cuántos datos tienen? ")) #COLUMNA - DATO

listaPersonas = []

#Método de escritura
for registro in range(0, numeroPersonas):
    persona = []
    print(f"Persona {registro + 1}:")
    for dato in range(0, numeroDeDatos):
        persona.append(input(f"Dame el dato {dato + 1}: "))
    listaPersonas.append(persona)

for registro in range(0, numeroPersonas):
    print(f"Persona {registro}:")
    for columna in range(0, numeroDeDatos):
        print(f"Dato {columna + 1}: {listaPersonas[registro][columna]}")
"""
for registro in range(0, numeroPersonas):
    print(f"Persona {registro + 1}:")
    nombre = input("Ingresa el nombre: ")
    edad = int(input("Ingresa su edad: ")) 
    sexo = bool(int(input("Ingresa su sexo: ")))
    persona = [nombre, edad, sexo]
    listaPersonas.append(persona)

#Formato estándar
print(listaPersonas)

#Método de lectura
for registro in listaPersonas:
    print(f"Persona")
    for dato in registro:
        print(f"{dato}")


  """