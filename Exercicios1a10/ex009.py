tabu = int(input('Digite um número para ver sua tabuada: '))

print('-' * 12)
for x in range(1, 11):
    print('{} x {:2} = {}'.format(tabu, x, (tabu * x)))

print('-' * 12)
