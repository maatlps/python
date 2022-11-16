from random import randint
numpc = randint(0,10)
print('PENSE EM UM NUMERO DE 0 A 10: ')
count = 0
p = 0
while p != numpc:
    p = int(input('Digite um numero: '))
    count += 1
    if p != numpc:
        print('Você disse o numero {}, está errado, tente novamente.'.format(p))
        if p > 10:
            print('Esse numero é maior do que 10, idiota')
print('\033[32mVOCÊ FINALMENTE ACERTOU E PRECISOU DE {} TENTATIVAS PARA ACERTAR!!!'.format(count))