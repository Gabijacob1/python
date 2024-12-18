preço=float(input("Digite o preço do produto: "))
percentual=float(input("Digite o percentual de aumento: "))
novo=0
novo = preço * ((percentual/100)+1)
print("O novo preço do produto é: %.1f " %novo)