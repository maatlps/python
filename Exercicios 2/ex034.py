r1 = float(input('Digite um valor:'))
r2 = float(input('Digite outro valor:'))
r3 = float(input('Digite outro valor:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possivel formar um triangulo ')
    if r1 == r2 == r3:
        print('EQUILATERO')
    elif r1 == r2 or r1 == r3:
        print('ISÓSCELES')
    elif r1 != r2 != r3 !=r1:
        print('ESCALENO')
else:
    print('Não é possivel formar um triangulo com estes valores')