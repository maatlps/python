p = 0
while p != 5:
    t = int(input('Digite um valor: '))
    c = int(input('Digite outro: '))
    print('''O QUE VOCÊ DESEJA FAZER COM ESSES DOIS VALORES?
    [1] SOMAR
    [2] MULTIPLICAR 
    [3] DIZER O MAIOR
    [4] DIZER NOVOS NUMEROS
    [5] SAIR DO PROGRAMA''''')
    p = int(input('Digite sua escolha: '))
    if p == 1:
        s = t + c
        print('A soma de {} e {} é {}'.format(t, c, s))
    if p == 2:
        razao = t * c
        print('A razão entre {} e {} é {}'.format(t, c, razao))
    if p == 3:
        if t > c:
            print('{} é maior que {}'.format(t,c))
        elif t < c:
            print('{} é maior que {}'.format(c,t))
        else:
            print('Os numeros digitados são iguais.')
    if p > 5:
        print('Essa alternativa não existe.')
print('Obrigado por me usar xD')


