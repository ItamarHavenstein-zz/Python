primeiro = int(input('Digite o primeiro numero: '))
segundo = int(input('Digite o segundo numero: '))
terceiro = int(input('Digite o terceiro numero: '))

maior = 0
menor = 0
medio = 0

if primeiro > segundo:
    maior = primeiro
    menor = segundo
else:
    maior = segundo
    menor = primeiro
if maior > terceiro:
    medio = terceiro
else:
    maior = terceiro
    medio = maior
if menor > medio:
    menor = medio

print('O menor valor digitado foi ', menor)
print('O maior valor digitado foi ', maior)