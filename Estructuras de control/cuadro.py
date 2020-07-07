ladoA = int(input("Lado A: "))
ladoB = int(input("Lado B: "))

for costado in range(0, ladoA):
    print("|", end="")
    for ancho in range(0, ladoB):
        print("-", end="")
    print("|", end="\n")