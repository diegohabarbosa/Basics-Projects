#055 - Maior e menor da sequência
mi = 0
ma = 0
for c in range(0,5):
    p = float(input('Digite o peso: '))
    mi = min(p)
    ma = max(p)  
print('{} foi o menor peso e o {} foi o maior peso'.format(mi, ma))

