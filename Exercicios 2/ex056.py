from datetime import date
ano = date.today().year
s = 0
maisv = 0
nomemaisv = ''
count = 0
for c in range(1,5):
    print('---- {} PESSOA ----:'.format(c))
    nome = str(input('NOME: ')).strip().upper()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [F/M]:')).strip().upper()
    s += idade
    if idade == 1:
        maisv = idade
        nomemaisv = nome
    if sexo == 'M' and idade > maisv:
        maisv = idade
        nomemaisv = nome
    if sexo == 'F' and idade < 20:
        count += 1

print('O HOMEM MAIS VELHO SE CHAMA {} E TEM {} ANOS'.format(nomemaisv, maisv))
print('A MÉDIA DE IDADE DAS PESSOAS É DE {} ANOS'.format(s/4))
print('EXISTEM {} MULHERES ABAIXO DE 20 ANOS'.format(count))