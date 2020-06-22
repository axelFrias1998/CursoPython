"""Operador ternario - que consta de tres elementos

resultado = valorPositivo if condición else valorNegativo
"""
"""
1. Si es de noche, prende la luz
2. Si es de día, apaga la luz.
"""
luz = False
hora = int(input("Dame la hora del día: "))
if (hora >= 8 and hora <= 18):
    luz = False
else: #Antes de las 8 de la mañana y después de las 6 de la tarde
    luz = True
print("Sin operador ternario: " + str(luz))
#resultado = valorPositivo if condición else valorNegativo
foco = False if (hora >= 8 and hora <= 18) else True
print(f"Con operador ternario: {foco}")

print("Es de día") if (hora >= 8 and hora <= 18) else print("Es de noche")