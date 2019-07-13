peso = int(input('Digite seu peso(Kg): '))
altura = float(input('Digite sua Altura(metros): '))

imc = peso / (altura ** 2)

print('Sua massa corporal é {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal, procure um médico')
elif imc > 18.5 and imc < 25:
    print('Você está com o PESO IDEAL ')
elif imc > 25 and imc < 30:
    print('Você está com SOBREPESO, tome cuidade ')
elif imc > 30 and imc < 40:
    print('Você está com OBESIDADE, atenção a sua alimentação ')
else:
    print('Você está com OBESIDADE MORBIDA, procure um médico')
