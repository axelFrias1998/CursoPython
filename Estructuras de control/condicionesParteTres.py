"""Booleano: que admite dos respuestas
Verdadero(1) ó Falso(0)
Operadores de comparación
< menor que
> mayor que
<= menor igual
>= mayor igual
== idéntico
!= diferente
PROGRAMA DE RESTRICCIÓN DE MORRAS BORRACHAS"""
a = 4 # '=' se llama asignación
b = 8
print(a == b) # '==' se llama comparación

mayorDeEdad = False #TODAS LOS BOOLEANOS SE INICIALIZAN EN FALSO porque no han sido evaluados o trabajos

"""Métodos de conversión
int()
bool()
float()
str()
La entrada estándar sólo retorna strings
"""
edad = int(input("¿Cuál es tu edad?: "))
"""
Si es menor a 18 años, la persona no pasa
Si tiene 18 años y es menor de 70, la persona pasa
Si tiene más de 70, se le da la sugerencia de irse
"""
"""
(0, 17) = no entran
[18, 70] = entran
    [60, 70] = Poco alcohol
[70, +) = sugerencia
"""
#Si la edad es menor a 18 años (0, 17]
if (edad < 18): #condición verdadera ó falsa
    print("Morra borracha, eres menor de edad.")
elif (edad >= 18 and edad <= 70): #condición verdadera ó falsa, después de una negativa
    print("Adelante")
    if (edad >= 60 and edad <= 70):
        print("Denle poco alcohol")
else: #última operación - Todo lo demás
    print("La Tierra los reclama")

# respuesta = bool(int(input("Verdadero(1) y Falso(0)")))
#Programa: Escribir un programa que evalúe si entro o no al baño de mujeres
#Programa: Escribir un programa que evalúe si el inicio de sesión es correcto
#if(usuario == "Mariana" and contrasenia == 1234)