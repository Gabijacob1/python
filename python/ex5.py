salario=float(input("Digite o salário do funcionário: "))
aumento=float(input("Digite o percentual de aumento: "))
novo=0
novo = salario * (aumento/100) + salario
print("O novo salario é: %.1f " %novo)