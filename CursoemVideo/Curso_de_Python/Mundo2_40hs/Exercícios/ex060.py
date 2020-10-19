#060 - Cálculo do Fatorial
'''
n2 = 1
n = int(input('Digite um número: '))
print('{}! = '.format(n), end='')
while 1 < n:
    print(n, end=' x ')
    n2 = n2*n
    n -= 1
print('{} = {}'.format(n, n2))
'''

from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
n2 = 1
f = factorial(n)
print('O Fatorial de {}! = '.format(n), end='')
while 1 < n:
    print(n, end=' x ')
    n2 = n2*n
    n -= 1
print('{} = {}.'.format(n, f))