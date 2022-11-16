print('='*25)
print('{:^5}'.format('PROGRESSÃO ARITMÉTICA'))
print('='*25)
n = int(input('PRIMEIRO TERMO: '))
r = int(input('RAZÃO: '))
pn = n + (10-1) * r
for c in range(n,pn, r):
    print('{} -> '.format(c), end='')
print('ACABOU')

