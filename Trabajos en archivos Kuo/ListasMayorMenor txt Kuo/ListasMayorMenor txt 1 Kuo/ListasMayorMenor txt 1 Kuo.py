
personas = []
for i in range(5):
    nombre = input(f'Ingrese nombre de la {i+1}° persona: ')
    personas.append(nombre)
ordenado = sorted(personas)

#transferencia
data = open('Nombre de la persona menor en orden alfabetico.txt', 'w')
data.write('Los ultimos nombres fueron:\n')
data.write(f'- {personas[0]}\n- {personas[1]}\n- {personas[2]}\n- {personas[3]}\n- {personas[4]}\n')
data.write('\nOrdenado alfabeticamente:\n')
data.write(f'- {ordenado[0]}\n- {ordenado[1]}\n- {ordenado[2]}\n- {ordenado[3]}\n- {ordenado[4]}\n')
data.close()
