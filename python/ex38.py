Pessoas = Pessoas + 1
somasexo = somasexo + 1
somaidade = somaidade + idade
continua = input('Deseja continuar: s/n ')


mediasexo = somasexo / Pessoas
mediaidade = somaidade / Pessoas
if sexo == 'M':
        menor += 1
else:
        maior += 1

print('A quantidade de Mulheres é: ', maior)
print('A quantidade de Homem é: ', menor)
print('A Média Total de Idade é: ', mediaidade)
print('Pessoas intrevistadas: ', Pessoas)

menor = 0
maior = 0
continua = 0
soma = 0
somasexo = 0
somaidade = 0
Pessoas = 0
while continua != "n":
    sexo = input('Digite o seu Sexo M/F: ')
    idade = float(input('Digite sua Idade: '))
    soma += idade



    Pessoas = Pessoas + 1
    somasexo = somasexo + 1
    somaidade = somaidade + idade
    continua = input('Deseja continuar: s/n ')


    mediasexo = somasexo / Pessoas
    mediaidade = somaidade / Pessoas
    if sexo == 'M':
        menor += 1
    else:
        maior += 1

print('A quantidade de Mulheres é: ', maior)
print('A quantidade de Homem é: ', menor)
print('A Média Total de Idade é: ', mediaidade)
print('Pessoas intrevistadas: ', Pessoas)