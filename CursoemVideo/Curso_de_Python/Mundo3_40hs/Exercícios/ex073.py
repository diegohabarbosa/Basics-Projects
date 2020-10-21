#073 - Tuplas com Times de Futebol
time = 'x'
tabela = ('Internacional','Flamengo','Atlético-MG','São Paulo','Santos','Fluminense','Fortaleza','Palmeiras','Atlético-GO','Grêmio','Sport','Bahia','Ceará','Botafogo','Vasco','Corinthians','Athletico-PR','Coritiba','Bragantino','Goiás')
while time not in tabela:
    time = str(input('Digite o time da tabela para ver a posição: ')).strip()   
posicao = tabela.index(time)+1
print('-='*20)
print(f'Lista de times do Brasileirão: {tabela}')
print('-='*20)
print(f'Os 5 primeiros são {tabela[:5]}')
print('-='*20)
print(f'Os 4 últimos são {tabela[16:]}')
print('-='*20)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print('-='*20)
print(f'O {time} está na {posicao}ª posição')