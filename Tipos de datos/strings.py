from string import Template

#f-Strings
nacionalidadNoviosMariana = "alemanes"
print(f"Mariana, deja de ligarte {nacionalidadNoviosMariana}.\n")

#String.format()
cadena = "Quiero unos tacos, {0}\n".format("Mariana")
print(cadena)

#Strings templates
t = Template("¡Hola, $name!\n")
string = t.substitute(name = "Mariana")
print(string)

#Escape de caracteres
print("Primer renglón.\nSegundo renglón.\n")
print("Tabulación.\t¡Mira el efecto!\n")

#Operadores
print("Concateno una frase " + "con otra\n")
print("Dos veces la misma frase*2")

palabra = "moraleja"
print("Primer caracter: " + palabra[0])
print("Busquemos la fruta en la palabra: " + palabra[0:3])
print("¿Se encuentra la palabra \"moral\"?: " + str("moral" in palabra))
print("¿No se encuentra la palabra \nalmeja\"?: " + str("almeja" not in palabra))

#cadenas
saludo = "Hola"
primerCaracter = saludo[0]
segundoCaracter = saludo[1]
tercerCaracter = saludo[2]
cuartoCaracter = saludo[3]

print(f"En la palabra \"{saludo}\", el primer caracter es: '{primerCaracter}'; en la segunda posición se encuentra la letra '{segundoCaracter}''; en la tercera, el segundo índice de la palabra, la letra '{tercerCaracter}''; y al final, antes del final de la palabra en la posición 4, a letra '{cuartoCaracter}''")


