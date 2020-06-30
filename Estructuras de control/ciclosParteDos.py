"""
Ciclos determinados
Controlados a partir de código
"""
numeroPasos = 0
while numeroPasos < 10:
    print(f"Avanaza {numeroPasos} pasos")
    numeroPasos += 1

for i in range(0, 10):
    print(i)
"""
Ciclos indeterminados
Todos los ciclos que no controles desde tu código
"""
articulosNuevos = int(input("¿Cuántos artículos vas a ingresar?"))
contador = 0
listaArticulos = []
while contador < articulosNuevos:
    listaArticulos.append(input(f"Artículo {contador}: "))
    contador += 1
else:
    listaArticulos.remove(listaArticulos[1])
    print(f"Tus artículos son: {listaArticulos}")

for contador in range(0, 20, 10):
    print(f"Artículo {contador}")
