altura = float(input('Qual é a sua altura em metros '))
peso = float(input('Quanto você pesa? '))
imc = peso / (altura * altura)
print('Seu imc é: \033[30m{:.1f}'.format(imc))
if imc <= 18.5:
    print('Cuidado, você está abaixo do peso ideal')
elif imc >= 18.5 and imc <= 25:
    print('Parabéns, você está no peso correto')
elif imc > 25 and imc <= 30:
    print('Você está Sobrepeso.')
elif imc > 30 and imc <= 40:
    print('Procure tratamento, você está obeso')
elif imc > 40:
    print('Você é um obeso morbido, idiota.')