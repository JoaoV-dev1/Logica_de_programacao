def numero(variavel1):
    if variavel1 > 0:
        print("numero positivo")
    elif variavel1 < 0:
        print("numero negativo")
    else:
        print("numero nulo")
if __name__ == '__main__':
    valor1 = float(input("digite um valor:"))
    numero(valor1)