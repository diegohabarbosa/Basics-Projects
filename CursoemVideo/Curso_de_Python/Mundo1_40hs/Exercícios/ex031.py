# Custo da viagem por km
from time import sleep
km = float(input('Digite a distância do percurso da sua viagem em km: '))
print('ATENÇÃO! ESTAMOS CALCULANDO O PREÇO DA SUA ROTA...')
sleep(3)
if km <= 200:
    print('O preço da sua passagem será R${:.2f}'.format(km*0.50))
else:
    print('O preço da sua passagem será R${:.2f}'.format(km*0.45))
