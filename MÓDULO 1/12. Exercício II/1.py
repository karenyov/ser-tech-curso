'''

Questão 1
Em Python é possível utilizar expressões condicionais para o direcionamento de fluxo do código. Considere o trecho de código a seguir:

x = int(input("Digite um número inteiro: "))

if XXX:
    resp1 = "negativo"
else:
    resp1 = "positivo"
    
if ***:
    resp2 = "par"
else:
    resp2 = "impar"
    

print("
O número {} é {} e {}.".format(x, resp1, resp2))
O código acima informa se o número inteiro informado pelo usuário (e armazenado na variável x) é positivo ou negativo e par ou ímpar. Por exemplo, caso o usuário digite o número -42, o output esperado é:

O número -42 é negativo e par.

Para que este output seja possível, pelo que devemos substituir XXX e *** no código acima, respectivamente?


x > 0
e

x % 2 == 0

x < 0
e

x // 2 == 0

x == 0
e

x / 2 == 0

x < 0
e

x % 2 == 0

x < 0   ** RESPOSTA CERTA
e

x % 2 != 0

'''