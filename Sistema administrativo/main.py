import os

encabezado = """
=========================
|                        |
|                        |
|   Abarrotes la Carmen  |
|                        |
|                        |
=========================
¿Qué quieres hacer?
1. Agregar productos - CREATE (CRUD)
2. Leer productos - READ
3. Eliminar productos - DELETE
4. Actualizar productos - UPDATE
5. Salir
"""

def main():
    listaProductos = []
    while True:
        print(encabezado)
        try:
            seleccion = int(input("¿Qué deseas realizar? ".upper()))
            #Escritura productos
            if seleccion == 1:
                os.system("clear")
                print("Agrega un producto: \n")
                listaProductos.append(nuevoProducto(listaProductos))
            #Leer
            elif seleccion == 2:
                os.system("clear")
                imprimirProductos(listaProductos)
            #Eliminar
            elif seleccion == 3:
                os.system("clear")
                item = eliminar(listaProductos)
                if item != None:
                    #listaProductos.remove(item) #Elimina el objeto
                    listaProductos.pop(listaProductos.index(item)) #elimina según el índice o el último valor
                    #del listaProductos[listaProductos.index(item)] #elimina la posición indicada

            elif seleccion == 4:
                os.system("clear")
            
            elif seleccion == 5:
                os.system("clear")
                print("SALIENDO")
                break
            else:
                os.system("clear")
                print("Selección inválido")
        except ValueError as valueError:
            print(f"Tipo de dato incorrecto. ERROR: {valueError}")
        
def nuevoProducto(listaProductos):
    try:
        key = 0
        if len(listaProductos) == 0:
            key = 1
        else:
            key = listaProductos[len(listaProductos) - 1][0] + 1
        nombreProducto = input("Ingresa su nombre: ")
        costoCompra = float(input("Ingresa sus fondos: "))
        return [key, nombreProducto, costoCompra]
    except ValueError as valueError:
        print(f"Tipo de dato incorrecto. ERROR: {valueError}")    

def imprimirProductos(listaProductos):
    if len(listaProductos) == 0:
        print("Registra un producto")
    else:
        for producto in listaProductos:
            print(f"|{producto[0]}|{producto[1]}|${producto[2]}|")

def eliminar(listaProductos):
    imprimirProductos(listaProductos)
    try:
        seleccion = int(input("¿Cuál registro deseas eliminar? (ID): "))
    except ValueError as valueError:
        print(f"Tipo de dato incorrecto. ERROR: {valueError}")
      
    for producto in listaProductos:
        if producto[0] == seleccion:
            return producto
    print("No existe el producto")
    return None


if __name__ == "__main__":
    main()

"""
|1|Leche|20.0|
|2|Papas|12.50|
"""