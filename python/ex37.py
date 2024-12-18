valor = 1
total = total =total2 = 0
while valor == 1:
    n = int(input('Digite um numero: '))
    valor = int(input('Deseja continuar? Digite 1 para continuar ou -1 para finalizar: '))
    if (n % 2 == 0):
        total = total + n
    else:
        total2 = (n*n)
print('--------')
print('Produto numeros impares: ', total2)
print("soma dos numeros pares: ", total)