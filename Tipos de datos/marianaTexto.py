#Desde aquí no copiar
from string import Template

#String templates
t = Template("¡Hola, $name!\n")
string = t.substitute(name = "Mariana")
print(string)
#Fin string templates
#Termina no copiar

#String.format()
cadena = "Quiero tacos. Aliméntame, {0}. {1} años sin verte".format("Mariana", 2)
print(cadena)
#Fin string.format()

#F-strings
nacionalidadNoviosMariana = "franceses"
edadLegalEnEstadosUnidos = 21
print(f"Mariana, deja de ligarte {nacionalidadNoviosMariana}. No tienes aún {edadLegalEnEstadosUnidos}.\n")

#Escapado de caracteres
print("\nPrimer Renglón SALTO DE LÍNEA.\nSegundo renglón.\n")
print("\tSangría. ¡Mira el efecto!")
print("\\")
#Fin escapado de caracteres

#Operadores
print("Concatenamos una frase " + "Concatenamos otra")
print(" Te amo"*1000)

palabra = "moraleja"
print(f"\nSexto caracter: {palabra[6]}")
print(f"Busquemos la fruta en la palabra {palabra}, que es: la {palabra[0:4]}")
#In significa existe en: el ejemplo dice "moral existe en palabra"
print(f'¿Se encuentra la palabra \"moral\" en {palabra}?: {"moral" in palabra}')
#NOT IN significa NO EXISTE EN: 
print(f'¿No se encuentra la palabra \"moral\" en {palabra}?: {"moral" not in palabra}')

No, no estoy en casa. (-) * (-) = (+)
No. No estoy en casa. (-) + (-) = (-)
No estoy en casa. (-) = (-)
#no no voy a ir al cine
#no no hay alguien en el cuarto vacío 

 