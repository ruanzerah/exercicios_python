print('Bem-vindo a Loja de Gelados do Ruan')
template = ('---|  Tamanho  |  Cupuaçu (CP)  |  Açaí (AC)  |---\n'
            '---|     P     |    R$  9.00    |  R$ 11.00   |---\n'
            '---|     M     |    R$ 14.00    |  R$ 16.00   |---\n'
            '---|     G     |    R$ 18.00    |  R$ 20.00   |---')
tamanho_t = 42
print('-'*21+'Carpadio'+'-'*21)
print('-'*50)
print(template)
print('-'*50)

valor_total = 0

while True:
    produto = input('Digite o sabor desejado: (CP/AC)\n')
    if produto.upper() == 'CP':
        tamanho = input('Digite o tamanho do produto: (P/M/G)\n')
        if tamanho.upper() == 'P':
            valor_total += 9
        elif tamanho.upper() == 'M':
            valor_total += 14
        elif tamanho.upper() == 'G':
            valor_total += 18
        else:
            print('Tamanho inválido. Tente novamente.')
            continue
    elif produto.upper() == 'AC':
        tamanho = input('Digite o tamanho do produto: (P/M/G)')
        if tamanho.upper() == 'P':
            valor_total += 11
        elif tamanho.upper() == 'M':
            valor_total += 16
        elif tamanho.upper() == 'G':
            valor_total += 20
        else:
            print('Tamanho inválido. Tente novamente.')
            continue
    else:
        print('Sabor inválido. Tente novamente.')
        continue
    continuar = input('Deseja mais alguma coisa? (S/N)')
    if continuar.lower() == 'n':
        print(f'O valor total a ser pago: R$ {valor_total:.2f} ')
        break
    elif continuar.lower() == 's':
        continue
    else:
        print('Entrada invalida. Finalizando...')
        print(f'O valor total a ser pago: R$ {valor_total:.2f} ')
        break