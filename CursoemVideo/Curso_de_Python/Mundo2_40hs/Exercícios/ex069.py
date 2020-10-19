#069 - Análise de dados do grupo
continuar = 'x'
sexo = 'x'
maior = homem = mulher = 0
t = 1
while continuar not in 'Nn':
    print('--'*20)
    print('         CADASTRE UMA PESSOA         ')
    print('--'*20)
    idade = int(input('Idade: '))
    sexo = 'x'
    while sexo not in 'MmFf':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade > 18:
        maior += 1
    if sexo in 'Mm':
        homem += 1
    if sexo in 'Ff' and idade < 20:
        mulher += 1
    continuar = 'x'
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
print('--'*20)
print('============= FIM DO PROGRAMA =============')
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'E temos {mulher} mulheres com menos de 20 anos')