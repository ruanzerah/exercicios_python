from random import randint

def gerar_linha(minimo, maximo):
    linha = []
    while len(linha) < 5:
        valor = randint(minimo, maximo)
        if valor not in linha:
            linha.append(valor)
    return linha

def gerar_cartela(sigla):
    linha_0 = gerar_linha(1,15)
    linha_1 = gerar_linha(16,30)
    linha_2 = gerar_linha(31,45)
    linha_3 = gerar_linha(46,60)
    linha_4 = gerar_linha(61,75)
    cartela = []
    for i in range(5):
        linha = [linha_0[i],linha_1[i], linha_2[i], linha_3[i], linha_4[i]]
        cartela.append(linha)
    cartela[2][2] = sigla
    return cartela

def definir_regras():
    global regras
    while True:
        try:
            regras = int(input('Escolha a regra:\n'
                               '1 - Linha, Coluna, Diagonal (padrão)\n'
                               '2 - Cartela Cheia\n>>'))
            match regras:
                case 1:
                    regras = 1
                    break
                case 2:
                    regras = 2
                    break
                case _:
                    break
        except ValueError:
            print('Valor invalido. Tente novamente.')
def imprimir_cartela(cartela):
    for linha in cartela:
        for valor in linha:
            try:
                if valor < 10:
                    print(f"[0{valor}]",end=" ")
                else:
                    print(f"[{valor}]",end=" ")
            except TypeError:
                print(f"[{valor}]",end=" ")
        print(end="\n")
def sorteia_valor(sorteados):
    if len(sorteados) >= 75:
        return -1
    while True:
        valor = randint(1,75)
        if valor in sorteados:
            continue
        else:
            return valor
def verifica_ganhador_cheia(cartelas, sorteados):
    pontos = 0
    for cartela in cartelas:
        for linha in cartela:
            for valor in linha:
                if valor in sorteados:
                    pontos += 1
                if pontos == 24:
                    return cartela
        pontos = 0
    return None


def verifica_ganhador_LCD(cartelas, sorteados):
    sorteados_set = set(sorteados)
    for cartela in cartelas:
        diagonal_1 = [cartela[0][0], cartela[1][1], cartela[3][3], cartela[4][4]]
        diagonal_2 = [cartela[0][4], cartela[1][3], cartela[3][1], cartela[4][0]]
        if all(num in sorteados_set for num in diagonal_1) or all(num in sorteados_set for num in diagonal_2):
            print('Diagonal ganha')
            return cartela

        for i, linha in enumerate(cartela):
            linha_limpa = linha.copy()
            if i == 2:
                del linha_limpa[2]

            if all(num in sorteados_set for num in linha_limpa):
                print('Linha ganha')
                return cartela

        colunas = []
        for j in range(5):
            coluna_atual = []
            for i in range(5):
                if i == 2 and j == 2:
                    continue
                coluna_atual.append(cartela[i][j])
            colunas.append(coluna_atual)

        for coluna in colunas:
            if all(num in sorteados_set for num in coluna):
                print('Coluna ganha')
                return cartela

    return None


lista_cartelas = []
lista_sorteados = []
regras = 1

while True:
    try:
        opcao = int(input('Escolha a opção:\n'
                          '1 - Gerar Cartelas\n'
                          '2 - Definir Regras\n'
                          '3 - Começar Bingo!\n'
                          '4 - Encerrar Programa\n>>'))
        match opcao:
            case 1:
                lista_cartelas.clear()
                while True:
                    try:
                        qtd = int(input('Quantas cartelas?\n'))
                        sgl = input('Qual sua Sigla: (2 letras)\n>>')
                        if len(sgl) != 2 and not sgl.isalpha():
                            print('Valor invalido. Tente novamente.')
                            continue
                        for i in range(qtd):
                            lista_cartelas.append(gerar_cartela(sgl))
                        break
                    except ValueError:
                        print('Valor invalido. Tente novamente.')
            case 2:
                definir_regras()
            case 3:
                while True:
                    sorteado = sorteia_valor(lista_sorteados)
                    if sorteado != -1:
                        lista_sorteados.append(sorteado)
                        match regras:
                            case 1:
                                cartela_LCD = verifica_ganhador_LCD(lista_cartelas, lista_sorteados)
                                if cartela_LCD is None:
                                    continue
                                else:
                                    print(f'Lista de numeros sorteados: {lista_sorteados}\n'
                                          f'Quantidade de numeros gerados: {len(lista_sorteados)}\n'
                                          f'Quantidade de cartelas: {len(lista_cartelas)}\n')
                                    imprimir_cartela(cartela_LCD)
                                    break
                            case 2:
                                cartela_cheia = verifica_ganhador_cheia(lista_cartelas, lista_sorteados)
                                if cartela_cheia is None:
                                    continue
                                else:
                                    print(f'Lista de numeros sorteados: {lista_sorteados}\n'
                                          f'Quantidade de numeros gerados: {len(lista_sorteados)}\n'
                                          f'Quantidade de cartelas: {len(lista_cartelas)}\n')
                                    imprimir_cartela(cartela_cheia)
                                    break
                            case _:
                                print('Valor invalido. Tente novamente.')
                    else:
                        print('Os guri se lasco')
                        break




    except ValueError:
        print('Valor invalido. Tente novamente.')