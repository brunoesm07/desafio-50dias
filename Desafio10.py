import math

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))

a = num1 + num2
b = num1 * (num2 ** 2)
c = num1 ** 2
d = (num1 ** 2 + num2 ** 2) ** 0.5
# ou d = math.sqrt(num1 ** 2 + num2 ** 2)
e = math.sin(num1 - num2)


print("A soma dos números é {}" .format(a))
print("O produto do primeiro número pelo quadrado do segundo é {}" .format(b))
print("O quadrado do primeiro número é {}" .format(c))
print("A raiz quadrada da soma dos quadrados é {:.2}" .format(d))
print("O seno da diferença do primeiro número pelo segundo é {:.2}" .format(e))