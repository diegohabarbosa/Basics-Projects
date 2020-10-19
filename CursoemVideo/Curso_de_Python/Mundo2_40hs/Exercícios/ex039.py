#Alistamento Militar
from time import sleep
from datetime import date
anonas = int(input('Digite o ano do seu nascimento: '))
idade = int(date.today().year - anonas)
alis = 18
print(' '*25)
print('Aguade enquanto calculamos...')
sleep(2)
print(' '*25)
if idade < 18:
    print('Faltam {} anos para você se alistar.'.format(alis-idade))
elif idade == 18:
    print('Você completou {} anos, você já pode se alistar'.format(idade))
else:
    print('Você já passou {} anos para se alistar, organize-se.'.format(idade-alis))