nota1 = float(input("digite a primeira nota:"))
nota2 = float(input("digite a segunda nota:"))
nota3 = float(input("digite a terceira nota:"))
media = (nota1 + nota2 + nota3) /3
if nota1 > 10 or nota3 > 10 or nota2 > 10:
    print("nota não válida")
if media < 7:
    print("reprovado")
else:
    print("aprovado")