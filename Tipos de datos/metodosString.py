#Manejo de strings

mensaje = "Mariana será una DIOSA y le gustará"

#print(args str)|print(str args) -> Imprime en consola el resultado de los argumentos
print("\nMÉTODO PRINT\n")
print(mensaje)

"""
Extensión/Tamaño
len(obj) -> integer: El método regresa la cuenta de caracteres en una variable o lista
"""
print("\nMÉTODO LEN")
print(len(mensaje))

"""
Encontrar/Find
Sobrecarga 1: Busca la cadena en todo el texto (str)
Sobrecarga 2: Busca la cadena en un rango (str, start, end)
Ambas te regresan un entero. El entero que te regresa, la posición de inicio
"""
print("MÉTODO FIND".center(50, '-'))
print(f"{mensaje.find('una')}".center(20, '_'))
print(mensaje.find("Mariana", 0, 3))
print(mensaje.find("Mariana", 0, 7))

"""
Lower
Sin argumentos
Retorna la cadena en minúsculas
"""
print("\nMÉTODO LOWER")
print(mensaje.lower())

"""
Upper
Sin argumentos
Retorna la cadena en mayúsculas
"""
print("\nMÉTODO UPPER")
print(mensaje.upper())

"""
Reemplazo/Replace
Argumentos: old str, new str, count int (opcional)
Sobrecarga 1: old str, new str -> str
Sobrecarga 2: old str, new str, count int (opcional) -> str
"""
print("\nMÉTODO REPLACE")
print(mensaje.replace("DIOSA", "BELLACA"))
palabrasRepetidas = "Como como cuando como lo que como porque como"
print(palabrasRepetidas.replace("como", "parkour", 3))

"""
CORTAR
Operador con corchetes str[inicio:final]
de [0 a 3]
"""
mensaje = "Mariana será una DIOSA y le gustará"
print(mensaje[0:7])

"""
zfill
Argumentos: width (longitud)
Agrega ceros a la izquierda según la longitud deseada. Si la cadena es mayor, no agregará ceros.
"""
numeros = "35" #000035
numeros2 = "19984" #19984
print("\nMétodo ZFILL")
print(f"Quiero imprimir un número de seis dígitos: {numeros.zfill(6)}")
print(f"Quiero imprimir un número de cinco dígitos: {numeros2.zfill(5)}")

"""
CENTER
Argumentos: width(longitud), el número de espacios que deja; fillChar, el caracter que imprime en cada espacio
Si la longitud de la cadena es menor a la longitud de espacios deseados, el resultado no se muestra
"""
print("\nMÉTODO CENTER")
print(mensaje.center(70, '_'))
print(mensaje.center(37, '-'))

"""Endswith
Argumentos: suffix (char) caracter a buscar; start y end son posiciones
Retorna True si existe o False si no
"""
registro="1;Mariana;20;1000;"
print("\nMÉTODO ENDSWITH")
print(f"¿El registro termina en ';'?: {registro.endswith(';')}")
print(registro[2:10])
print(f"¿De la posición dos a ocho termina en 'A'?: {registro.endswith(' A', 2, 10)}")