# Aprovando Empréstimo
from time import sleep
imovel = float(input('Digite o valor do Imóvel que você deseja comprar: '))
salario = float(input('Digite o valor da sua remuneração mensal: '))
parcela = int(input('Em quantos anos você deseja pagar: '))
prestacao = float(imovel / (parcela*12))
part = float(prestacao / salario)*100
print(' '*25)
print('Aguarde enquanto calculamos os valores...')
sleep(5)
print(' '*25)
if part <= 30:
    print('APROVADO! Você deseja parcelar em {} parcelas no qual os valores ficaram em R${:.2f}'.format(parcela*12, prestacao))
    sleep(2)
    print(' '*25)
    continuar = str(input('Deseja continuar? '))
    if continuar == 'SIM':
        print(' '*25)
        print('ÓTIMO! Clica neste link para o envio das documentações')
    else:
        print(' '*25)
        print('Que pena, estamos à disposição!')
elif part > 30:
    print('REPROVADO! Você deseja parcelar em {} pacelas no qual os valores ficaram em R${:.2f} que ultrapassam 30% da sua remuneração mensal'.format(parcela*12, prestacao, part))