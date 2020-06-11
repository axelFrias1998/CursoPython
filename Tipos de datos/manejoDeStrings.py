#Manejo de strings

mensaje = "Mariana será una DIOSA y le gustará"

#args significa argumentos
#print(args str) -> Imprime en consola el resultado del mensaje
print("MÉTODO PRINT\n")
print(mensaje)

"""Extensión/Tamaño de cadena
len(obj) -> Retorna un número entero con la longitud de la cadena/objeto
"""
print("MÉTODO LEN\n")
print(len(mensaje))

"""Encontrar
Sobrecarga 1: Busca la cadena en todo el texto (str)
Sobrecarga 2: Busca la cadena de texto en un rango(str, integer -> start, integer -> end)
Ambos retornan un entero. El inicio si lo encuentra y -1 si no.
"""
print("\nMÉTODO FIND\n")
print(mensaje.find("Mariana"))
print(mensaje.find("Diosa", 0, 10))
print(mensaje.find("una", 10, 20))

"""Lower
Sin argumentos
Retorna la cadena en minúsculas
"""
print("\nMÉTODO LOWER")
print(mensaje.lower())

"""Upper
Sin argumentos
Retorna la cadena en mayúsculas
"""
print("\nMÉTODO UPPER")
print(mensaje.upper())

"""Reemplazar/Replace
Argunemtos: old, new, count (opcional). Old es la cadena que sistituirá, new es la cadena que pondrá y count es el número de veces que lo cambiará
"""
print("\nMÉTODO REPLACE")
print(mensaje.replace("DIOSA", "BELLACA"))
palabrasRepetidas = "Como como cuando como lo que como porque como"
print(palabrasRepetidas)
print(palabrasRepetidas.replace("como", "parkour", 2))

"""Cortar
Operador de cadenas con corchetes [inicio:final]
"""
print("\nCORTAR CON CORCHETES")
print(mensaje[0:7])

"""zfill
Argumentos: width (longitud)
Agrega ceros a la izquierda según la longitud deseada. Si la cadena es mayor, no agregará ceros.
"""
numeros = "35"

print("\nMétodo ZFILL")
print(f"Quiero imprimir un número con seis dígitos: {numeros.zfill(6)}")


"""CENTER
Argumentos: width(longitud), el número de espacios que deja; fillChar, el caracter que imprime en cada espacio
Si la longitud de la cadena es menor a la longitud de espacios deseados, el resultado no se muestra
"""
print("\nMÉTODO CENTER")
print(mensaje.center(100, '-'))
print(mensaje.center(10, ' '))

"""Endswith
Argumentos: suffix (char) caracter a buscar; start y end son posiciones
Retorna True si existe o False si no
"""
registro="1;Mariana;20;1000;"
print("\nMÉTODO ENDSWITH")
print(f"¿La cadena termina en ';'?: {registro.endswith(';')}")
print(f"¿De la posición cero a cinco termina en ';'? :{registro.endswith(';', 0, 5)}")