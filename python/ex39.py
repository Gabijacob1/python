p1 = str(input('Telefonou para a vítima?, (s/n): ')).upper()
p2 = str(input('Esteve no local do crime?, (s/n): ')).upper()
p3 = str(input('Mora perto da vítima?, (s/n): ')).upper()
p4 = str(input('Devia para a vítima?, (s/n): ')).upper()
p5 = str(input('Já trabalhou com a vítima?, (s/n): ')).upper()
soma = 0
if p1 == "s":
    soma = soma + 1
elif p2 == "s":
        soma = soma + 1
elif p3 == "s":
        soma = soma + 1
elif p4 == "s":
        soma = soma + 1
elif p5 == "s":
        soma = soma + 1

print('-------------')
if soma == 2:
    print("Suspeiro")
elif 2 < soma < 5:
    print('Cúmplice')

elif soma>=5:
    print('Assassino')

else:
    print('Inocente')