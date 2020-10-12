# Radar Eletrônico
velocidade = int(input('Digite a velocidade do carro: '))
multa = (velocidade-80)*7
if velocidade <= 80:
    print('\033[32m'+'PARABÉNS você transitou dentro do limite de velocidade!')
    print('Dirija sempre com segurança.')
else:
    print('\033[31m'+'MULTADO! Atenção você transitou acima da velocidade permitida de 80 km/h')
    print('Você pagará uma multa de R${:.2f}!'.format(multa))