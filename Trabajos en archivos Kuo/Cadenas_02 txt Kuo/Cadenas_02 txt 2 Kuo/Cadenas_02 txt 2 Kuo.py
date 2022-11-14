
frase = input('Ingrese una frase con todos los espacios innecesarios que quiera: ')
Nfrase = " ".join(frase.split())
esp_cant = len(frase.split()) - 1

#transferencia
data = open('Espacios innecesarios eliminados.txt', 'w')
data.write(f'Frase original: "{frase}"\n')
data.write(f'Frase corregida: "{Nfrase}"\n')
data.close()
