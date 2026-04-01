print("Bem-vindo a Loja do Ruan")
valor = float(input("Digite o valor: "))
quantidade = int(input("Digite a quantidade: "))
valor_total = valor * quantidade
desconto = 0
if valor_total <= 2500:
    print('Você não obteve um desconto')
elif valor_total >= 2500 and valor_total < 6000:
    desconto = 0.04
elif valor_total >= 6000 and valor_total < 10000:
    desconto = 0.07
else:
    desconto = 0.11

if desconto > 0:
    print(f'O valor total com desconto foi de R${valor_total-valor_total*desconto:.2f}')
print(f'O valor total sem desconto foi de R${valor_total:.2f}')