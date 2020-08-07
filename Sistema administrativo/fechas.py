from datetime import date
from datetime import datetime
from datetime import timedelta
from datetime import time

#dia > 0 &  < 32 (0, 32) [1, 31]
#mes > 0 &  < 13
#anio > 1930 & 2021

def main():
    try:
        #do while
        while(True):
            dia = int(input("Ingresa tu día de nacimiento (1 - 31): "))
            if (dia > 0 and dia < 32):
                pass
            else:
                continue
            mes = int(input("¿De qué mes? (1 - 12): "))
            if (mes > 0 and mes < 13):
                pass
            else:
                continue
            anio = int(input('¿De qué anio? (1960 - 2020): '))
            if (anio > 1959 and anio < 2021):
                pass
            else:
                continue
            fechaNacimiento = date(anio, mes, dia)
            diaSemana = datetime.weekday(fechaNacimiento)
            print(f"Naciste un {diaSemanaEscrito(diaSemana)} {fechaNacimiento.day} de {mesEscrito(fechaNacimiento.month)} de {fechaNacimiento.year}")
    except ValueError as error:
        print(f"Tipo de dato incorrecto. ERROR: {error}")


def mesEscrito(mes):
    meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    return meses[mes - 1]

def diaSemanaEscrito(diaSemana):
    semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    return semana[diaSemana]

if __name__ == "__main__":
    main()