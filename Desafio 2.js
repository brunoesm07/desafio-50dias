var inteiro1 = prompt("Insira o primeiro numero: ")
var inteiro2 = prompt("Insira o segundo numero: ")
var inteiro3 = prompt("Insira o terceiro numero: ")

var maior = inteiro1
if (inteiro2 > maior)
    maior = inteiro2
else if (inteiro3 > maior)
    maior = inteiro3

var menor = inteiro1
if (inteiro2 < menor)
menor = inteiro2
else if (inteiro3 < menor)
menor = inteiro3

alert("O maior numero e " + maior + " e o menor e " + menor)


