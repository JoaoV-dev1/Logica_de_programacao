valor1 = float(input("digite um comprimento:"))
valor2 = float(input("digite outro comprimento:"))
valor3 = float(input("digite outro comprimento:"))
existe = valor1 - (valor2 + valor3)
if existe < 0:
    if valor1 == valor2 or valor1 == valor3 or valor2 == valor3:
        if valor1 == valor2 and valor1==valor3:
            print("é um triângulo equilátero")
        else:
            print("é um triângulo isósceles")
    if valor1 != valor2 and valor1!=valor3 and valor1!=valor2:
        print("é um triângulo escaleno")
else:
    print("não é um triângulo")