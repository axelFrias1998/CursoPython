def main():
    print("REGISTROS")
    numeroPersonas = int(input("¿Cuántas personas quieres registrar? ")) 
    listaPersonas = escrituraRegistros(numeroPersonas)
    lecturaRegistros(listaPersonas)

#Método de escritura de registros según el número de personas
def escrituraRegistros(numeroPersonas): 
    listaPersonas = []
    for registro in range(0, numeroPersonas):
        print(f"Persona {registro + 1}:")
        nombre = input("Ingresa el nombre: ")
        edad = int(input("Ingresa su edad: ")) 
        sexo = bool(int(input("Ingresa su sexo: ")))
        saldo = float(input("Ingresa sus fondos: "))
        curp = input("Ingrese su CURP: ")
        persona = [nombre, edad, sexo, saldo, curp]
        listaPersonas.append(persona)
    return listaPersonas

"""Método de lectura de registros - genérico
def lecturaRegistros(listaPersonas):
    print("|-----------------|")
    print("|Nombre|Edad|Sexo|Saldo|CURP|")
    for registro in listaPersonas:
        print("|", end="")
        for dato in registro:
            print(f"{dato}".center(20, " "), end="|")
        print("")
    print("|-----------------|")
"""
def lecturaRegistros(listaPersonas):
    print("|-----------------|")
    print("|Nombre|Edad|Sexo|Saldo|CURP|")
    for registro in listaPersonas:
        print(f"|{registro[0].center(10, ' ')}".upper(), end="|")
        print(str(registro[1]).center(5, " "), end="|")
        print(f"{'Mujer' if registro[2] else 'Hombre'}".center(8, " "), end="|")
        print(f"${registro[3]}".center(10, " "), end="|")
        print(registro[4].center(10, " "), end="|\n")
    print("|-----------------|")

if __name__ == "__main__":
    main()

"""
|Mariana|20|F|200|FIADSADS|
|Axel|21|M|20|DSADSA|
"""
