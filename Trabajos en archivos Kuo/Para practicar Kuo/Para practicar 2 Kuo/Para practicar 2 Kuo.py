
tweet = input('Ingrese un tweet (con los hashtags que quiera): ')
cant = tweet.count('#')

#transferencia
data = open('Cantidad de hashtags.txt', 'w')
data.write('El tweet:\n')
data.write(tweet)
data.write(f'\n\nTiene {cant} hashtag(s)\n')
data.close()
