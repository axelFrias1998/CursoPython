#Palabra while, seguida de condición
"""coche = 10
while coche <= 9:
    print(f"Vuelta {coche}")
    coche = coche + 1
    #coche += 1
else:
    print("El coche ya dio vueltas")



opcion = 0
while opcion != 4:
    print(parrafo)
    opcion = int(input("Elige una opción:"))
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
        pass #Salida forzada de un ciclo
    else:
        print("Opción incorrecta. Intenta nuevamente.")
"""
listaNumeros = [1, 2, 3, 4, 5]
palabra = "Hola"
print("Recorrido números con for")
for numero in listaNumeros: #Foreach for
    print(numero)

for i in range(0, len(listaNumeros)):
    print(f"En la posición {i}, se encuentra el número: {listaNumeros[i]}")

print("Recorrido números con while")
try:
    listaNumeros = [1, 2, 3, 4, 5]
    tamanio = len(listaNumeros)
    i = 0
    print(f"Hay {tamanio} datos")
    while i <= tamanio: #while
        print(listaNumeros[i])
        i += 1
except IndexError as error:
    print(f"Error de tipo: {error}")
#contadores


print("Palabra")
for letra in palabra:
    print(letra)

"""Para trabajar con booleanos, se recomienda
utilizar while
opcion = False
while opcion == False:
    pass
while nombre == "Mariana":
    pass
while numero <= (3 + 4):
    pass
"""

#Tarea que inicien con A y que su tamaño sea menor a 6
listaNombres = ["Mariana", "Axel", "David", "Alejandra", "Pedro", "Ximena"]