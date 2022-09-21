peso = float(input("Insira seu peso: "))
altura = float(input("Insira sua altura "))

imc = round(peso / (altura * altura), 2)

if imc < 18.5:
    print("Seu IMC é {} e se encontra na faixa de magreza" .format(imc))
elif 18.5 <= imc < 25:
    print("Seu IMC é {} e se encontra na faixa normal".format(imc))
elif 25 <= imc < 30:
    print("Seu IMC é {} e se encontra na faixa de sobrepeso".format(imc))
elif 30 <= imc < 40:
    print("Seu IMC é {} e se encontra na faixa de obesidade".format(imc))
elif imc > 40:
    print("Seu IMC é {} e se encontra na faixa de obesidade grave".format(imc))