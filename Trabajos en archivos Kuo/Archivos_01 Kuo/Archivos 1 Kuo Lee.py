
#setup
lista_telefonica = {}

def agregar():
    cant = int(input('Cuantos clientes desea agregar a la lista? '))
    for i in range(cant):
        nombre = input('Ingrese nombre del nuevo cliente: ')

        if nombre != '':
            if nombre in lista_telefonica.keys():
                a = input('Tal cliente ya existe, desea cambiar su numero de telefono?(s/n) ')
                if a == 's': cambiar(nombre)
            else:
                telefono = input('Ingrese el telefono del nuevo cliente: ')
                lista_telefonica.update({nombre: telefono})
                print('Nuevo cliente agregado a la lista telefonica con exito')

def cambiar(nombre):
    if nombre in lista_telefonica.keys():
        telefono = input(f'Ingrese nuevo numero de telefono de {nombre}: ')
        lista_telefonica.update({nombre: telefono})
        print(f'Numero de {nombre} cambiado con exito')
    else: print('Tal cliente no existe')

def eliminar(nombre):
    if nombre in lista_telefonica.keys():
        a = input(f'Desea eliminar el telefono de {nombre}?(s/n) ')
        if a == 's':
            lista_telefonica.update({nombre: ''})
            print(f'Se elimino el numero de telefono de {nombre}')
        else: print('No se elimino ningun numero de telefono')

def actualizar():
    global accion
    
    lista = open('telefonos.txt', 'a')
    lista.write('\n')

    for nombre, telefono in lista_telefonica.items():
        lista.write(f'{nombre}, {telefono}\n')
    lista.write('\n')
    lista.close()
    accion = -1

def mostrar():
    lista = open('telefonos.txt', 'r')
    contenido = lista.read()
    print(contenido)
    lista.close()

def tabla():
    print('0. Mostrar tabla de opciones')
    print('1. Agregar numero de telefono de un nuevo cliente')
    print('2. Cambiar el numero de telefono de un cliente')
    print('3. Eliminar el numero de telefono de un cliente (El cliente queda en la lista)')
    print('1. Agregar numero de telefono de un nuevo cliente')
    print('4. Actualizar lo hecho en la lista telefonica (termina de ejecutar)')
    print('5. Mostrar la lista telefonica (no actualizado hasta el momento)')

#main
accion = 'nose'
tabla()
while accion != -1:    
    print()
    accion = int(input())
    
    if accion == 0:
        tabla()
    elif accion == 1:
        agregar()
    elif accion == 2:
        nombre = input('Ingrese nombre del cliente: ')
        cambiar(nombre)
    elif accion == 3:
        nombre = input('Ingrese nombre del cliente: ')
        eliminar(nombre)
    elif accion == 4:
        actualizar()
    elif accion == 5:
        mostrar()

















        
    
