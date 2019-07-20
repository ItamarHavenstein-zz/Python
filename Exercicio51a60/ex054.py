from datetime import date

ano = date.today().year
maiorDeIdade = 0
menorDeIdade = 0

for c in range(1, 8, 1):
    pessoa = int(input('Em que ano a {}° pessoa nasceu? '.format(c)))
    idade = ano - pessoa
    if idade >= 18:
        maiorDeIdade += 1
    else:
        menorDeIdade += 1

print('Ao todo tivemos {} pessoas maiores de idade'
      '\nE também tivemos {} pessoas menores de idade.'.format(maiorDeIdade, menorDeIdade))
