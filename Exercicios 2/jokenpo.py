from time import sleep
from random import randint
print('''ESCOLHA ENTRE:
\033[32m[0]\033[m PEDRA
\033[32m[1]\033[m PAPEL
\033[32m[2]\033[m TESOURA''')
sleep(1)
escolha = int(input('\033[4mDIGITE SUA ESCOLHA:\033[m'))
print('\033[31m-=-'*11)
computador = randint(0,2)
doubt = ('PEDRA','PAPEL','TESOURA')
if escolha == 0:
     carne = 'PEDRA'
elif escolha == 1:
    carne = 'PAPEL'
elif escolha == 2:
    carne = 'TESOURA'
lista = doubt[computador]
print('\033[m{:>5}:'.format('RESULTADO'))
print('\033[mVOCÊ ESCOLHEU {}.'.format(carne))
print('O COMPUTADOR ESCOLHEU {}.\033[m'.format(lista))
print('\033[31m-=-'*11)
if escolha == 0 and lista == 'TESOURA':
    print('VOCÊ VENCEU !!')
elif escolha == 0 and lista == 'PAPEL':
    print('O COMPUTADOR VENCEU !!')
elif escolha == 0 and lista == 'PEDRA':
    print('EMPATE !!')
elif escolha == 1 and lista == 'TESOURA':
    print('O COMPUTADOR VENCEU !!')
elif escolha == 1 and lista == 'PAPEL':
    print('EMPATE !!')
elif escolha == 1 and lista == 'PEDRA':
    print('VOCÊ VENCEU !!')
elif escolha == 2 and lista == 'PEDRA':
    print('O COMPUTADOR VENCEU !!')
elif escolha == 2 and lista == 'PAPEL':
    print('VOCÊ VENCEU !!')
elif escolha == 2 and lista == 'TESOURA':
    print('EMPATE !!')
else:
    print('INVALIDO.')

