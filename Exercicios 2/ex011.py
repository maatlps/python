h = float(input('Qual é o tamanho, em metros, da sua parede?'))
b = float(input('Qual a Largura?'))
area = b * h
print('Será necessario \033[1;35m{:.3f}l\033[m para pintar a parede.'.format(area/2))
