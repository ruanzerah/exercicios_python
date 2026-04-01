def criar_menu(template_mensagem):
    linha = '-'*40
    linha_lat = (len(linha)//2)
    print(linha+'-'*(len(template_mensagem)+2))
    print('-'*linha_lat+' '+template_mensagem+' '+'-'*linha_lat)

def cadastrar_livro(id):
    criar_menu('MENU CADASTRAR LIVRO')
    print(f'Id do livro: {id}')
    nome = input('Por favor, entre com o nome do livro: ')
    autor = input('Por favor, entre com o autor do livro: ')
    editora = input('Por favor, entre com o editora do livro: ')
    livro = {'id': id, 'nome': nome, 'autor': autor, 'editora': editora}
    lista_livros.append(livro.copy())
def consultar_livro():
    while True:
        criar_menu('MENU CONSULTAR LIVRO')
        try:
            opcao = int(input('Escolha a opção desejada:\n'
                          '1 - Consultar Todos os Livros\n'
                          '2 - Consultar Livro por id\n'
                          '3 - Consultar Livro(s) por autor\n'
                          '4 - Retornar\n>>'))
            match opcao:
                case 1:
                    for livro in lista_livros:
                        print(f'id: {livro["id"]}\n'
                              f'nome: {livro["nome"]}\n'
                              f'autor: {livro["autor"]}\n'
                              f'editora: {livro["editora"]}\n')
                case 2:
                    id = int(input('Digite o id do livro: '))
                    for livro in lista_livros:
                        if livro["id"] == id:
                            print(f'id: {livro["id"]}\n'
                                  f'nome: {livro['nome']}\n'
                                  f'autor: {livro["autor"]}\n'
                                  f'editora: {livro["editora"]}\n')
                case 3:
                    autor = input('Digite o autor do(s) livro(s): ')
                    for livro in lista_livros:
                        if livro["autor"] == autor:
                            print(f'id: {livro["id"]}\n'
                                  f'nome: {livro["nome"]}\n'
                                  f'autor: {livro["autor"]}\n'
                                  f'editora: {livro["editora"]}\n')
                case _:
                    break
        except ValueError:
            print('Valor invalido. Tente novamente.')

def remover_livro():
    criar_menu('MENU REMOVER LIVRO')
    try:
        id = int(input('Digite o id do livro a ser removido: '))
        for livro in lista_livros:
            if livro["id"] == id:
                lista_livros.remove(livro)
                print('Livro removido com sucesso!')
    except ValueError:
        print('Valor invalido. Tente novamente.')
def menu():
    global id_global
    while True:
        try:
            criar_menu('MENU PRINCIPAL')
            opcao = int(input('Escolha a opção desejada:\n'
                          '1 - Cadastrar Livro\n'
                          '2 - Consultar Livro(s)\n'
                          '3 - Remover Livro\n'
                          '4 - Sair\n>>'))
            match opcao:
                case 1:
                    cadastrar_livro(id_global)
                    id_global += 1
                    continue
                case 2:
                    consultar_livro()
                    continue
                case 3:
                    remover_livro()
                    continue
                case 4:
                    break
                case _:
                    print('Opção invalida. Tente novamente.')
                    continue
        except ValueError:
            print('Valor invalido. Tente novamente.')



lista_livros = []
id_global = 5859243
print('Bem vindo a Livraria do Ruan')
menu()
