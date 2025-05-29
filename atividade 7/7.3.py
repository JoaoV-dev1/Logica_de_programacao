def calculadora(variavel1,variavel2):
    operador = input("soma[+]\t\t\t\tsubtração[-]\nmultiplicação[x]\tdivisão[/]\nescolha a operação:")
    if operador == '+':
        soma = variavel1 + variavel2
        print("resultado:",soma)
    elif operador == '-':
        subtracao = variavel1 - variavel2
        print("resultado:",subtracao)
    elif operador == 'x':
        multiplicacao = variavel1 * variavel2
        print("resultado:",multiplicacao)
    elif operador == '/':
        divisao = variavel1/variavel2
        print("resultado:",divisao)
    else:
        print("opção inexistente")
if __name__ == '__main__':
    valor1 = float(input("digite um valor:"))
    valor2 = float(input("digite outro valor:"))
    calculadora(valor1,valor2)