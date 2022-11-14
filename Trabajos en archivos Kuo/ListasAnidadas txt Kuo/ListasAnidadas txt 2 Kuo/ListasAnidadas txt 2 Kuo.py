
lista = [[4, 12, 5, 66], [14, 6, 25], [3, 4, 5, 67, 89, 23, 1], [78, 56]]
Nlista = [[4, 12, 5, 66], [14, 6, 25], [3, 4, 5, 67, 89, 23, 1], [78, 56]]
for parte in Nlista:
    for elemento in parte:
        if elemento > 10:
            Nlista[Nlista.index(parte)][parte.index(elemento)] = 0

#transferencia
data = open('Fijar a 0 numeros mayores a 10.txt', 'w')
data.write('La lista original:\n')
data.write(f'{lista}\n')
data.write('La lista modificada:\n')
data.write(f'{Nlista}\n')
data.close()
