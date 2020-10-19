# Comparando números
from time import sleep
n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))
print(' '*25)
print('Aguarde enquanto estamos comparando os números...')
sleep(3)
print(' '*25)
if n1 > n2:
    print('O primeiro valor é maior')
elif n1 < n2:
    print('O segundo valor é maior')
elif n1 == n2:
    print('Não existe valor maior. Os dois são iguais')