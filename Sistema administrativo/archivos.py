import os

encabezado = """
¿Qué quieres hacer?
1. CREAR ARCHIVO - CREATE (CRUD)
2. LEER ARCHIVO - READ
3. ELIMINAR ARCHIVO - DELETE
4. Salir
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
                print("SALIENDO")
                break
            else:
                os.system("clear")
                print("Selección inválido")
        except ValueError as valueError:
            print(f"Tipo de dato incorrecto. ERROR: {valueError}")

def lectura():
    if os.path.exists(f"{os.getcwd()}/informacion.txt"):
        file = open(f"{os.getcwd()}/informacion.txt", "r")
        for line in file:
            print(f"UNA LÍNEA: {line}")

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


