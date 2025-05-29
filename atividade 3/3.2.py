alunos= 0
aprovados = 0
reprovados = 0
print("digite [-1] para finalizar:")
while True:
    notas = float(input("digite a nota da prova"))
    if notas == -1:
        break
    alunos = alunos +1
    if notas >= 5:
        aprovados = aprovados + 1
    else:
        reprovados = reprovados +1
print("quantidade de alunos que fizeram a prova:",alunos)
print("quantidade de alunos aprovados:",aprovados)
print("quantidade de alunos reprovados:",reprovados)