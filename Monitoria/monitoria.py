# ----------------------------------------------- Matrizes ---------------------------------------------- #
#
# # Criar matriz de ordem N:

# n = int(input('Digite a ordem da matriz: '))
# # Cria a matriz de ordem n
# mat = [[None]*n for i in range(n)]

# # Criar matriz nº de linhas e colunas

# n_col = int(input('Digite o numero de colunas: '))
# n_lin = int(input('Digite o numero de linhas: '))
# mat = [[None]*n_col for i in range(n_lin)]

# # Saída formatada de uma matriz

# for i in range(n_lin):
#     for j in range(n_col):
#         print(f'{mat[i][j]}', end='')
#     print()

# -------------------------------------------------------------------------------------------------- #
# Questões da lista de exercícios

# Vetores:

# 1. Escreva um programa que leia um vetor contendo N => TAMANHO elementos inteiros (N será
# lido), calcule e exiba:

# • A quantidade de elementos pares;
# • A quantidade de elementos ímpares;
# • A soma de todos os elementos;
# • A média dos elementos do vetor.

# n = int(input('Digite tamanho: '))
# vetor = [None]*n

# pares = 0
# impares = 0
# soma = 0
# for i in range(n):
#     vetor[i] = int(input(f'Digite o numero do elemento {i}: '))
#     soma += vetor[i]
#     if vetor[i] % 2 == 0:
#         pares += 1
#     else:
#         impares += 1
# media = soma/n

# print(f'''
# Pares: {pares}
# Impares: {impares}
# Soma: {soma}
# Media: {media}
# ''')


# Matrizes:

# 5. Escreva um programa que:

# . Crie uma matriz de ordem 20 x 4 e armazene nela as 3 notas dos 20 alunos de umaturma e a média de cada um deles.

# . As notas serão lidas e armazenadas nas 3 primeiras colunas da matriz;
# . As médias serão calculadas e armazenadas na 4a coluna da matriz.
# . Imprima as notas dos alunos e suas respectivas médias (no formato de matriz).
# . Calcule e imprima a média geral da turma.
# . Calcule e imprima o número de alunos com média superior à média geral da turma.

# n_lin = 2
# n_col = 4
# # Cria matriz
# mat = [[None]*n_col for i in range(n_lin)]
# # Insere as notas
# for i in range(n_lin):
#     soma = 0
#     for j in range(3):
#         mat[i][j] = int(input(f'Digite a nota {j+1}: '))
#         soma += mat[i][j]
#     # O último elemento é média
#     mat[i][-1] = soma/3

# # Apenas p/ Testes
# # mat = [[10, 10, 10, 10],
# #        [4, 4, 4, 4]]
# print()
# # Saída formatada
# for i in range(n_lin):
#     print(f'Aluno {i+1}: ', end='')
#     for j in range(n_col):
#         print(f'{mat[i][j]}\t', end='')
#     print()

# # Media da turma
# soma = 0
# for i in range(n_lin):
#     soma += mat[i][-1]
# media = soma/n_lin
# print(f'Média: {media}')

# # Acima da média
# cont = 0
# for i in range(n_lin):
#     if mat[i][-1] > media:
#         cont += 1
# print(f'Acima: {cont}')
