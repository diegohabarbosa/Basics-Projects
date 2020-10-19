#063 - Sequência de Fibonacci v1.0 -- Fn = Fn - 1 + Fn - 2
t1 = 0
t2 = 1
n = int(input('Digite o número de sequência: '))
print('{} ➝  {}'.format(t1, t2), end=' ➝  ')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(t3, end=' ➝  ')
    t1 = t2
    t2 = t3
    cont += 1
print('Fim')