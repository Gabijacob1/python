pares = 0
impar = 0
for x in range(10):
    n = int(input("Digite um número:"))
    if (n % 2 == 0):
        pares = pares + 1
    else:
        impar = impar+1

print(pares, "números pares")
print((10 - pares), "números ímpares")
