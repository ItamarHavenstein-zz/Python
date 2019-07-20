frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
contrario = junto[::-1]#colocar a frase ao contrario

print('O inverso de {} é {}'.format(junto, contrario))

if junto == contrario:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo!')
