'''
Questão 4
Em muitos programas é necessário que mais de uma expressão lógica seja avaliada, de maneira composta. É possível realizar a composição lógica através dos operadores and e or do Python. Além disso, o operador not é utilizado para inverter o valor lógico de um booleano ou expressão lógica como um todo.

x = 4.2

y = 10

z = "42"

not (((x * y == z) and not (x < y)) or y % 2 == 0)
Qual das seguintes alternativas contém uma expressão que resulta no mesmo valor lógico (True ou False) que a última linha do código acima?


not (not (x < y and x * y == z)) or (x >= y or y % 2 == 0)

not False

not ((x == y or True) and ((int(z) < x*y) and (type(y) == type(int(z)))))

not (((not True) or int(z) % 7 == 0) and ((str(int(x*y)) == z) and (type(x) != type(z)))) RESPOSTA **

(True and True) or not True



'''