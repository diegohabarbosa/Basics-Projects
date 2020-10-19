# Maior e menor valores
from time import sleep
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
print(' ' * 30)
print('Por favor aguarde enquanto estamos analisando os números...')
sleep(3)
nmax = max(n1,n2,n3)
nmin = min(n1,n2,n3)
print(' ' * 30)
print('O número {} é o maior e o número {} é o menor'.format(nmax, nmin))