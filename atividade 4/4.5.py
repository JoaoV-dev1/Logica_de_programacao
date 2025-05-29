ct = 0
print("- ordem descrescente")
x = int(input("digite o numero inicial da sua sequencia:"))
for numeros in range(x, -1, -1):
    print(numeros)
    ct = ct+1
print("encerrou a repetição")
print("a quantidade de numeros digitados é igual a:",ct)