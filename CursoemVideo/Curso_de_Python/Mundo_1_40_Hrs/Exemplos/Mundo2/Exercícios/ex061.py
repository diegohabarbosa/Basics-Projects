#061 - Progressão Aritmética v2.0
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = p + (10 - 1) * r
while p < d:
    print(p, end='➝ ')
    p += r
print(d)