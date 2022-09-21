cateto1 = float(input("Digite o valor de um dos catetos: "))
cateto2 = float(input("Digita o valor do outro cateto: "))

hipotenusa = (cateto1 ** 2 + cateto2 ** 2) ** (1/2)

print("A hipotenusa é {}." .format(hipotenusa))