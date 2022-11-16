print('Soma de todos os numeros impares entre 0 e 500 é:')
s = 0
for c in range(0, 501):
    impares = c % 2
    multiplos = c % 3
    if impares != 0 and multiplos == 0:
        s = s + c

print(s)
