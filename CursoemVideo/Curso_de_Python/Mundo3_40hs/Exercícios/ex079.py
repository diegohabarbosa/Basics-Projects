#079 - Valores únicos em uma Lista
valores = []
continuar = 'x'
while continuar not in 'Nn':
    continuar = 'x'
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar ...')
    while continuar not in 'SsNn':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
print(f'Você digitou os valores {sorted(valores)}')        