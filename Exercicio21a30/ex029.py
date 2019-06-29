velocidade = int(input('Qual é a velocidade do automovel? '))

if velocidade <= 80:
    print('Tempo bom para uma boa viagem!!')
else:
    adicional = velocidade - 80
    print('MULTADO!!! VOCÊ PASSOU DO LIMITE QUE É DE 80Km/h '
          'E FOI MULTADO EM {:.2f}R$'.format(adicional * 7))
