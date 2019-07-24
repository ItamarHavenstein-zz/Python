from time import sleep

primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))

opcao = 0
while opcao != 5:
    sleep(1)
    print('[ 1 ] somar'
          '\n[ 2 ] multiplicar'
          '\n[ 3 ] maior'
          '\n[ 4 ] novos números'
          '\n[ 5 ] sair do programa')
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        print('A soma entre {} + {} é {}'.format(primeiro, segundo, (primeiro + segundo)))
    elif opcao == 2:
        print('A multiplicação entre {} x {} é {}'.format(primeiro, segundo, (primeiro * segundo)))
    elif opcao == 3:
        if primeiro > segundo:
            maior = primeiro
        else:
            maior = segundo
        print('O maior número entre {} e {} é {}'.format(primeiro, segundo, maior))
    elif opcao == 4:
        primeiro = int(input('Primeiro valor: '))
        segundo = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=' * 10)
sleep(4)
print('Fim do programa! Volte sempre!')
