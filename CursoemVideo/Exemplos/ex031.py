# Custo da viagem
km = float(input('Digite a distância do percurso da sua viagem em km: '))
if km <= 200:
    print('O preço da sua passagem será R${:.2f}'.format(km*0.50))
else:
    print('O preço da sua passagem será R${:.2f}'.format(km*0.45))
