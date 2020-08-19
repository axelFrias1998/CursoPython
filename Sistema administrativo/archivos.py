import os

encabezado = """
¿Qué quieres hacer?
1. CREAR ARCHIVO - CREATE (CRUD)
2. LEER ARCHIVO - READ
3. ELIMINAR ARCHIVO - DELETE
4. Modificar
5. Salir
"""
def main():
    print("BASE DE DATOS")
    while True:
        print(encabezado)
        try:
            seleccion = int(input("¿Qué deseas realizar? ".upper()))
            #Escritura productos
            if seleccion == 1:
                os.system("clear")
                crearArchivo()
            #Leer
            elif seleccion == 2:
                os.system("clear")
                lectura()
            #Eliminar
            elif seleccion == 3:
                os.system("clear")
            elif seleccion == 4:
                os.system("clear")
                modificar()
            elif seleccion == 5:
                os.system("clear")
                print("SALIENDO")
                break
            else:
                os.system("clear")
                print("Selección inválido")
        except ValueError as valueError:
            print(f"Tipo de dato incorrecto. ERROR: {valueError}")

def modificar():
    print(f"{os.getcwd()}\\Registros\\prueba.txt")
    if os.path.exists(f"{os.getcwd()}\\Registros\\prueba.txt"):
        with open(f"{os.getcwd()}\\Registros\\prueba.txt") as prueba:
            lineas = prueba.readlines()
        temporal = lineas[4].split(';')
        temporal[0] = "200"
        temporal[1] = "Mariana"
        temporal[2] = "FIHA98"
        lineas[4] = ';'.join(temporal)
        with open(f"{os.getcwd()}\\Registros\\prueba.txt", "w") as updateFile:
            updateFile.writelines(lineas)
    #valor = "3213;Axel;FIHA980" 
    #despuesDeSplit = valor.split(';')
    #print(f"Tu ID es: {despuesDeSplit[0]}\nTu nombre es: {despuesDeSplit[1]}\nTu CURP es: {despuesDeSplit[2]}")
    #print(despuesDeSplit)
    ##sub -> substraer
    #producto = "Sabritas"
    #fecha = "09082020"
    #local = "Ajusco"
    #clave = producto[0:3].upper() + fecha[2:4] + local[-3:].upper()
    #print(clave)
def lectura():
    if os.path.exists(f"{os.getcwd()}/informacion.txt"):
        file = open(f"{os.getcwd()}/informacion.txt", "r")
        for line in file:
            print(f"UNA LÍNEA: {line}")
        file.close()

def crearArchivo():
    if not os.path.exists('Registros'):
        os.makedirs("Registros")
    os.chdir("Registros")
    file = open(f"{os.getcwd()}/informacion.txt", "w")
    file.write('Hola mundo en archivos!')
    file.close()
    #if os.path.exists(f"{os.getcwd()}/informacion.txt"):
    #    file = open(f"{os.getcwd()}/informacion.txt", "a")
    #    for num in range(0, 10):
    #        file.write(f"{str(num)};MARIANA;MAR\n")
    #    file.close()
    #else:

if __name__ == "__main__":
    main()


