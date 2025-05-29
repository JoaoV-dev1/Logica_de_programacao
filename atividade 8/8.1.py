numeros = []
print("digite [-1] para terminar o processo")
while True:
    valor1 = int(input("digite um numero para adicionar na lista:"))
    if valor1 == -1:
        break
    numeros.append(valor1)
print("a quantidade de numeros digitados foi:",len(numeros))