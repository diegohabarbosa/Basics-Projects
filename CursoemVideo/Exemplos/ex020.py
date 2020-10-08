# Sorteando uma ordem na lista
import random
n1 = input('Digite o nome: ')
n2 = input('Digite o nome: ')
n3 = input('Digite o nome: ')
n4 = input('Digite o nome: ')
alunos = [n1, n2, n3, n4]
random.shuffle(alunos)
print('A ordem da apresentação será {}'.format(alunos))