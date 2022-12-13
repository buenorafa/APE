import os
from time import sleep 

# UTILITÁRIO

# Func. de limpar o terminal -> clear(tempo em s de delay)
def clear(delay):
    sleep(delay)
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')

# Retorna um telefone de 11 dígitos numéricos ou None
def define_telefone():
    while True:
        clear(.3)
        print('Formato do telefone: ddd + 9 + telefone sem separação')
        print('Digite \'exit\' p/ sair.')
        print()
        telefone = input('Digite o telefone: ')
        if telefone == 'exit':
            return
        if len(telefone) == 11 and telefone.isalnum():
            return telefone
        else:
            print('Telefone inválido. Digite novamente.')
            clear(.5)

# Retorna a senha de 6 caracteres ou None
def define_senha():
    while True:
        senha = input('Digite a senha de 6 caracteres (Digite \'exit\' p/ sair): ')
        if senha == 'exit':
            return
        if len(senha) == 6:
            return senha
        else:
            print('Senha inválida. Digite novamente.\n')


# Verifica se já existe um arquivo -> True or False
def verifica_arq(arq):
    return os.path.isfile(arq)

# MENU INICIAL 

# 1 Func entrar -> Login ou None 
def entrar():
    # Verificação do Login 
    while True:
        clear(.3)
        # Entra com o numero cadastrado
        login = input('Digite o login (Digite \'exit\' p/ sair): ')
        if login == 'exit':
            clear(.5)
            return
        # Adiciona o caminho do arquivo de agenda
        arq = login + '.agenda.txt'
        # Se não encontrar
        if not verifica_arq(arq):
            print('Login incorreto. Tente novamente.')
            clear(.5)
        else:
            break
    # Caminho do arquivo de senha 
    arq_senha = login + '.senha.txt'    
    with open(arq_senha, 'r') as f:
        # Senha cadastrada pelo usuário
        chave = f.read()
    # Validação da senha
    while True:
        senha = input('Digite a senha (Digite \'exit\' p/ sair): ')
        if senha == 'exit':
            return
        if senha != chave:
            print('Senha inválida. Digite novamente.')
            clear(.5)
        else:
            print('Senha validada com sucesso')
            clear(.5)
            return arq

# 2 Cria um novo usuário -> Cria um arquivo da agenda e um arquivo da senha [SEM RETORNO]
def registrar_usuario():
    # Verificação do Login
    # clear(.3)
    while True:
        num_telefone = define_telefone()
        if num_telefone == None:
            return
        # AQUI VAI FICAR A AGENDA DO USUÁRIO
        arq_agenda = num_telefone + '.agenda.txt'
        # AQUI A SENHA
        arq_senha = num_telefone + '.senha.txt'
        # Informa erro se já existir este numero cadastrado 
        if verifica_arq(arq_agenda):
            print('\nTelefone já cadastrado. Digite outro número.')
        # SE N EXISTIR PARA O FLUXO DO WHILE E CRIA OS ARQUIVOS
        else:
            break
    # Verificação da senha
    senha = define_senha()
    if senha == None:
        return
    with open(arq_agenda, 'w') as agenda:
        pass
    with open(arq_senha, 'w') as s:
        s.write(senha)

# MENU PRINCIPAL:

# ARQUIVO EM ORDEM ALFABÉTICA -> DEVE SER CHAMADO APÓS ADIÇÃO / MODIFICAÇÃO / EXCLUSÃO DE UM CONTATO
def ordena_arquivo(arquivo):
    with open(arquivo, 'r') as f:
        lista = f.read()
    lista = lista.split('\n')
    # Remove o último elemento da lista (Elemento vazio)
    tamanho = len(lista) - 1
    lista = lista[:tamanho]
    # Organiza em ordem alfabética
    lista.sort()
    with open(arquivo, 'w') as f:
        for i in lista:
            f.write(i + '\n')

def adicionar_contato(arquivo):
    clear(.3)
    nome = input('Digite o nome do contato: ')
    if nome == 'exit':
        return
    numero = define_telefone()
    if numero == None:
        return
    contato = nome + ':' + numero + '\n'
    with open(arquivo, 'a') as f:
        f.write(contato)

# FORMATA -> (83) 98888-8888
def formata_telefone(numero):
    return '(' +  numero[:2] + ')' + ' ' + numero[2:7] + '-'+ numero[7:]  

# EXIBE UMA LISTA DE CONTATOS
def exibe_lista(lista):
    lista = lista.split('\n')
    print('Lista de Contatos: ')
    print()
    tamanho = len(lista)
    print()
    for i in range(tamanho):
        if lista[i] != '':
            aux = lista[i]
            aux = aux.split(':')
            nome = aux[0]
            telefone = formata_telefone(aux[1])
            print(f'{nome}      {telefone}')
    print()

def exibe_lista_num(lista):
    lista = lista.split('\n')
    print('Lista de Contatos: ')
    print()
    tamanho = len(lista)
    print()
    for i in range(tamanho):
        if lista[i] != '':
            aux = lista[i]
            aux = aux.split(':')
            nome = aux[0]
            telefone = formata_telefone(aux[1])
            print(f'{i + 1} {nome}      {telefone}')
    print()


def lista_contatos(arquivo):
    with open(arquivo, 'r') as f:
        lista = f.read()
    exibe_lista(lista)
    entrada = input('Digite \'exit\' p/ sair: ')
    if entrada == 'exit':
        return

