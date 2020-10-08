# Primeiro e último nome de uma pessoa
# Diego Henrique de Almeida Barbosa
nome = str(input('Digite o nome completo: ')).strip().title().split()
print(f'Muito prazer em te conhecer!\n'
        f'Seu primeiro nome é {nome[0]}\n'
            f'Seu último nome é {nome[-1]}')
