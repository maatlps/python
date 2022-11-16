p = float(input('Qual a nota da sua prova? '))
t = float(input('Qual a nota do seu teste? '))
o = float(input('Quanto você tirou no trabalho? '))
s = t + o + p
d = s /2
print('Sua media é \033[30m{:.1f}'.format(d))
if d <= 5.0:
    print('\033[31mSua nota está ruim e você está de recuperação, estude mais!!!')
elif d == 5.0:
    print('\033[32mOk, você está na média.')
else:
    print('\033[35mSua Média é muita boa, meus parabéns')

