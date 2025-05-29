mulherhomem = int(input("se vc for um homem digite 1, se for mulher digite 2:"))
altura = float(input("digite sua altura em metros:"))
pesohomem = (72.7 * altura) - 58
pesomulher = (62.1 * altura) - 44.7
if mulherhomem == 1:
    print("seu peso ideal é:",pesohomem)
else:
    print("seu  peso ideal é", pesomulher)