from math import hypot

catOpo = float(input("Comprimento do cateto oposto: "))
catAdj = float(input("Comprimento do cateto adjacente: "))

hip = hypot(catAdj,catOpo)

print("A hipotenusa vai medir {:.2f}".format(hip))
