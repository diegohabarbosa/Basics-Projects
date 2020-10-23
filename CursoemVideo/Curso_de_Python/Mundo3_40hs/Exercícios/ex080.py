#080 - Lista ordenada sem repetições
valores = []
for cont in range(0,5):
    valor = int(input('Digite um valor: '))
    if cont == 0:
        valores.append(valor)
        print('Adicionado ao final da lista...')
    else:
        if valor >= max(valores):
            valores.insert(max(valores)+1, valor)
        if valor <= min(valores):
            valores.insert(min(valores)-1, valor)
        print(f'Adicionado na posição da lista...')
print(f'Os valores digitados em ordem foram {valores}')