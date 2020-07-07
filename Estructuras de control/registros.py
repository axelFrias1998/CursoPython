numeroPersonas = int(input("¿Cuántas personas quieres registrar? ")) #FILA - REGISTRO

listaPersonas = []
for registro in range(0, numeroPersonas):
    print(f"Persona {registro + 1}:")
    nombre = input("Ingresa el nombre: ")
    edad = int(input("Ingresa su edad: ")) 
    sexo = bool(int(input("Ingresa su sexo: ")))
    saldo = float(input("Ingresa sus fondos: "))
    curp = input("Ingrese su CURP: ")
    persona = [nombre, edad, sexo, saldo, curp]
    listaPersonas.append(persona)

#Formato estándar
print(listaPersonas)

#Método de lectura
for registro in listaPersonas:
    print(f"Persona")
    for dato in registro:
        print(f"{dato}")

"""
|-----------------|
|Nombre|Edad|Sexo|Saldo|CURP|
|Mariana|20|F|200|FIADSADS|
|Axel|21|M|20|DSADSA|
|---------| 
"""
