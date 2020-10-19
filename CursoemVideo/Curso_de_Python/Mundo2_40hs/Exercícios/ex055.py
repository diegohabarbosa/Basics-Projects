#055 - Maior e menor da sequência
ma = 0
mi = 0
for c in range(0, 5):
    p = float(input('Digite o peso da {}ª pessoa: '.format(c+1)))
    if c+1 == 1:
        ma = p
        mi = p
    else:
        if p > ma:
            ma = p
        elif p < mi:
            mi = p 
print('O menor peso lido foi de {} Kgs'.format(mi))
print('O maior peso lido foi de {} Kgs'.format(ma))