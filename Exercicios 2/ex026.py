frase = str(input('Digite uma frase: ')).lower().strip()
a = frase.count('a')
first = frase.find('a') + 1
last = frase.rfind('a')
print('A letra "a" aparece {} vezes'.format(a))
print('A primeira vez em que aparece, ela esta na posição {}'.format(first))
print('A ultima vez em que aparece, está na posição {}'.format(last))

