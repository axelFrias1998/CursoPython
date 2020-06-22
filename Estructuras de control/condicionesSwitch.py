parrafo = """
\n\t\tBienvenido
Este es un programa de cálculo de triángulos. 
Seleccione el tipo de triángulo que quiere trabajar. El programa te dará el perímetro de la figura.

1. Equilátero
2. Escaleno
3. Isósceles
4. Salir

"""
while True:
    print(parrafo)
    opcion = int(input("Elige una opción: "))
    if (opcion == 1): #Tres lados iguales
        print("Opción triángulo equilátero.")
        a = float(input("¿Cuánto miden sus lados?: ")) #decimales
        #resultado = a * 3
        #print(f"El perímetro de tu triángulo es de: {resultado} cm")
        print(f"El perímetro de tu triángulo es de: {a * 3} cm")
    elif (opcion == 2): #Tres lados diferentes
        print("Método escaleno")
    elif (opcion == 3): #Dos iguales, uno diferente
        print("Método isósceles")
    elif (opcion == 4):
        break #Salida forzada de un ciclo
    else:
        print("Opción incorrecta. Intenta nuevamente.")
    