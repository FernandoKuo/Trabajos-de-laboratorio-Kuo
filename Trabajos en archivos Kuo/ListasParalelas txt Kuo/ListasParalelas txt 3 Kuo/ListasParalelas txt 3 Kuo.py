
print('Ingresara 4 enteros en dos listas')
lista1 = []
lista2 = []
listas = [lista1, lista2]
lista_sum = []
for i in range(2):
    for j in range(4):
        num = int(input(f'{j+1}° numero de la {i+1}° lista: '))
        listas[i].append(num)
for l1, l2 in zip(lista1, lista2):
    lista_sum.append(l1 + l2)

#transferencia
data = open('Suma de enteros de dos listas.txt', 'w')
data.write(f'Primera lista: {lista1}\n')
data.write(f'Segunda lista: {lista2}\n')
data.write('La suma de los elementos de las dos listas:\n')
data.write(f'{lista_sum}')
data.close()
