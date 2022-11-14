
texto = input('Ingrese una frase corta: ')
tapa = len(texto) + 2
simbolo = '*'

#transferencia
def tapar():
    for i in range(tapa):
        data.write(simbolo)
    data.write('\n')

def espaciar():
    data.write('          ')
    
data = open('Visualizacion del texto en un cuadro.txt', 'w')
espaciar()
tapar()
espaciar()
data.write(f'{simbolo}{texto}{simbolo}\n')
espaciar()
tapar()
data.close()


