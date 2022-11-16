import math
p = int(input('Pense em qualquer numero: '))
teste = p % 2
if teste == 0:
    print('O número {} é par'.format(p))
else:
    print('O numero {} é ímpar'.format(p))
