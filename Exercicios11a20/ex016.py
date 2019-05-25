from math import trunc

numero = float(input("Digite um valor: "))
valorInteiro = int(numero)

valorInteiro2 = trunc(numero)

print("O valor digitado foi {} e a sua porção inteira é {}".format(numero,valorInteiro))
print("O valor digitado foi {} e a sua porção inteira usando a biblioteca math é {}".format(numero,valorInteiro2))
