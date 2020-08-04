import os
encabezado = """
¿QUE NECESITAS HACER?
1.-Introducir tus datos
2.-Leer tus datos
3.-Eliminar tus datos
4.-Actualizar tus datos
5.-Salir
"""
def main():
    listaDatos = []
    while True:
        print(encabezado)
        try:
            opcion= int(input("¿QUE NECESITAS HACER?"))
            #ESCRITURA
            if opcion == 1:
                os.system("clear")
                print("Introduce tus datos:\n")
                listaDatos.append(datos(listaDatos))
            elif opcion == 2:
                os.system("clear")
                imprimirDatos(listaDatos)
            elif opcion == 3:
                os.system("clear")
                item= eliminar(listaDatos)
                if item != None:
                    listaDatos.pop(listaDatos.index(item))
            elif opcion == 4:
                os.system("clear")
                actualizar(listaDatos)
            elif opcion == 5:
                os.system("clear")
                print("SALIENDO")
                break
            else:
                os.system("clear")
                print("SELECCION INVALIDA")
        except ValueError as valueError:
            print(f"Ingrese correctamente los datos proporcionados: {valueError}")


def datos(listaDatos):
    try:
        nombrePropio = input("INGRESE SU NOMBRE COMPLETO:")
        nombreCurp = (input("INGRESE SU CURP:"))
        return [nombrePropio, nombreCurp]
    except ValueError as valueError:
        print(f"TIPO DE DATO INCORRECTO{valueError}")
    

def imprimirDatos(listaDatos):
    if len(listaDatos) == 0:
        print("Registra tus datos:")
    else:
        for dato in listaDatos:
            print(f"/{dato[0]}/ {dato[1]}/")

def eliminar(listaDatos):
    imprimirDatos(listaDatos)
    try:
        opcion= input("¿Cual registro deseas eliminar?")
    except ValueError as valueError:
        print(f"Tipo de dato incorrecto.Error: {valueError} ") 
    for dato in listaDatos:
        if dato[1] == opcion:
            return dato 
    print("No existe producto")
    return None 


 
def actualizar(listaDatos):
    imprimirDatos(listaDatos)
    try:
        opcion=input("¿QUE DATO NECESITAS CORREGIR?")
        for dato in listaDatos:
            if dato[1] == opcion:
                print(f"Vas a modificar el registro:\n\t - {dato[1]} /")
                print("OPRIME ENTER SI NO DESEAS NINGUN CAMBIO")
                nuevoCurp = input("Ingresa el CURP corregido")
                if nuevoCurp != "":
                    dato[1]= nuevoCurp
    except ValueError as valueError:
        print(f"Tipo de dato incorrecto. ERROR: {valueError}")

    print("No existe dato")


if __name__ == "__main__":
    main()