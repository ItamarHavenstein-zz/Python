casa = float(input('Qual o valor da casa: R$'))
salario = float(input('Qual o seu salário: R$'))
anosPagamento = int(input('Em quantos anos vc quer pagar? '))

qtdMeses = anosPagamento * 12

parcela = casa / qtdMeses

valorDaParcelaAprovado = salario * 0.3

print('Para pagar uma casa de {:.2f}R$ em {} anos a prestação será de R${:.2f}'.format(casa, anosPagamento, parcela))
if parcela <= valorDaParcelaAprovado:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
