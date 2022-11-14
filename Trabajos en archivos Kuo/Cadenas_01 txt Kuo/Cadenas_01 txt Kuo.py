
cant = int(input('Ingrese cantidad de empleados: '))
empleados = {}
for i in range(cant):
    nombre = input(f'Ingrese nombre del {i+1}° empleado: ').strip()
    dni = int(input('Ingrese respectivo dni: '))
    str_dni = str(dni)
    usuario = nombre[0:3] + str_dni[len(str_dni)-3: len(str_dni)]
    empleados.update({usuario: [nombre, dni]})
    print('Usuario del empleado creado exitosamente')

#transferencia
data = open('Usuarios de los empleados de un local.txt', 'a')
for u, (n, dni) in empleados.items():
    data.write(f'{u}: {n} {dni}\n')
data.close()
