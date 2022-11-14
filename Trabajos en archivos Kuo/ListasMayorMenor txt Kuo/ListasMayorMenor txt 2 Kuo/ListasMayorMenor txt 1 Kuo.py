
enteros = []
for i in range(5):
    n = int(input(f'Ingrese {i+1}° entero: '))
    enteros.append(n)
mayor = max(enteros)
cant = enteros.count(mayor)

#transferencia
data = open('Mayor de 5 numeros.txt', 'w')
data.write(f'Los 5 numeros: {enteros}\n')
data.write(f'El mayor de los 5 numeros: {mayor}\n')
data.write(f'El mayor numero se repite {cant} veces\n')
data.close()
