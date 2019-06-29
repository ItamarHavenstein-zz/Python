from random import randint
from time import sleep

palpite = int(input('advinhe qual número estou pensando de 0 a 5? '))

pensado = randint(0, 5)
print('Processando!!!!')
sleep(2)

if palpite == pensado:
    print('Você acertou o número!!')
else:
    print('Infelizmente você não acertou!!!, eu pensei {} e não no {}'.format(pensado, palpite))
