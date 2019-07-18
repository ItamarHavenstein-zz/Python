termo = int(input('Digite o primeiro termo: '))
razao = int(input('digite a razão: '))

for c in range(termo, termo +(10 * razao), razao):
    print('{}'.format(c), end=' ')
print('ACABOU')
