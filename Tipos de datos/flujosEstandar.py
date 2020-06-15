#FLUJOS ESTÁNDAR

"""
UNA VARIABLE SE CREA:
nombreDeLaVariable = valor
"""
try:
    nombre = input("¿Cuál es tu nombre?: ")
    print(f"¡Hola, {nombre}! Te haremos algunas preguntas. :)")
    moneda = float(input("¿Cuánto dinero tienes?: $")) #10.60
    #Género: F True(1) M False(0)
    genero = bool(input("¿Estado civil?: "))
    edad = int(input(f"¿Cuál es tu edad, {nombre}?: "))
    print(f"Tu edad es: {edad} y de tipo {type(edad)}")
#De conversión/valor
except ValueError:
    print("La edad no es correcta")
#De índice
except IndexError:
    print("Error, el índice no se encuentra dentro del rango")
#Generico
except:
    print("No se pudo determinar el error")
