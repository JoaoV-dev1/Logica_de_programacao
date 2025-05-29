valor1 = float(input("digite um valor:"))
valor2 = float(input("digite outro valor:"))
calculadora =  int(input("digite 1 para soma ou 2 para multiplicação ou 3 para subtração ou 4 para divisão:"))
soma = valor1 + valor2
vezes = valor1*valor2
subtracao = valor1-valor2
divisao = valor1/valor2
if calculadora == 1:
    print("resultado:",soma)
if calculadora == 2:
    print("resultado:",vezes)
if calculadora == 3:
    print("resultado:", subtracao)
if calculadora == 4:
    print("resultado:",divisao)