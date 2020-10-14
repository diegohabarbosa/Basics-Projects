# Classificando Atletas
from datetime import date
ano = int(input('Digite o ano de nascimento do atleta: '))
idade = date.today().year - ano
if idade <=9:
    print('O atleta está na categoria MIRIM')
elif idade >9 and idade <=14:
    print('O atleta está na categoria INFANTIL')
elif idade >14 and idade <=19:
    print('O atleta está na categoria JUNIOR')
elif idade >19 and idade <=25:
    print('O atleta está na categoria SÊNIOR')
else:
    print('O atleta está na categoria MASTER')