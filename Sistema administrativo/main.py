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
                listaProductos.append(nuevoProducto())
            
            elif seleccion == 2:
                os.system("clear")
            
            elif seleccion == 3:
                os.system("clear")
            
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
        
def nuevoProducto():
    key = int(input("Ingresa su ID: "))
    nombreProducto = input("Ingresa su nombre: ")
    costoCompra = float(input("Ingresa sus fondos: "))
    return [key, nombreProducto, costoCompra]

if __name__ == "__main__":
    main()

"""
|1|Leche|20.0|
|2|Papas|12.50|
"""