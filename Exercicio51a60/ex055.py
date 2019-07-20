maiorPeso = 0.0
menorPeso = 0.0
for c in range(1, 6, 1):
    peso = float(input('Pesso da {}° pessoa: '.format(c)))
    if c == 1:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        elif peso < menorPeso:
            menorPeso = peso

print('O maior peso lido foi de {}Kg'
      '\nO menor peso lido foi de {}Kg'.format(maiorPeso, menorPeso))
