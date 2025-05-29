print("Fahrenheit | Celsius")
print("----------------------")
for fahrenheit in range(45, 81):
    celsius = (5/9) * (fahrenheit - 32)
    print(f"{fahrenheit:10} | {celsius:7.2f}")