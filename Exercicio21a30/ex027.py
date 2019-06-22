nome = str(input('Digite seu nome completo: ')).strip()

lista = nome.split()

print('Um prazer em lhe conhecer!\n Seu primeiro nome: {} \n Seu último nome: {}'.format(lista[0], lista[len(lista)-1]))

