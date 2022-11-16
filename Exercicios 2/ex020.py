import random
a1 = input('Digite o nome do primeiro aluno:')
a2 = input('Do segundo:')
a3 = input('Do terceiro:')
a4 = input('Do quarto:')
lista = (a1,a2,a3,a4)
sorteio = random.choice(lista)
print('O aluno sorteado foi', sorteio)




