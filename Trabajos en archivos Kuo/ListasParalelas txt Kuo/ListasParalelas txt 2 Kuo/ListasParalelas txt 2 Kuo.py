
alumnos = []
notas = []
condicion = []
for i in range(4):
    nombre = input(f'Ingrese nombre del {i+1}° alumno: ')
    nota = int(input('Ingrese respectiva nota: '))
    alumnos.append(nombre)
    notas.append(nota)
    if nota >= 8: condicion.append('Avanzado')
    elif nota >= 6: condicion.append('Suficiente')
    else: condicion.append('En Proceso')

#transferencia
data = open('Notas de los alumnos.txt', 'w')
data.write('Nombres, notas y condiciones de los alumnos:\n')
for a, n, c in zip(alumnos, notas, condicion):
    data.write(f'- {a}   {n}   {c}\n')
data.close()
