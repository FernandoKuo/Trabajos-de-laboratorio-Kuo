
oracion = input('Ingrese una oracion: ')
esp_cant = len(oracion.split()) - 1

#transferencia
data = open('Cantidad de espacios.txt', 'w')
data.write(f'La ultima oracion ingresada tenia {esp_cant} espacios\n')
data.write(f'La oracion: "{oracion}"\n')
data.close()
