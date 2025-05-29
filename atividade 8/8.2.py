notas = []
print("digite [-1] para terminar o processo")
while True:
    nota = float(input("digite a nota da prova:"))
    if nota == -1:
        break
    elif nota < -1:
        print("nota invalida")
        break
    else:
        notas.append(nota)
media = sum(notas)/len(notas)
print("a quantidade de alunos é:",len(notas))
print("a media das notas da turma é:",media)