print('Analise de triângulo ')
reta1 = float(input('Digite o valor da reta1: '))
reta2 = float(input('Digite o valor da reta2: '))
reta3 = float(input('Digite o valor da reta3: '))

correto = 0
if reta1 - reta2 < reta3 < reta1 + reta3:
    correto = correto + 1
if reta1 - reta3 < reta2 < reta1 + reta3:
    correto = correto + 1
if reta3 - reta2 < reta1 < reta3 + reta2:
    correto = correto + 1

if correto == 3:
    print('Com as 3 retas conseguimos formar um triângulo !!')
else:
    print('Não forma um triângulo!!')
