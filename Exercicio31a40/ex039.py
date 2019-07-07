import datetime

nascimento = int(input('Ano do nascimento: '))

anoAtual = datetime.date.today().year
idade = anoAtual - nascimento

print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, anoAtual))

if idade < 18:
    print('Faltam {} anos para seu alistamento'.format(18 - idade))
    print('Seu alistamento será no ano de {}'.format(anoAtual + (18 - idade)))
elif idade > 18:
    print('Já se passaram tantos {} anos do seu alistamento'.format(idade - 18))
    print('Seu alistamento foi no ano {}'.format(anoAtual - (idade - 18)))
else:
    print('Você está no ano de seu alistamento')
