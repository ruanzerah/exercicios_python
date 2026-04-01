def escolha_servico():
    dig_custo_pagina = 1.1
    ico_custo_pagina = 1
    ipb_custo_pagina = 0.4
    fot_custo_pagina = 0.2
    while True:
        servico = input('Entre com o tipo de serviço desejado\n'
                    'DIG - Digitalização\n'
                    'ICO - Impressão Colorida\n'
                    'IPB - Impressão Preto e Branco\n'
                    'FOT - Fotocópia\n>>'
                    )
        servico = servico.upper()
        if servico == 'DIG':
            return dig_custo_pagina
        elif servico == 'ICO':
            return ico_custo_pagina
        elif servico == 'IPB':
            return ipb_custo_pagina
        elif servico == 'FOT':
            return fot_custo_pagina
        else:
            print('Entrada invalida. Tente novamente: (DIG/ICO/IPB/FOT)\n')
            continue
def num_paginas():
    while True:
        try:
            print()
            num_paginas = int(input('Entre com o numero de paginas: '))
            if num_paginas < 20:
                return num_paginas
            elif num_paginas >= 20 and num_paginas < 200:
                return num_paginas - (num_paginas*0.15)
            elif num_paginas >= 200 and num_paginas < 2000:
                return num_paginas - (num_paginas*0.20)
            elif num_paginas >= 2000 and num_paginas < 20000:
                return num_paginas - (num_paginas*0.25)
            else:
                print('Não aceitamos tantas paginas de una vez.\n'
                      'Por favor, entre com o numero de paginas novamente.')
                continue
        except ValueError:
            print('Valor invalido. Tente novamente.')
            continue
def servico_extra():
    while True:
        try:
            servico_extra = int(input('Deseja adicionar algum serviço?\n'
                                      '1 - Encadernação Simples - R$ 15.00\n'
                                      '2 - Encadernação Capa Dura - R$ 40.00\n'
                                      '0 - Não Desejo mais nada\n>>'))
            if servico_extra == 1:
                return 15.0
            elif servico_extra == 2:
                return 40.0
            elif servico_extra == 0:
                return 0.0
            else:
                print('Serviço invalido. Tente novamente.')
                continue
        except ValueError:
            print('Valor invalido. Tente novamente.')


print('Bem-vindo a Copiadora do Ruan\n')

servico = escolha_servico()
num_paginas = num_paginas()
extra = servico_extra()

total = (servico * num_paginas) + extra
print()
print(f'Total: R$ {total:.2f} (serviço: {servico:.2f} * paginas: {num_paginas:.0f} + extra: {extra:.2f})')

