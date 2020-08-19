#PASO UNO
import os

#IO -> INPUT OUTPUT
#f -> file
print(os.getcwd())
f = open(f"{os.getcwd()}\\almacenamiento\\baseDeDatosPrueba.txt", "w")
f.write("AQUI CREO O SOBREESCRIBO MI ARCHIVO")
f.close()

f = open(f"{os.getcwd()}\\almacenamiento\\baseDeDatosPrueba.txt", "a")
f.write("\nAQUI AGREGO UNA LINEA\n")
for numero in range(0, 20):
    f.write(f"{numero}-")
f.close()

meses = ["Enero", "Febrero", "Marzo"]
f = open(f"{os.getcwd()}\\almacenamiento\\baseDeDatosPrueba.txt", "a")
f.writelines(meses)
f.close()

f = open(f"{os.getcwd()}\\almacenamiento\\baseDeDatos.txt", "a")
f.write("1;Mariana;MAR149908\n")
f.close()


