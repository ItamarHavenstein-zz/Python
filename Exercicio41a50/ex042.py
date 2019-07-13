print('Analise de triângulo ')
reta1 = float(input('Digite o valor do primeiro segmento: '))
reta2 = float(input('Digite o valor do segundo segmento: '))
reta3 = float(input('Digite o valor do terceiro segmento: '))

correto = 0
if reta1 - reta2 < reta3 < reta1 + reta3:
    correto = correto + 1
if reta1 - reta3 < reta2 < reta1 + reta3:
    correto = correto + 2
if reta3 - reta2 < reta1 < reta3 + reta2:
    correto = correto + 1

if correto == 3:
    if reta1 == reta2 == reta3:
        print('Podemos formar um triângulo, Tipo EQUILÁTERO!!')
    elif reta1 != reta2 != reta3 != reta1:
        print('Podemos formar um triângulo, Tipo ESCALENO')
    else:
        print('Podemos formar um triângulo, Tipo ISÓSCELES')
else:
    print('Não forma um triângulo!!')
