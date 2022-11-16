Km = float(input('Quantos Km é a sua viagem? '))
if Km <= 200:
    p = Km * 0.50
    print('A passagem será de: R${:.2f}'.format(p))
else:
    passagem = Km * 0.45
    print('A passagem será R${:.2f}'.format(passagem))
