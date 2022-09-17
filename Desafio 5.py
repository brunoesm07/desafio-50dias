#Faca um programa que receba um número inteiro positivo N e calcule o somatório de 1 até N.
#Imprima na tela o resultado da soma.

n = int(input("Digite um número inteiro positivo: "))
soma = int(n * (1 + n) / 2)

print(soma)

#Opção 2:

n = int(input("Digite um número inteiro positivo: "))
soma = 0
for i in range(1, n+1):
    soma += i

print(soma)






