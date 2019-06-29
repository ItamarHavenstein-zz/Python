viagem = float(input('Digite a distancia da viagem! '))

print('A distância da viagem é {}Km'.format(viagem))
if viagem <= 200:
    preco = viagem * 0.50
else:
    preco = viagem * 0.45
print('O custo da sua viagem será de {:.2f}R$'.format(preco))
