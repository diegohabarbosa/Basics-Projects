# Aumentos múltiplos
s = float(input('Digite o sálario do colaborador: '))
if s<=1250.00:
    print('O salário terá um reajuste de 15% e valor reajustado será de R${:.2f}'.format(s*1.15))
else:
    print('O salário terá um reajuste de 10% e valor reajustado será de R${:.2f}'.format(s*1.10))
