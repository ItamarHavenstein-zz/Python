print('Gerador de PA')
print('=-=' * 10)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
contador = 0
print('{} -> '.format(termo), end='')
while contador != 9:
    termo += razao
    print('{} -> '.format(termo), end='')
    contador += 1
print('FIM')
