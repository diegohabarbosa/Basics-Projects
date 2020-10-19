import math
#from math import srqt, floor, ceil
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))
print('A raiz de {} é igual a {} arredondado para cima'.format(num, math.ceil(raiz)))
print('A raiz de {} é igual a {} arredondado para baixo'.format(num, math.floor(raiz)))
print('A raiz de {} é igual a {:.2f} exponencial'.format(num, math.expm1(raiz)))
