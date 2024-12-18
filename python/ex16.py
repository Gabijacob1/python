idade = int(input('Digite sua idade em anos: '))

if idade<16:
    print('Não eleitor')
elif idade<=18 and idade>70:
    print('Eleitor facultativo')
elif idade<=70 and idade>18:
    print('Eleitor obrigátorio')
else:
    print('Eleitor facultativo')