import random

aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')

pessoas = [aluno1,aluno2,aluno3,aluno4]

'''sorteado = pessoas[random.randrange(len(pessoas))]'''
sorteado = random.choice(pessoas)
print('O aluno sorteado foi : ',sorteado)
