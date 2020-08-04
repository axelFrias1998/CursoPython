from datetime import date
from datetime import datetime
from datetime import timedelta
from datetime import time

#Hora actual
horaActual = time(18, 17, 10)
print(horaActual)

#Día actual
hoy = date.today()

#Día/hora actual
ahora = datetime.now()

print(ahora)
print(hoy)

#Date
print(f"El día actual es {hoy.day}")
print(f"El mes actual es {hoy.month}")
print(f"El año actual es {hoy.year}")

fechaConFormato = ahora.strftime("México, D.F. a %d de %B del %Y")

print(fechaConFormato)

fechaNacimiento = datetime(10, 98, 14, 0, 0, 0)
edad = ahora - fechaNacimiento
print(fechaNacimiento)
print(f"Tu edad es de: {edad / 365}")