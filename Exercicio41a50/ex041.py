import datetime

nascimento = int(input('Digite seu ano de nascimento: '))

anoAtual = datetime.date.today().year
idade = anoAtual - nascimento

print('A idade do atleta é {}'.format(idade))

if idade <= 9:
    print('A categoria do atleta é MIRIM')
elif idade > 9 and idade <= 14:
    print('A categoria do atleta é INFANTIL')
elif idade > 14 and idade <= 19:
    print('A categoria do atleta é JUNIOR')
elif idade > 19 and idade <= 25:
    print('A categoria do atleta é SÊNIOR')
else:
    print('A categoria do atleta é MASTER')
