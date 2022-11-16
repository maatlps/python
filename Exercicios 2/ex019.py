from math import sin, cos, tan, radians
angulo = float(input('Forneça o angulo:'))
coseno = cos(radians(angulo))
seno = sin(radians(angulo))
tangente = tan(radians(angulo))
print('O Coseno é {:.2f}\nO Seno é {:.2f}\nA Tangente é {:.2f}'.format(coseno, seno, tangente))
