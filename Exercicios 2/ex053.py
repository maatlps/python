n = int(input('DIGITE UM NUMERO: '))
total = 0
for c in range(1, n + 1):
    if n % c == 0:
        total = total + 1
        print('\033[31m',end='')
    else:
        print('\033[m',end='')
    print(c,end='  ')
print('\n\033[mO numero {} foi dividido {} vezes,'.format(n,total), end=' ')
if total > 2:
    print('portanto o número {} NÃO é PRIMO'.format(n))
else:
    print('portanto o número {} É PRIMO'.format(n))

