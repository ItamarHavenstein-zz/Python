nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1 + nota2) / 2

print('Notas {}, {} tem média igual a {}'.format(nota1, nota2, media))
if media < 5:
    print('Você está REPROVADO')
elif media >= 7:
    print('Você está APROVADO')
else:
    print('Você está em RECUPERAÇÂO')
