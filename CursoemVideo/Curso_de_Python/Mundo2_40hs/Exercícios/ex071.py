#071 - Simulador de Caixa Eletrônico
print('='*40)
print('{:^40}'.format('BANCO DO CEV'))
print('='*40)
valor = int(input('Que valor você deseja sacar? R$'))
total = valor
cedula = 50
totalcedulas = 0
while True:
    if total >= cedula:
        total -= cedula    
        totalcedulas += 1
    else:
        if totalcedulas > 0:
            print(f'Total de {totalcedulas} Cédulas de R${cedula},00')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 2
        totalcedulas = 0
        if total == 0:
            break          
print('Volte sempre ao BANCO DO CEV! Tenha um bom dia!')