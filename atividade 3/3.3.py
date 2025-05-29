ct = 0
pares = 0
impares = 0
print("digite [0] para terminar")
while True:
    valores = int(input("digite um valor:"))
    if valores == 0:
        break
    ct=ct+1
    resto = valores%2
    if resto == 0:
        pares = pares + valores
    else:
        impares = impares + valores
mediaP=pares/ct
mediaI=impares/ct
print("media aritmética dos números pares digitados é:",mediaP)
print("media aritmética dos números ímpares digitados é:",mediaI)