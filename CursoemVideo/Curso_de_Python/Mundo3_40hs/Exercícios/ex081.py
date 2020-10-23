#081 - Extraindo dados de uma Lista
valores = []
continuar = 'x'
while continuar not in 'Nn':
    continuar = 'x'
    valor = valores.append(int(input('Digite um valor: ')))
    while continuar not in 'SsNn':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
print(valores)
print(valores.reverse())
print(f'Você digitou {len(valores)} elementos.')
print(f'Os valores em ordem decrescente são {valores.reverse()}')
if valores.count(5) == 0:
    print('O valor 5 NÃO faz parte desta lista')
else:
    print('O valor 5 faz parte desta lista!')