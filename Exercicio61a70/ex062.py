print('Gerador de PA')
print('=-=' * 10)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

progressao = 10
contador = 1
continuar = True
print('{} ->'.format(termo), end='')
while continuar:
    if contador != progressao:
        termo += razao
        print('{} -> '.format(termo), end='')
        contador += 1
    else:
        print('PAUSA')
        mais = int(input('Quantos termos você quer mostrar a mais? '))
        progressao += mais
        if mais == 0:
            continuar = False
print('Progressão finalizada com {} termos mostrados.'.format(progressao))
