#054 - Grupo da Maioridade
from datetime import date
x = 0
d = date.today().year
for c in range(0,7):
    n = int(input('Digite o ano de nascimento: '))
    m = (d-n)
    if m >= 18:
        1
    else:
        0
print(c)
print('{} Atingiram a maioridade'.format(x))