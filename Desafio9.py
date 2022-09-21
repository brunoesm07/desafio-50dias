dias_trab = int(input("Insira a quantidade de dias trabalhados: "))
anos = int(dias_trab / 360)
meses = int((dias_trab % 360) / 30)
dias = int(dias_trab % 30)

print("O funcionário trabalhou {} ano(s), {} mes(es) e {} dia(s)." .format(anos, meses, dias))
