from datetime import date
ano = int(input('Digite um ano, caso não souber, digite 0: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print('O Ano de {} é Bissexto'.format(ano))
else:
    print('O ano de {} não é Bissexto'.format(ano))