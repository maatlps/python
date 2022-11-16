n = input('Digite seu nome completo:')
upper = n.upper()
lower = n.lower()
name = n.split()
first = len(name[0])
divido = ''.join(name)
lengh = len(divido)
print('Seu nome com todas as letras maiúsculas fica {}\nCom todas minúsculas fica {}\nSeu primeiro nome tem {} letras'.format(upper,lower,first))
print('E seu nome, sem espaços tem o total de {} letras'.format(lengh))



