def est_premier(nombre):
    premier = True

    for diviseur in range(2, nombre):
        if nombre % diviseur == 0:
            premier = False
            break

    return premier


for nombre in range(2, 1001):
    if est_premier(nombre):
        print(nombre)



        