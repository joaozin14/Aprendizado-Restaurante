import os

# Criando dicionário com nomes, categorias e se está ativou ou não
restaurantes = [{'nome':'Buteco das primas','categoria':'Bar','status':False},
                {'nome':'Pizza suprema','categoria':'Pizzaria','status':True},
                {'nome':'La papa','categoria':'Restaurante','status':True}]

# Função que exibe o nome do programa
def exibir_nome_do_programa():
    print("""
------------------------        
Ｓａｂｏｒ Ｅｘｐｒｅｓｓ 
------------------------
 """)

# Função que exibe as opções
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

# Função que fecha o programa
def finalizar_app():
    os.system('cls')
    print('Finalizando o app')

# FFunção para opção inválida
def opcao_invalida():
    print('Opção inválida')
    input('\nDigite uma tecla para voltar para o menu principal')
    main()

# Função que cadastras os restaurantes
def cadastrar_restaurante():
    os.system('cls')
    print('Cadastro de novos restaurantes\n')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_restaurante = input(f'Digite o nome da categoria do restaurante {nome_restaurante}: ')
    dados_restaurante = {'nome':nome_restaurante,'categoria':categoria_restaurante,'status':False}
    restaurantes.append(dados_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

# Função que mostrar os restaurantes em lista
def mostrar_restaurantes():
    os.system('cls')
    print('Restaurantes cadastrados: \n')
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria do restaurante'.ljust(22)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo_restaurante = 'ativado' if restaurante['status'] else 'desativado'
        print(f'-{nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo_restaurante} ',sep='\n')
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

#Função que ativa e desativa o True e False 
def ativar_desativar():
    os.system('cls')
    print('Alternando o estado do restaurante\n')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['status'] = not restaurante['status']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['status'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

# Função para escolher uma opção
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1: 
            cadastrar_restaurante()
        elif opcao_escolhida == 2: 
            mostrar_restaurantes()
        elif opcao_escolhida == 3: 
            ativar_desativar()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

# Função principal que chama as outras funções
def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()