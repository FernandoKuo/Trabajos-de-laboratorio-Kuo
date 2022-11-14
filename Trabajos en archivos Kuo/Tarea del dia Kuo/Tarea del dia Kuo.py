
#setup
def tabla():
    print('Ingresar numero para eligir la opcion')
    print('0. Mostrar tabla actual.')
    print('1. Carta certificada.')
    print('2. Telegrama.')
    print('3. Carta documento.')
    print('4. Telegrama de renuncia.')
    print('5. Terminar.')

opcion = 0
total = 0
acciones = []
renuncia = False
nombre = input('Ingrese su nombre: ')
tabla()
while opcion != 5:
    print()
    opcion = int(input('Opcion: '))
    if opcion == 0:
        tabla()
    elif opcion == 1:
        print('El coste de la carta sera $3000')
        texto = input('Escriba su texto en la carta certificada: \n- ')
        total += 3000
        acciones.append('Carta certificada')
    elif opcion == 2:
        print('El coste del telegrama sera $500 por palabra')
        texto = input('Escriba su texto en el telegrama: \n- ')
        total += len(texto.split()) * 500
        acciones.append('Telagrama')
    elif opcion == 3:
        print('El coste de la carta de documento sera $1000 por hoja')
        cant = int(input('Ingrese la cantidad de hojas: '))
        print('No mienta seguro tiene mas hojas')
        total += (cant + 1) * 1000
        acciones.append('Carta de documento')
    elif opcion == 4:
        print('El telegrama de renuncia es gratis, adios')
        renuncia = True
        opcion = 5
        acciones.append('Telegrama de renuncia')
    elif opcino == 5:
        print('adios')

#transferencia
data = open('Ventas en un correo.txt', 'w')
data.write(f'Nombre del ultimo cliente: {nombre}\n\n')
data.write('Acciones realizadas:\n')
for accion in acciones:
    data.write(f'- {accion}.\n')
data.write(f'Coste total: ${total}\n')
if renuncia: data.write('Gracias por renunciar, adios\n')
data.close()
