import os

#Make directory -> carpeta
for numero in range(0, 5):
    os.mkdir(f'{os.getcwd()}\\Carpeta de prueba\\{numero}')
    f = open(f'{os.getcwd()}\\Carpeta de prueba\\{numero}.txt', "w")
    f.write('Hola')
    f.close()

#Remove directory -> remover carpeta
rutas = os.listdir("Carpeta de prueba")
print(rutas)

for ruta in rutas:
    if os.path.isfile(f'{os.getcwd()}\\Carpeta de prueba\\{ruta}'):
        print('Es un archivo')
        os.remove(f'{os.getcwd()}\\Carpeta de prueba\\{ruta}')
    if os.path.isdir(f'{os.getcwd()}\\Carpeta de prueba\\{ruta}'):
        print('Es un directorio, no se va a a eliminar')
