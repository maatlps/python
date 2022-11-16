n = int(input('Digite um numero: '))
count = 0
for c in range(1, n+1):
    r = n % c
    t = n // c
    if r == 0:
        print('{} foi divido por {} e deu {}'.format(n, c, t))
        count += 1
if 0 < count <= 2:
    print('O numero foi divido {} vezes portanto ele é primo'.format(count))
elif count > 2:
    print('O numero foi dividido {} vezes portanto ele não é primo'.format(count))
elif count == 0:
    print('0 não é divisivel por nenhum numero.')