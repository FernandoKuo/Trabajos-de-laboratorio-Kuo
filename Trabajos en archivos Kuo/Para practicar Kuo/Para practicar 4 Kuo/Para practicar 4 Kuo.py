
Otexto = input('Ingrese texto: ')
lista = list(Otexto)
texto = []
for l in lista:
    texto.append(str(ord(l)))
texto = " ".join(texto)

#transferencia
data = open('Valores ASCII.txt', 'w')
data.write('Texto original:\n')
data.write(f'- {Otexto}\n\n')
data.write('Texto en valor ASCII:\n')
data.write(f'- {texto}\n')
data.close()
