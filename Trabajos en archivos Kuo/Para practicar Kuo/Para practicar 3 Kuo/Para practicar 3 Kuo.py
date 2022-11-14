
Otexto = input('Ingrese texto con indices:\n- ')
indice = input('Ingrese el tipo de indice que ingreso: ').strip()
indicacion = []
guardar = False

for l in Otexto:
    if l == indice:
        guardar = not guardar
        continue
    if guardar:
        indicacion.append(l)
texto = "".join(indicacion)

#transferencia
data = open('Texto oculto entre los indices.txt', 'w')
data.write('Texto oculto entre los indices:\n\n')
data.write(texto)
data.write('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
data.write('Texto original:\n\n')
data.write(Otexto)
data.write('\n')
data.close()
