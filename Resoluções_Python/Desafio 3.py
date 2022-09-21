#Programa que receba 4 notas de um aluno, uma de cada bimestre, e calcule a media final.
#Imprima a media final e se o aluno foi aprovado ou reprovado, considerando que a media para aprovação seja igual ou superior a seis.
aluno = input("Qual o nome do aluno? ")
nota1 = float(input("Insira a nota do 1º bimestre: "))
nota2 = float(input("Insira a nota do 2º bimestre: "))
nota3 = float(input("Insira a nota do 3º bimestre: "))
nota4 = float(input("Insira a nota do 4º bimestre: "))

media_final = float(nota1 + nota2 + nota3 + nota4) / 4

if float(media_final) >= 6:
    print("O aluno(a) {} teve média final {} e está APROVADO".format(aluno, media_final))
else:
    print("O aluno(a) {} teve média final {} e está REPROVADO".format(aluno, media_final))

