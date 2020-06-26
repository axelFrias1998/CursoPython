import sys
import math

parrafo = f"""
\tBienvenido.
Este es un programa de cálculo de triángulos. Seleccione el tipo de triangulo que quiere trabajar
1. Equilátero
2. Escaleno
3. Isósceles 
4. Salir
"""
print(math.pi)

while True:
    print(parrafo)
    opcion = int(input("Elige una opción:"))
    sys.getsizeof()
    print(f"La opción a pesa: {sys.getsizeof(opcion)} bytes")
    if (opcion == 1):
        print("Método Equilátero")
        a = float (input("¿Cuánto miden sus lados?:"))
        print(f"El perímetro de tu triángulo es de: {a * 3} cm")
    elif (opcion == 2):
        print("Método Escaleno")
        a = float(input("¿Cuanto miden los lados iguales?"))
        b = float(input("¿Cuanto miden el lado diferente?"))
        print(f"El perímetro de tu triángulo es de {a * 2 + b} cm ")
    elif (opcion == 3):
        ambitoDiferente = "Hola"
        print("Método Isósceles")
        a = float(input("¿Cuánto mide su lado"))
        b = float(input("¿Cuánto mide su lado"))
        c = float(input("¿Cuánto mide su lado?"))
        print(f"El perímetro de tu triángulo es de: {a + b + c} cm ")
    elif (opcion == 4):
        break #Salida forzada de un ciclo
    else:
        print("Opción incorrecta. Intenta nuevamente.")
