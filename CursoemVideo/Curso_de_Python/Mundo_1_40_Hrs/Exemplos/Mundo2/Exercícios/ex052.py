#052 - Números primos
n = int(input('Digite um número: '))
d1 = (n // n)
d2 = (n % 2)
if n != 1 and d1 == 1 and d2 != 0:
    print('O {} é um número primo!'.format(n))
else:
    print('O {} não é um número primo!'.format(n))