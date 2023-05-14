


def saudacao(nome, curso):
    print(f'Seja bem-vindo(a) {nome}!')

    print(f'Curso: {curso}!')


saudacao("Maria", "Python")


def soma(num1, num2):
    return num1+num2


print('O resultado da soma é: ', soma(5,7))


def calculadora(num1, num2, operacao='+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    
resultado = calculadora(10, 20, '+')

print(resultado)
