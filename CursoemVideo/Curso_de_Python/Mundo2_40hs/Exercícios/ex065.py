#065 - Maior e Menor valores
b = 0
c = 0
ma = 0
mi = 0
s = int(input('Digite um número inteiro: '))
while s != 'S':
    b += s 
    c += 1
    if s > ma:
        ma = s
    elif s < mi:
        mi = s           
    x = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if x == 'S':
        s = int(input('Digite um número inteiro: '))
        b += s 
        c += 1
        if s > ma:
                ma = s
        elif s < mi:
                mi = s
        break       
print('A média total dos valores foi de {}.'.format(b/(c-1)))
print('O {} é o menor valor e o {} é o maior valor'.format(mi, ma))