salario = float(input('Qual o seu Salário? R$'))
dez = (10*salario) / 100
quinze = (15*salario) / 100
if salario <=1250:
    print('Voce obteve um aumento de 15% no seu salario e passara a receber R${:.2f}'.format(salario + quinze))
else:
    print('Você obteve um aumento de 10% no seu salario e passara a receber RS{:.2f}'.format(salario + dez))
