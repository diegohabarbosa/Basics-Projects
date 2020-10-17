#063 - Sequência de Fibonacci v1.0 -- Fn = Fn - 1 + Fn - 2
a = 0
p = 0
n = int(input('Digite o número de sequência: '))
n2 = n**2
while p < n2:
    print(p, end=', ')
    p = p + a
    a = p - a
    if p == 0:
        p = p + 1
print(p)