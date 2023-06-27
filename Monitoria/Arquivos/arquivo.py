'''
    Para abrir um arquivo em python
    1. open() 
    2. a função recebe dois parâmetros, o nome arquivo e o modo de abertura do arquivo
    Os modos de abertura podem ser: 'w' - Escrita, 'r' - Leitura e o 'a' de Adicionar ao fim do arquivo
    3. Após aberto o arquivo, podemos utilizar as funções read (leitura do arquivo) e readline (leitura por linha) e write de escrita.
    
    Por último é necessário fechar o arquivo: close()
'''

# 1.

# nome_arq = input('Digite o nome do arquivo: ')
# nome_arq += '.txt'

# arq = open(nome_arq, 'r')

# # P/ fazer a leitura completa do arquivo
# conteudo = arq.read()

# # P/ fazer a leitura linha a linha
# # conteudo = arq.readline()

# arq.close()

# print(conteudo)

# 2.
# nome_arq = input('Digite o nome do arquivo com extensão (.txt): ')

# with open(nome_arq, 'r') as arq:
#     conteudo = arq.read()

# print(conteudo)
# print()

# novo_conteudo = ''
# for i in conteudo:
#     if i == ' ':
#         novo_conteudo += '#'
#     else:
#         novo_conteudo += i

# novo_arq = 'copia.txt'
# with open(novo_arq, 'w') as arq:
#     arq.write(novo_conteudo)

# with open(novo_arq, 'r') as arq:
#     resultado = arq.read()

# print(resultado)

# 3.
# nome = input('Digite o nome do arquivo: ')
# arq = open(nome, 'a')
# texto = input('Digite a string a ser adicionada: ')
# arq.write(texto + '\n')
# arq.close()


# 4.
# nome_arq = input('Digite o nome do arquivo: ')

# arq = open(nome_arq, 'r')

# n = 1
# for i in arq:
#     print(f'{n} {i}')
#     n += 1
# arq.close()
