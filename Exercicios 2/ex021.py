import random
n1 = input('Digite o nome do(a) primeiro(a) aluno(a):')
n2 = input('Segundo(a):')
n3 = input('Terceiro(a):')
n4 = input('Quarto(a):')
lista = [n1,n2,n3,n4]
r = random.shuffle(lista)
print('A ordem de apresentação será:{}')
print(lista)