def pesquisar_contato(arquivo):
    with open(arquivo, 'r') as f:
        lista = f.read()
    # SEPARAMOS OS CONTATOS EM UMA LISTA
    lista = lista.split('\n')
    while True:
        clear(.3)
        print('Pesquisa:')
        print()
        # RECEBE O NOME DO CONTATO A SER PESQUISADO
        entrada = input('Digite o nome do contato (Digite \'exit\' p/ sair): ')
        if entrada == 'exit':
                clear(.3)
                return
        # OS CONTATOS ENCONTRADOS SERÃO SALVOS NESSA STRING
        lista_da_pesquisa = ''
        print()
        for i in lista:
            # PARA EXCLUIR O ELEMENTO NULO
            if i != '':
                if i.lower().find(entrada.lower()) != -1:
                    # AQUI SALVAMOS OS CONTATOS ENCONTRADOS + \n P/ UTILIZAR A FUNC EXIBE LISTA
                    lista_da_pesquisa += i + '\n'
        if lista_da_pesquisa != '':
            clear(.3)
            exibe_lista(lista_da_pesquisa)
            entrada = input('Digite \'exit\' p/ sair ou qualquer tecla p/ voltar: ')
            if entrada == 'exit':
                clear(.3)
                return
        else:
            clear(0)
            print('Usuário não encontrado. Tente novamente!')
            clear(.5) 

def remover_contato(arq):
    
    login = arq.split('.agenda.txt')
    login = login[0]
    print('Login: ' + login)
    with open(arq, 'r') as f:
        lista = f.read()
    exibe_lista_num(lista)
    lista = lista.split('\n')
    lista = lista[:len(lista) - 1]
    while True:
        entrada = input('Digite o nº do usuário a ser removido (Digite \'exit\' p/ sair): ')
        if entrada == 'exit':
            return
        if entrada.isdigit():
            entrada = int(entrada)
            if entrada - 1 <= len(lista):
                del lista[entrada - 1]
                print('Contato removido com sucesso')
                # print(lista)
                with open(arq, 'w') as f:
                    for i in lista:
                        f.write(i + '\n')
                return
            else: 
                print('Contato inválido. Tente novamente. ')
        else:
            print('Contato inválido. Tente novamente. ')

def alterar_contato(arq):
    pass

def remover_usuario(arquivo):
    print('Excluir conta: ')
    print()
    print('Deseja excluir permanentemente sua conta?')
    print()
    print('Pressione \'S\' p/ excluir ou qualquer tecla p/ voltar.')
    entrada = input('Esse processo não poderá ser revertido: ')
    if entrada.lower() == 's':
        login = entrar()
        if login == arquivo:
            arq = login
            login = login.split('.agenda.txt')
            arq_senha = login[0] + '.senha.txt'
            os.remove(arq)
            os.remove(arq_senha)
            return -1
        else:
            print('Não foi possível excluir sua conta. Tente novamente!')
            return
    else:
        return


#Entrar Menu Principal -> Sem retorno
# Nenhuma das funções abaixo precisa de retorno
def menu_principal(arquivo):
  arq = arquivo
  while True:
    # clear(.3)
    print('Opções disponíveis:')
    print()
    print('[1] Adicionar Contato')
    print('[2] Listar Contatos')
    print('[3] Pesquisar Contato')
    print('[4] Remover Contato')
    print('[5] Alterar Contato')
    print('[6] Excluir Conta do Usuário')
    print('[7] Sair')
    print()
    entrada = input('Digite a opção desejada: ')
    if entrada == '1':
        adicionar_contato(arq)
        ordena_arquivo(arq)
    elif entrada == '2':
        lista_contatos(arq)
    elif entrada == '3':
        pesquisar_contato(arq)
    elif entrada == '4':
        remover_contato(arq)
        # ordena_arquivo(arq)
    elif entrada == '5':
        #alterar_contato()
        pass
    elif entrada == '6':
       remover = remover_usuario(arq)
       if remover == -1:
        return
    elif entrada == '7':
        return 
    else:
        print('\nOpção inválida. Por favor, tente novamente.')
    print()


#função menu inicial
def menu_inicial():
    while True:
        print('Menu Inicial: ')
        print()
        print('[1] Entrar')
        print('[2] Registrar Usuário')
        print('[3] Sair')
        print()
        entrada = input('Digite a opção desejada: ')
        print()
        if entrada == '1':
            return 1
        elif entrada == '2':
            return 2
        elif entrada == '3':
            return 3
        else:
            clear(0)
            print('\nOpção inválida. Por favor, tente novamente.')
            clear(1)
        print()


# MAIN FUNCTION
def main():
    while True:
        menu = menu_inicial()
        if menu == 1:
            # Recebe a func entrar
            login = entrar()
            if login == None:
                # clear(.5)
                # volta pro inicial
                pass
            else:
                menu_principal(login)
                clear(.5)
        elif menu == 2:
            registrar_usuario()
            clear(.5)
        elif menu == 3:
            clear(0)
            print('Programa encerrado.')
            clear(.5)
            break

main()
# lista_contatos('83988888888.agenda.txt')
# pesquisar_contato('83988888888.agenda.txt')
# remover_contato('83988888888.agenda.txt')



