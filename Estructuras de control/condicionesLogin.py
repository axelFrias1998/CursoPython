"""
Contraseña eran números
Usuario eran string
"""
usuario = input("Dame tu usuario: ")
contrasenia = int(input("Dame contraseña: "))

if(usuario.upper() == "MARIANA" and contrasenia == 1234):
    print("Bienvenida")
else:
    print("Usuario y/o contraseña incorrectos")



