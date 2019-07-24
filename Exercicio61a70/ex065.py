continuar = 'S'
soma = qtd = 0
maior = menor = 0
while continuar != 'N':
    valor = int(input('Digite um número: '))
    soma += valor
    qtd += 1
    if maior == 0:
        maior = valor
        menor = valor
    else:
        if maior < valor:
            maior = valor
        elif menor > valor:
            menor = valor
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
print('Você digitou {} números e a média foi {:.2f}'.format(qtd, (soma / qtd)))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
