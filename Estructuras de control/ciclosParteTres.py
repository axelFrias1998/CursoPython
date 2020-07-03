numPersonas=int(input("Ingrese numero de personas"))
listaPersonas=[]
print(listaPersonas)
i=0

#Escritura
while i < numPersonas:
    nombre = input("Ingresa el nombre: ")
    edad = int(input("Ingresa su edad: ")) 
    sexo = bool(int(input("Ingresa su sexo: ")))
    persona = [nombre, edad, sexo]
    listaPersonas.append(persona)
    i+=1

print(listaPersonas)
#CRUD= CREATION, READ, UPDATE, DELETE
i=0
#Lectura
print(f"Total de personas: {len(listaPersonas)}")
while i < numPersonas:
    print(f"Datos persona {i + 1}")
    print(f"Su nombre es: {listaPersonas[i][0]}")
    print(f"Su edad es: {listaPersonas[i][1]}")
    #valor_si if condicion else valor_no
    print(f"Su sexo es: {'Mujer' if listaPersonas[i][2] else 'Hombre'}")
    i+=1
#listaPersonas[i][0]=input("Ingresa nombre 1:") 
 #   listaPersonas[i][1]=int(input("Ingresa Edad:"))
  #  listaPersonas[i][2]=bool(int(input("ingresa sexo:")))