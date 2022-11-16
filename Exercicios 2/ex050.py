teste = str(input('Digite uma frase: ')).strip().upper()
separado = teste.split()
junto = ''.join(separado)
inverso = ''
for c in range(len(junto) -1, -1, -1):
    inverso = inverso + junto[c]
print('{} AO CONTRÁRIO FICA {}'.format(teste, inverso))
if inverso == junto:
    print('{} É UM PALINDROMO'.format(teste))
else:
    print('{} NÃO É UM PALINDROMO'.format(teste))