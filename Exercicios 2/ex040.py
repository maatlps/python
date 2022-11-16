value = float(input('Qual valor da casa? R$'))
sallary = float(input('Quanto você ganha por mês? R$'))
parc = int(input('Em quantas parcelas? '))
prestação = value / parc
if prestação > 30 * sallary/100:
    print('\033[31mVocê não pode fazer este empréstimo')
else:
    print('\033[34m-=-' * 20)
    print('Seu Empréstimo de {:.2f} foi aprovado!!!'.format(value))
    print('A sua parcela será de \033[35mR${:.2f}\033[m, por mês'.format(prestação))

