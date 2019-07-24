print("-" * 20)
print("Sequencia de Fibonacci")
print('-' * 20)

qtdTermos = int(input('Quantos termos você quer mostrar? '))
vezes = 0;

print('~' * 20)
while vezes < qtdTermos:
    if (vezes == 0):
        a = vezes
        print(' {} ->'.format(a), end='')
        vezes += 1
    elif vezes == 1:
        b = vezes
        print(' {} ->'.format(b), end='')
        vezes += 1
    else:
        c = a + b
        a = b
        b = c
        print(' {} ->'.format(c), end='')
        vezes += 1
print(' FIM')
print('~' * 20)
