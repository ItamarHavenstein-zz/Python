somaIdade = 0
pessoaMaisVelha = 0
pessoaMaisVelhaNome = ""
mulheresMenosVinte = 0

for p in range(1, 5, 1):
    print('----- {}° PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()#para tirar os espaços
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    somaIdade += idade
    if sexo == "M":
        if pessoaMaisVelha < idade:
            pessoaMaisVelha = idade
            pessoaMaisVelhaNome = nome
    if sexo == "F" and idade < 20:
        mulheresMenosVinte += 1
print('A média de idade do grupo é de {:.1f} anos'
      '\nO homem mais velho tem {} anos e se chama {}.'
      '\nAo todo são {} mulheres com menos de 20 anos.'
      .format((somaIdade/4), pessoaMaisVelha, pessoaMaisVelhaNome, mulheresMenosVinte))
