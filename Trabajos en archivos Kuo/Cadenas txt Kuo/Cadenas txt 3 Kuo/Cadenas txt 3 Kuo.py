
guardar = False
clave = input('Ingrese clave: ')
if len(clave) >= 10 and len(clave) <= 20:
    print('Clave creada exitosamente')
    guardar = True
else:
    print('Clave debe tener entre 10 y 20 caracteres')

#transferencia
if guardar:
    data = open('Contraseña.txt', 'w')
    data.write(f'Ultima clave ingresada: {clave}\n')
    data.close()
