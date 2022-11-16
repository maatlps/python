num = int(input('Digite um numero: '))
print('Calculando {}!'.format(num))
count = num
f = 1
while count > 0:
    print('{}'.format(count), end=' ')
    print('x ' if count > 1 else '=', end='')
    f *= count
    count -= 1
print('',f)

