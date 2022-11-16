km = float(input('Quantos km você rodou com seu carro alugado?'))
dia = int(input('Quantos dias você ficou com ele'))
pago = (0.15 * km) + (60 * dia)
print('Você deve pagar R${:.2f}'.format(pago))
