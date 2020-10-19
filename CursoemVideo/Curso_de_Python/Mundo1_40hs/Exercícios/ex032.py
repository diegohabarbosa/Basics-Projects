# Ano Bissexto
from datetime import date
ano = int(input('Digite um ano para saber se é Bissexto: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O Ano {} é Bissexto'.format(ano))
else:
    print('O Ano {} não é Bissexto'.format(ano))