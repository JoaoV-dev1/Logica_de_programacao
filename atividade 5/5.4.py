soma = 0
for numero in range(3,501,3):
    if numero % 2 != 0 and numero % 3 == 0:
        soma = numero + soma
print("a soma de todos os numeros inteiros impares multiplos de 3 até quinhentos é:",soma)