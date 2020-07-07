altura = int(input("Altura: "))
for n in range(0, altura):
    print(f"/{'*' * ((2*n) + 1)}\\".center(50))
    
"""    
     /*\ n
    /***\ n
   /*****\ n
  /*******\ n

n = altura triángulo
asteriscos = 2n + 1

Ciclo 0: n = 0;
    print("*" * 2(0) + 1) *

Ciclo 1: n = 1;
    print("*" * 2(1) + 1) ***

Ciclo 2: n = 2;
    print("*" * 2(2) + 1) *****

Ciclo 3: n = 3;
    print("*" * 2(3) + 1)  *******  

"""
    