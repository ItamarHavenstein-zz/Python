import math

angulo = float(input('Digite o ângulo que você deseja: '))

radiano = math.radians(angulo)

print('O ângulo de {:.1f} tem o SENO de {:.2f}'.format(angulo, math.sin(radiano)))
print('O ângulo de {:.1f} tem o COSSENO de {:.2f}'.format(angulo, math.cos(radiano)))
print('O ângulo de {:.1f} tem a TANGENTE de {:.2f}'.format(angulo,math.tan(radiano)))
