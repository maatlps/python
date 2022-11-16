print('Digite o nome e o peso de 5 pessoas e eu te mostrarei a mais gorda.')
maior = 0
menor = 0
for c in range(1,6):
    peso = float(input('{} pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é {}kg e o menor é {}kg'.format(maior, menor))




