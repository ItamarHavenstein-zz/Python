from random import randint

pc = randint(0, 10)

print('Sou seu computador...'
      '\nAcabei de pensar em um número entre 0 e 10.'
      '\nSerá que você consegue adivinhar qual foi?')
palpite = int(input('Qual é seu palpite? '))
tentativas = 0
while palpite != pc:
    if pc < palpite:
        print('Menos... Tente mais uma vez.')
    else:
        print('Mais... Tente mais uma vez.')
    tentativas += 1
    palpite = int(input('Qual é seu palpite? '))
tentativas += 1
print('Acertou com {} tentativas. Parabéns!!!'.format(tentativas))
