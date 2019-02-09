import matplotlib.pyplot as graph
from math import*
from time import sleep
#Une boucle pour repeter le programme
while True:
    a = input("Choisissez un nombre pour y appliquer la conjecture de Syracuse.\n")
    a = int(a)
    altitude = [a]
    b = a
    def syracuse(a):
        vol = 0
        sleep(1)
        print("Le nombre choisi est ", a)
        print(a)
        while a != 1:
            #Ici la condition pour le nombre pair
            if a%2 == 0:
                a = a/2
                print(a)
                sleep(0.35)
                vol = vol + 1
                altitude.append(a)
            #Ici la condition pour le nombre impair
            elif a%2 != 0:
                a = a*3+1
                print(a)
                sleep(0.35)
                vol = vol + 1
                altitude.append(a)
        sleep(1)
        print('le temps de vol est de', vol, 'valeurs')
        sleep(1)
        print("L'altitude maximale de la suite Syracuse", b, "est de", max(altitude))
        sleep(1)
        graph.axis([0, vol, 0, max(altitude)])
        graph.xlabel('vol de la suite de Syracuse choisie')
        graph.ylabel('altitude de la suite')
        for k in range(1, vol):
            graph.plot([k], [altitude[k]], 'ro')
        graph.show()
    syracuse(a)
    
