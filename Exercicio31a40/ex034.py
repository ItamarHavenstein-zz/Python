salario = float(input('Digite o valor do seu salário: '))

if salario <= 1250:
    novoSalario = salario + (salario * 0.15)
else:
    novoSalario = salario + (salario * 0.10)
print('Seu novo salário será de {:.2f}R$'.format(novoSalario))
