from random import randint
sorteio = int(input('Tente acertar o numero de 0 a 5 que eu estou pensando: '))
sort = randint(0,5)
print('o numero sorteado é {}'.format(sort))
if sorteio == sort:
    print('Incrivel, você acertou o numero.')
else:
    print('Quase! Tente novamente.')

