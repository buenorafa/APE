import os

# Retorna um telefone de 11 dígitos numéricos
def define_telefone():
    while True:
        telefone = input('Digite o telefone (Ex: 83988889999): ')
        if len(telefone) == 11 and telefone.isalnum():
            return telefone
        else:
            print('Telefone inválido. Digite novamente.')

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

# Cria um novo usuário -> Um arquivo da agenda e um arquivo da senha 
def registrar_usuario():
    # Verificação do Login
    while True:
        num_telefone = define_telefone()
        # AQUI VAI FICAR A AGENDA DO USUÁRIO
        arq_agenda = num_telefone + '.agenda.txt'
        # AQUI A SENHA
        arq_senha = num_telefone + '.senha.txt'
        # Se não existir login  com esse nome
        if not verifica_arq(arq_agenda) and not verifica_arq(arq_senha):
            break
    # Verificação da senha
    senha = define_senha()
    with open(arq_agenda, 'w') as agenda:
        pass
    with open(arq_senha, 'w') as s:
        s.write(senha)


#função menu inicial
def menu_inicial():
    while True:
        print('[1] Entrar')
        print('[2] Registrar Usuário')
        print('[3] Sair')
        entrada = input('Digite a opção desejada: ')
        print()
        if entrada == '1':
            # Func entrar
            print('Entrar')
        elif entrada == '2':
            registrar_usuario()
        elif entrada == '3':
            print('Programa encerrado.')
            break
        else:
            print('\nOpção inválida. Por favor, tente novamente.')
        print()

menu_inicial()
