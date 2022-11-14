
texto = input('Ingrese texto: ')
lista = []
for letra in texto:
    if letra != ' ':
        lista.append(letra)
texto = ' '.join(lista)

#transferencia
data = open('Caracteres separados.txt', 'a')
data.write(texto)
data.write('\n\n')
data.close()
