print('Aluguel de carro.')
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos kilometros rodados? '))

pordia = 60 * dias
totalkm = 0.15 * km
pagar = pordia + totalkm

print('O total a pagar é de R${:.2f}'.format(pagar))
