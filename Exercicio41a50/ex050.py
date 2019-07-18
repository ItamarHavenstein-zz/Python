Num1 = int(input('Primeiro número: '))
Num2 = int(input('Segundo número: '))
Num3 = int(input('Terceiro número: '))
Num4 = int(input('Quarto número: '))
Num5 = int(input('Quinto número: '))
Num6 = int(input('Sexto número: '))
lista = [Num1, Num2, Num3, Num4, Num5, Num6]
soma = 0
for c in range(0, len(lista)):
    if (lista[c] % 2 == 0):
        soma += lista[c]
print('A soma dos valores pares é {}'.format(soma))

somas = 0
for c in range(1, 7):
    num = int(input('Digite o {}° valor: '.format(c)))
    if (num % 2 == 0):
        somas += num
print('A soma dos valores pares é {}'.format(somas))
