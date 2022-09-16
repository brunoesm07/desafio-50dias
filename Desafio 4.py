#Faça um programa que receba duas dimensões de um terreno (frente e comprimento) e imprima a area deste.
#Considerando que o preço do metro quadrado é de R$ 7.592,00, imprima também o valor que custará o terreno.

frente = float(input("Quantos metros o terreno tem de frente?"))
fundos = float(input("Quantos metros o terreno tem de comprimento?"))
area = (frente * fundos)

print("O terreno possui {} m2" .format(area))

precoM2 = (7592.0)
valorTerreno = (area * precoM2)

print("O terreno está avaliado em R$ {}" .format(valorTerreno))
#print(f"O terreno está avaliado em R$ {valorTerreno}")