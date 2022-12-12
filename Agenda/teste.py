import os
from time import sleep 


# Func. de limpar o terminal -> clear(tempo em s de delay)
def clear(delay):
    sleep(delay)
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')

# Retorna um telefone de 11 dígitos numéricos
def define_telefone():
    while True:
        telefone = input('Digite o telefone (Ex: 83988889999): ')
        if telefone == 'exit':
            return 'exit'
        if len(telefone) == 11 and telefone.isalnum():
            return telefone
        else:
            print('Telefone inválido. Digite novamente.')
            clear(1)

# Retorna a senha de 6 caracteres
def define_senha():
    while True:
        senha = input('Digite a senha de 6 caracteres: ')
        if len(senha) == 6:
            return senha
        else:
            print('Senha inválida. Digite novamente.\n')


# Verifica se já existe um arquivo -> True or False
def verifica_arq(arq):
    return os.path.isfile(arq)

# FUNÇÕES DO PROGRAMA 
# Func entrar 
def entrar():
    # Verificação do Login 
    while True:
        # Entra com o numero cadastrado
        login = input('Digite o login: ')
        if login == 'exit':
            clear(0)
            return
        # Adiciona o caminho do arquivo de agenda
        arq = login + '.agenda.txt'
        # Se não encontrar
        if not verifica_arq(arq):
            print('Login incorreto. Tente novamente.')
            clear(1)
        else:
            break
    # Caminho do arquivo de senha 
    arq_senha = login + '.senha.txt'    
    with open(arq_senha, 'r') as f:
        # Senha cadastrada pelo usuário
        chave = f.read()
    # Validação da senha
    while True:
        senha = input('Digite a senha: ')
        if senha != chave:
            print('Senha inválida. Digite novamente.')
            clear(1)
        else:
            print('Senha validada com sucesso')
            clear(1)
            menu_principal(arq)
            break

# Cria um novo usuário -> Um arquivo da agenda e um arquivo da senha 
def registrar_usuario():
    # Verificação do Login
    clear(1)
    while True:
        num_telefone = define_telefone()
        if num_telefone == 'exit':
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
    with open(arq_agenda, 'w') as agenda:
        pass
    with open(arq_senha, 'w') as s:
        s.write(senha)

# Menu principal
def adicionar_contato(arquivo):
    nome = input('Digite o nome do contato: ')
    numero = define_telefone()
    if numero == 'exit':
        return
    contato = nome + '\t\t' + numero
    with open(arquivo, 'a') as f:
        f.write(contato)

#Entrar Menu Principal
def menu_principal(arquivo):
  arq = arquivo
  while True:
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
    elif entrada == '2':
        pass
        #listar_contatos()
        pass
    elif entrada == '3':
        #pesquisar_contato()
        pass
    elif entrada == '4':
        #remover_contato()
        pass
    elif entrada == '5':
        #alterar_contato()
        pass
    elif entrada == '6':
        #excluir_conta_usuario()
        pass
    elif entrada == '7':
        
        print('Voltando ao menu inicial.')
        menu_inicial()
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
            # Func entrar
            clear(0)
            entrar()
        elif entrada == '2':
            registrar_usuario()
        elif entrada == '3':
            clear(0)
            print('Programa encerrado.')
            clear(1)
            break
        else:
            clear(0)
            print('\nOpção inválida. Por favor, tente novamente.')
            clear(1)
        print()



menu_inicial()