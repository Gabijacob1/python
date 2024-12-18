import random

maior = 0
quant = 0

for c in range(10):
    n = random.randrange(1,101)
    quant += 1
    if quant ==1:
        maior = n

    else:
        if n > maior:
            maior = n
 
    print(n)
print(' O Número de maior valor gerado foi: ', maior)