import random
from time import sleep

print('Suas opções:\n'
      '[ 0 ] Pedra\n'
      '[ 1 ] Papel\n'
      '[ 2 ] Tesoura')
opcao = int(input('Qual é a sua jogada? '))
itens = ['PEDRA', 'PAPEL', 'TESOURA']
escolher = [0, 1, 2]

pc = random.choice(escolher)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!\n')

print('O computador jogou {}'.format(itens[pc]))
print('Você jogou         {}\n'.format(itens[opcao]))

if opcao == pc:
    print('Houve um empate')
elif (opcao == 0 and pc == 2) or (opcao == 1 and pc == 0) or (opcao == 2 and pc == 1):
    print('Você ganhou')
elif (opcao == 0 and pc == 1) or (opcao == 1 and pc == 2) or (opcao == 2 and pc == 0):
    print('Você perdeu')
else:
    print('Opção inválida, Tente novamente.')
