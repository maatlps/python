a = int(input('Digite um Valor: '))
b = int(input('Digite um segundo valor: '))
c = int(input('Digite um terceiro valor'))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
menor = b
if a < b and a < c:
    menor = a
if c < a and c < b:
    menor = c
print('O Maior valor é o: {}'.format(maior))
print('O Menor valor é o: {}'.format(menor))