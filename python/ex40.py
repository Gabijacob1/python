menor = 0
maior = 0
soma = 0

for c in range(10):
    sexo = input('Digite o seu Sexo M/F: ')
    idade = float(input('Digite sua Idade: '))
    soma += idade
    media = soma/10
    if sexo == 'M':
        menor += 1
    else:
        maior += 1

print('A quantidade de Mulheres é: ', maior)
print('A quantidade de Homem é: ', menor)
print(' A Média Total de Idade é: ', media)
