# Radar Eletrônico
v = int(input('Digite a velocidade do carro: '))
if v <= 80:
    print('Parabéns você transitou dentro do limite de velocidade!')
else:
    print('Atenção você transitou acima da velocidade permitida de 80 km/h')
    print('Você pagará uma multa de R${:.2f}'.format((v-80)*7))
