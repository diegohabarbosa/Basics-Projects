#075 - Análise de dados em uma Tupla
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
nt = (n1, n2, n3, n4)
print(f'Você digitou os valores {nt}')
print(f'O valor 9 apareceu {nt.count(9)} vezes')
if nt.count(3) == 0:
    print('O valor 3 não foi digitado em nenhuma posição')
else:
    print(f'O valor 3 apareceu {nt.count(3)} vezes')
print(f'Os valores pares digitados foram ',end='')
for c in nt:
    if c % 2 == 0:
        print(c, end=' ')