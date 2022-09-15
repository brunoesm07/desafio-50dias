#Faça um programa que calcule a diferença entre o preço de um produto e o valor em dinheiro pago, imprimindo para o usuário o quanto será o troco
preco = input("Preço do produto: ")
pagamento = input("Valor pago em dinheiro: ")
troco = float(pagamento) - float(preco)

print(f"Seu troco é de {troco}")