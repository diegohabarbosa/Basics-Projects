#049 - Tabuada v.2.0
t = 0
n = int(input('Digite um número para ver sua tabuada: '))
for c in range(1,11):
    t = n*c
    print('{} x {} = {}'.format(n,c,t))