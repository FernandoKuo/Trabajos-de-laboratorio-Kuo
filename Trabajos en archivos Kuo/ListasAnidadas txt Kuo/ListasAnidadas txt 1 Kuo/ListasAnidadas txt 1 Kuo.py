
lista = [[100, 7, 85, 8], [4, 8, 56, 25], [67, 89, 23, 1], [78, 56]]
Nlista = [[100, 7, 85, 8], [4, 8, 56, 25], [67, 89, 23, 1], [78, 56]]
for parte in Nlista:
    for elemento in parte:
        if elemento > 50:
            Nlista[Nlista.index(parte)][parte.index(elemento)] = 0

#transferencia
data = open('Fijar a 0 numeros mayores a 50.txt', 'w')
data.write('La lista original:\n')
data.write(f'{lista}\n')
data.write('La lista modificada:\n')
data.write(f'{Nlista}\n')
data.close()
