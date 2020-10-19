#070 - Estatísticas em produtos
cont = soma = quant = 0
chave = 'x'
continuar = 'x'
print('--'*20)
print('         LOJA SUPER BARATÃO          ')
print('--'*20)
while continuar not in 'Nn':
    produto = str(input('Nome do Produto: ')).strip().title()
    preco = float(input('Preço: R$'))
    soma += preco
    quant += 1
    if preco >= 1000:
        cont += 1
    if quant == 1:
        menor = preco
    else:
        if preco < menor:
            menor = preco
            chave = produto
    continuar = 'x'
    while continuar not in 'SsNn':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
print('')
print('-------------- FIM DO PROGRAMA --------------')
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {cont} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {chave} que custa {menor:.2f}')