# Sorteando um item na lista
import random
n1 = input('Digite o primeiro nome: ')
n2 = input('Digite o segundo nome: ')
n3 = input('Digite o terceiro nome: ')
n4 = input('Digite o quarto nome: ')
alunos = [n1,n2,n3,n4]
x = random.choice(alunos)
print('O aluno escolhido foi {}'.format(x))

