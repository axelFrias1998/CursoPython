import os

#Make directory -> carpeta
for numero in range(0, 5):
    os.mkdir(f'{os.getcwd()}\\Tarea imposible parte dos\\{numero}')
    f = open(f'{os.getcwd()}\\Tarea imposible parte dos\\{numero}.txt', "w")
    f.write('Hola')
    if numero > 449
    f.close()

#Remove directory -> remover carpeta
rutas = os.listdir("Carpeta de prueba")
print(rutas)

os.remove
for ruta in rutas:
    
    if os.path.isfile(f'{os.getcwd()}\\Carpeta de prueba\\{ruta}'):
        print('Es un archivo')
        os.remove(f'{os.getcwd()}\\Carpeta de prueba\\{ruta}')
    if os.path.isdir(f'{os.getcwd()}\\Carpeta de prueba\\{ruta}'):
        print('Es un directorio, no se va a a eliminar')

#Agregar 500 archivos, 500 carpetas en un directorio llamado 'Tarea imposible parte dos'. En el archivo 99 Escribir 'Hola soy Mariana', en el 199 escribir 'Axel me odia por la tarea' y desde el 450 escribir la numeración como la hemos trabajado
#Eliminar las carpetas 153, 29, 300 y 0; y los archivos múltiplos de 5
