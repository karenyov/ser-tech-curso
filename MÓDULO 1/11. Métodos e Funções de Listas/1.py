lista = [10, 50, 30, 40, 25, 60, 5]

print('Antes do append:', lista)

lista.append(3)

print('Depois do append:', lista)

lista.insert(2, 10)

print('Depois do insert:', lista)


lista2 = [4,2,3]
lista.extend(lista2)

print('Depois do extend:', lista)

lista.pop()

print('Lista após o pop:', lista)

lista.pop(0)

print('Lista após o pop:', lista)

lista.remove(3)

print('Lista após o remove:', lista)

print('Quantidade de 2 na lista:', lista.count(2))

print('Índice do elemento 12:', lista.index(2))

lista.sort()

print(lista)

lista.sort(reverse=True)

print(lista)

print(len(lista))

print(sum(lista))

print(min(lista))


print(max(lista))










