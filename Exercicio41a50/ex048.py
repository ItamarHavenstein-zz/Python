soma = 0
vezes = 0

for c in range(1, 501):
    if (c % 2 == 1):
        if (c % 3 == 0):
            soma += c
            vezes += 1
print('A soma de todos os {} valores solicitados é {}'.format(vezes, soma))
