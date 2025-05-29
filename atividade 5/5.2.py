x = float(input("digite a temperatura inicial da tabela:"))
y = float(input("digite a temperatura final da tabela:"))
print("Fahrenheit | Celsius")
print("----------------------")
if x <= y:
    for fahrenheit in range(x, y):
        celsius = (5/9) * (fahrenheit - 32)
        print(f"{fahrenheit:10} | {celsius:7.2f}")
elif x > y:
    for fahrenheit in range(y, x):
        celsius = (5/9) * (fahrenheit - 32)
        print(f"{fahrenheit:10} | {celsius:7.2f}")