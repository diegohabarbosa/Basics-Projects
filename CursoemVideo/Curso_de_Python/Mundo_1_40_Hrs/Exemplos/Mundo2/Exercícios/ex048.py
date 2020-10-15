#048 - Soma ímpares múltiplos de três
s = 0
for c in range(1,501,2):
    if c% 3 ==0:
        print(c, end=' ')
        s += c
    else:
        0
print(s)
