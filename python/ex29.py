aula=float(input("Digite o valor da hora da aula: "))
dadas=float(input("Digite o numero de aulas dadas: "))
calculo=aula+dadas
print("o valor do salario bruto é: %.1f " %calculo)
desconto=float(input("Digite o percentual de desconto do INSS: "))
conta=calculo/100*desconto
print("o valor do desconto é: %.1f " %conta)
resultado=calculo-conta
print("o salrio liquido é: %.1f " %resultado)