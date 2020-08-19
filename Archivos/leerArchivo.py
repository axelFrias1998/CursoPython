#Paso UNO
import os

print(os.getcwd())
try:
    if os.path.exists(f"{os.getcwd()}\\almacenamiento\\baseDeDatosPrueba.txt"):
        f = open(f"{os.getcwd()}\\almacenamiento\\baseDeDatosPrueba.txt", "r")
        print("Impresión directa de F/FILE")
        #for linea in f: -> Consume más proceso
            #print(linea, end="")
        #caracteres = f.readline(5)
        lineas = f.readlines()
        print(f.readable())
        f.close()

        print("Impresión directa de variables")
        #print(caracteres) ->consume RAM
        print(lineas)
        for linea in lineas: 
            #if linea[0] == 'a' or linea[0] == 'A':
                #print(linea)
            if len(linea) > 10:
                print(linea)
#EOF -> End Of File
except EOFError as eofError:
    print("Algo malo pasó")
except FileNotFoundError as fileNotFounError:
    print("No existe el archivo")
