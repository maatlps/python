from math import hypot
oposto = float(input('Cateto oposto:'))
adj = float(input('Cateto adjacente:'))
hyp = hypot(oposto, adj)
print('O valor da Hipotenusa é {:.2f}'.format(hyp))