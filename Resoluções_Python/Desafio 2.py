#Faça um programa que leia tres valores inteiros e imprima o maior e o menor deles
valor1 = int(input("Insira o primeiro valor:"))
valor2 = int(input("Insira o segundo valor:"))
valor3 = int(input("Insira o terceiro valor:"))

maiorValor = valor1
if (valor2 > maiorValor):
    maiorValor = valor2
if (valor3 > maiorValor):
    maiorValor = valor3

menorValor = valor1
if (valor2 < menorValor):
    menorValor = valor2
if (valor3 < menorValor):
    menorValor = valor3

print("O maior valor é", maiorValor)
print("O menor valor é", menorValor)