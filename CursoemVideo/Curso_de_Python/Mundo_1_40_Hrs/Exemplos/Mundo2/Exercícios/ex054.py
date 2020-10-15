#054 - Grupo da Maioridade
from datetime import date
a = 0
b = 0
d = date.today().year
for c in range(0,7):
    n = int(input('Digite o ano de nascimento: '))
    m = (d-n)
    if m >= 21:
        a += 1
    else:
        b += 1
print('{} atingiram a maioridade'.format(a))
print('{} não atingiram a maioridade'.format(b))