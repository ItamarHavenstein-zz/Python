import locale

valor = int(input('Preço das compras: R$'))

print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque \n'
      '[ 2 ] à vista cartão \n'
      '[ 3 ] 2x no cartão \n'
      '[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual a opção? '))
locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

if opcao == 1:
    pagamento = valor - (valor * 0.10)
    print('Suas compras de {}, ficaram em {} com o desconto de 10%'
          ''.format(locale.currency(valor), locale.currency(pagamento)))
elif opcao == 2:
    pagamento = valor - (valor * 0.05)
    print('Suas compras de {:.2f}, ficaram em {:.2f} com o desconto de 5%'.format(valor, pagamento))
elif opcao == 3:
    pagamento = valor / 2
    print('Suas compras de {}, ficaram no valor de {} em 2 vezes sem acréscimo'.format(valor, pagamento))
elif opcao == 4:
    parcelas = int(input('Em quantas parcelas você deseja: '))
    pagamento = (valor + (valor * 0.20)) / parcelas
    print('Suas compras de {}, ficaram no valor de {} em {} vezes com juros \n'
          'Valor final da sua compra será de {}'.format(valor, pagamento, parcelas, (pagamento * parcelas)))
else:
    print('Opção inválida, tente novamente')
