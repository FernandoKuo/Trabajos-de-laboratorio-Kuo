
#main
old = open('estudiantes.txt', 'r')
new = open('estudiantes2.txt', 'w')

for est in old:
    est = est.split()
    est[0] = est[0].capitalize()
    est[1] = est[1].capitalize()

    new.write(f'{est[0]} {est[1]} , {est[2]} , {est[3]} 301\n')

old.close()
new.close()
