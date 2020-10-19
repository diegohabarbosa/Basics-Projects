#062 - Super Progressão Aritmética v3.0
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = p + (10) * r
t2 = r
while p < d:
    print(p, end='➝ ')
    p += r
    while p >= d:
        x = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]         
        if x == 'S':    
            t = int(input('Quantos termos você deseja adicionar?: '))
            t2 += t
            d = p + (t) * r
            print(p, end='➝ ')
            p += r
        break
print('Progressão finalizada com {} termos mostrado.'.format(r+t2))