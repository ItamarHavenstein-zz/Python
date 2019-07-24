valor = soma = qtd = 0
while valor != 999:
    valor = int(input('Digite um número [999 para parar]: '))
    if valor != 999:
        soma += valor
        qtd += 1
print('Você digitou {} nùmeros e a soma entre eles foi {}.'.format(qtd, soma))
