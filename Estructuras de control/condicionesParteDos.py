#Código para elaboración de hot cakes
ganas = bool(int(input("¿Tienes ganas de hot cakes? (1/0)")))
print("Ganas: " + str(ganas))
hambre = bool(int(input("¿Tienes hambre de hot cakes? (1/0)")))
print("Ganas: " + str(hambre))
if ganas and hambre:
    ingredientes = ["Masa", "Leche", "Huevos"]
    comida = False
    #Evaluación comida
    if (len(ingredientes) > 0):
        comida = True
    else:
        dinero = float(input("¿Cuánto dinero tienes?: $"))
        if (dinero >= 47.10):
            ingredientes = ["Masa", "Leche", "Huevos"]
        else:
            print("No tienes dinero")
    #Evaluación ingredientes
    if comida:
        gas = int(input("¿Cuánto gas tienes en litros?: "))
        if (gas > 0):
            hotCakes = True
            print("Vamos a comer") 
        else:
            print("Compra gas")
    else:
        print("No tienes ingredientes, ni dinero")
else:
    print("No tengo ganas/No tengo hambre")