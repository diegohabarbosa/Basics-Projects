#060 - Cálculo do Fatorial
n2 = 1
n = int(input('Digite um número: '))
print('{}! = '.format(n), end='')
while 1 < n:
    print(n, end='x')
    n2 = n2*n
    n -= 1
print('{} = {}'.format(n, n2))