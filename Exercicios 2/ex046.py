print('\033[31m{:=^50}'.format(' TABUADA '))
n = int(input('\033[mDigite um numero: '))
for c in range(0,11):
    print('{} x {} = '.format(n,c),end='')
    p = c * n
    print(p)
print('\033[31m='*50)

