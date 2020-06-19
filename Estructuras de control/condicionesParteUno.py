pregunta = bool(int(input("1 = True, 0 = False: ")))
print(pregunta)

valor = input("¿Es de noche? (True/False): ")
noche = False

if valor == "True":
    noche = True
else:
    noche = False

#(no)(noche)
#(0)(1) = 0
#True = 1 y False = 0
#Si (no)(noche) es verdadero

if not noche is True:
    luz = True
    print("Ufas, ando prendido")
else:
    luz = False
    print("Estoy apagado")