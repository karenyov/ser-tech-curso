'''
Questão 2
Algumas situações requerem que os dados sejam recebidos diretamente pelo usuário como parte da execução do programa. Isso pode ser feito com a função input(). No entanto, esta função sempre retorna os valores em string. Assim, se os dados esperados do usuário forem numéricos, é importante realizar a conversão dos tipos de dados para que eles possam ser processados. Considere o trecho abaixo:

num1 = XXX

dobro = 2*num1

print("O dobro do número digitado é:", dobro)
Levando em consideração que o usuário pode entregar qualquer número como input, o 'XXX' no código acima deve ser substituído por qual elemento?



input("Digite um número a seguir: ")

float(input("Digite um número a seguir: ")) RESPOSTA ***

str(input("Digite um número a seguir: "))

int(input("Digite um número a seguir: ")) 

list(input("Digite um número a seguir: "))

'''