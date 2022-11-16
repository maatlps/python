s = 0
count = 0
for c in range(0, 6):
    n = int(input('Digite um numero numero: '))
    pares = n % 2
    s = s + n
    count = count + 1
if pares == 0:
    print('Todos os numeros são pares e a soma de todos eles é', s)
else:
    print('Invalid.')










