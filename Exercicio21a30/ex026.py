frase = str(input('Digite uma frase: '))

fraseSemEspaço = frase.strip().upper()
qtd = fraseSemEspaço.count('A')
primeiraVez = fraseSemEspaço.find('A') + 1
ultimaVez = fraseSemEspaço.rfind("A") + 1

print('A letra A aparece {} vezes na frase.'.format(qtd))
print('A primeira Letra A apareceu na posição {}'.format(primeiraVez))
print('A última letra A apareceu na posição {}'.format(ultimaVez))
