def valor_absoluto(variavel1):
    if variavel1 >= 0:
        return variavel1
    elif variavel1 < 0:
        variavel1 = variavel1 * (-1)
        return variavel1
if __name__ == '__main__':
    valor1 = float(input("digite um valor:"))
    print("numero absoluto:",valor_absoluto(valor1))