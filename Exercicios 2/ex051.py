import datetime
ano = datetime.date.today().year
pessoas = 0
count = 0
countm = 0
for c in range(1,8):
    print('\033[31mPESSOA {}\033[m'.format(c))
    nomes = int(input('EU QUE ANO ANO NASCEU A {} PESSOA? '.format(c)))
    idade = ano - nomes
    pessoas += 1
    if idade >= 18:
        count += 1
    else:
        countm += 1
print('Das {} pessoas que você falou, {} são maiores de idade e {} são menores'.format(pessoas, count, countm))