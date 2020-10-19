#067 - Tabuada v3.0
t = 0
n = 1
while n >= 0:
    print('--'*20)
    n = int(input('Digite um número para ver sua tabuada: '))
    print('--'*20)
    if n < 0:
        break
    for c in range(1,11):
        t = n*c
        print('{} x {} = {}'.format(n,c,t))
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')