import os

for numero in range(0, 100):
    f = open(f"{os.getcwd()}\\almacenamiento\\{numero}.txt", "w")
    if numero % 2 == 1: #Que sobre 0 (par)
        f.write('Es impar')
    else: #
        for valor in range(0, numero + 1):
            f.write(str(valor) + "\n")
    f.close()

numero = "1458942"
temp = 0
for cifra in numero:
    temp = int(cifra) + temp
    print(temp)

if temp % 3 == 0:
    print('Es divisible entre tres')
    