#Booleano True(1) o False(0)
genero = bool(int(input("¿Eres hombre(0) o mujer(1)?: ")))
#De "1" a 1. Luego, de 1 lo pasamos a True
if genero == True:
    print("Pasa al baño de mujeres.")
else:
    print("Pasa al baño de hombres.")

genero = bool(int(input("¿Eres hombre(0) o mujer(1)?: ")))
if genero:
    print("Pasa al baño de mujeres.")
else:
    print("Pasa al baño de hombres.")