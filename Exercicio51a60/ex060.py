fatorial = int(input('Digite um número para\ncalcular seu Fatorial: '))
print('Calculando {}! = {} x'.format(fatorial, fatorial), end=" ")
multiplica = fatorial
while fatorial != 1:
    fatorial -= 1
    multiplica = multiplica * fatorial
    if fatorial != 1:
        print('{} x '.format(fatorial), end="")
    else:
        print('{} '.format(fatorial), end="")

print('= {}'.format(multiplica))
