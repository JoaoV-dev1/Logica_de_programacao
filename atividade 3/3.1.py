ct = 0
ct1 = 0
soma = 0
print("digite [-1] para terminar")
valores = float(input("digite um valor:"))
while True:
    if valores == -1:
        break
    soma = soma + valores
    valores = float(input("digite um valor:"))
    ct = ct + 1
    if valores > 20:
        ct1 = ct1 + 1
media = soma/ct
print("a quantidade de valores digitados é:",ct)
print("a soma dos valores digitados é:",soma)
print("a media dos valores digitados é:",media)
print("a quantidade de valores digitados maior que 20 é:",ct1)