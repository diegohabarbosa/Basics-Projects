#Gerenciador de Pagamentos
from time import sleep
valor = float(input('Digite o valor do produto R$'))
print(' '*20)
print('Digite o digito da condição de pagamento sendo:')
print('[1] - dinheiro / cheque')
print('[2] - à vista no cartão')
print('[3] - em até 2x no cartão de crédito')
print('[4] - 3x ou mais no cartão de crédito')
print(' '*20)
sleep(5)
condicao = int(input('Escolha a condição de pagamento (1 à 4): '))
if condicao == 1:
    print('Você receberá um desconto de 10% nesta compra no valor total de R${:.2f}'.format(valor*0.9))
elif condicao == 2:
    print('Você receberá um desconto de 5% nesta compra no valor total de R${:.2f}'.format(valor*0.95))
elif condicao == 3:
    print('O valor total da compra foi de R${:.2f}'.format(valor))
elif condicao == 4:
    print('Será aplicado um juros de 20% nesta compra no valor total de R${:.2f}'.format(valor*1.2))
else:
    print('Opção invalida. Tente novamente!')