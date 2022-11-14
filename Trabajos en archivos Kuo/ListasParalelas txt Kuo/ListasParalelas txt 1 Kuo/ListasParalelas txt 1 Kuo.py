
productos = []
precios = []
promedio = 0
for i in range(5):
    producto = input(f'Ingrese nombre del {i+1}° producto: ')
    precio = int(input('Ingrese precio del respectivo producto: '))
    productos.append(producto)
    precios.append(precio)
    promedio += precio
promedio /= 5

#transferencia
data = open('Producto y precios mayor al promedio.txt', 'w')
data.write('Productos y sus precios:\n')
for pro, pre in zip(productos, precios):
    data.write(f'- {pro} ${pre}\n')
data.write(f'\nProductos que superaron el promedio del precio: (>{promedio})\n')
for pro, pre in zip(productos, precios):
    if pre > promedio:
        data.write(f'- {pro} ${pre}\n')
data.close()
