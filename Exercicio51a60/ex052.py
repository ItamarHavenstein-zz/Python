numero = int(input('Digite um Numero: '))
primo = 0

for c in range(1, numero + 1, 1):
    if (numero % c == 0):
        print("{}".format(c), end=" ")
        primo += 1
    else:
        print('\033[31m{}\033[m'.format(c), end=" ")

print('\nO número {} foi divisível {} vezes'.format(numero, primo))
if primo == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
