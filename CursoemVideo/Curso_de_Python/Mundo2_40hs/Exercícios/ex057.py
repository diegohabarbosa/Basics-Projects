#057 - Validação de Dados
sexo = str(input('Informe o seu sexo [F/M]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Opção Invalida! Informe o seu sexo [F/M]: ')).strip().upper()[0]
if sexo == 'M':
    sexo = 'masculino'
elif sexo == 'F':
    sexo = 'feminino'
print('Sexo {} regisitrado com sucesso!'.format(sexo))
