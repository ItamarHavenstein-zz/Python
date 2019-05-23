metros = float(input('Digite uma distância em metros: '))

print('A medida de {}m corresponde a '.format(metros))
print('{}km'.format(metros * .001))
print('{}hm'.format(metros * .01))
print('{:.1f}dam'.format(metros * .1))
print('{:.0f}dm'.format(metros * 10))
print('{:.0f}cm'.format(metros * 100))
print('{:.0f}mm'.format(metros * 1000))
