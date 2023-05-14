'''

Questão 5
Um dos principais usos destinados aos operadores lógicos é a construção de expressões condicionais, que são utilizadas para (re)direcionar o fluxo de um programa. Isso é possível com as expressões if, elif e else em Python.

a = int(input("Digite o primeiro número inteiro: "))
b = int(input("Digite o segundo número inteiro: "))
c = int(input("Digite o terceiro número inteiro: "))

if a > b and a > c:

  resposta = a % 2 == 0

elif b > a and b > c:

  resposta = b % 2 == 0

else:

  resposta = c % 2 == 0

print(XXX, resposta)
Pelo que o "XXX" deve ser substituído no código acima (ou seja, o que este código efetivamente faz?)


"O maior número entre os três informados é positivo?" (ou seja, o programa exibe, através de um booleano, se o maior entre os três números informados é positivo).


"O maior entre os três números informados é:" (ou seja, o programa exibe qual é o maior entre os três números informados).


"O maior número entre os três informados é par?", (ou seja, o programa exibe, através de um booleano, se o maior entre os três números informados é par). RESPOSTA **

"O menor entre os três números informados é:" (ou seja, o programa exibe qual é o menor entre os três números informados).


"O maior número entre os três informados é ímpar?" (ou seja, o programa exibe, através de um booleano, se o maior entre os três números informados é ímpar).

'''