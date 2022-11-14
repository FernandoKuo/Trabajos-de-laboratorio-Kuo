
oracion = input('Ingrese una oracion: ')
vocales = ['a', 'e', 'i', 'o', 'u']
cant = 0
for letra in oracion.lower():
    if letra in vocales:
        cant += 1

#transferencia
data = open('Cantidad de vocales.txt', 'w')
data.write(f'La ultima oracion ingresada tenia {cant} vocales\n')
data.write(f'La oracion: "{oracion}"\n')
data.close()
