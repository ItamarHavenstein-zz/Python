nome = input("Digite seu nome completo:").strip()

print('analisando seu nome...')
print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome)-nome.count(' ')))
primeiroNome = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(primeiroNome[0], len(primeiroNome[0])))
