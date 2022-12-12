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

# Func entrar -> Login ou None 
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

# Cria um novo usuário -> Cria um arquivo da agenda e um arquivo da senha [SEM RETORNO]
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

# Menu principal
def adicionar_contato(arquivo):
    clear(.3)
    nome = input('Digite o nome do contato: ')
    if nome == 'exit':
        return
    numero = define_telefone()
    if numero == None:
        return
    contato = nome + '\t\t' + numero
    with open(arquivo, 'a') as f:
        f.write(contato)

#Entrar Menu Principal -> Sem retorno
# Nenhuma das funções abaixo precisa de retorno
def menu_principal(arquivo):
  arq = arquivo
  while True:
    clear(.3)
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
