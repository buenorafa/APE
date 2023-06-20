# ------------------------------------------------ Prova ------------------------------------------------ #

# 1 - Ler o gabarito de uma prova de 5 questões onde,  cada resposta pode ser (A, B, C, D ou E), após fazer a leitura do gabarito, o programa deverá fazer a correção das provas de 3 alunos, onde deve calcular e mostrar a pontuação dele. (Obs.: Cada questão certa vale 2 pontos)

# questoes = 5
# gabarito = [None]*questoes

# for i in range(questoes):
#     gabarito[i] = input(f'Digite a resposta da Q.{i+1}: ')

# alunos = 0
# prova = [None]*questoes
# while alunos < 3:
#     cont = 0
#     # Verificar as questões
#     for i in range(questoes):
#         prova[i] = input(f'{i+1}> ')
#         if gabarito[i] == prova[i]:
#             cont += 2
#     print(f'Aluno: {alunos+1}\nNota: {cont}')
#     alunos += 1

# -------------------------------------------------------------------------------------------------------- #
# 2 - Criar uma matriz 10 x 12 (10 times de 12 jogadores), nessa matriz iremos receber as alturas.
# . Média de altura de cada time
# . Qual time possui a maior media

# import random

# n_lin = 10  # TIMES
# n_col = 12  # JOGADORES

# times = [[None]*n_col for i in range(n_lin)]
# # Preechimento aleatório das alturas
# for i in range(n_lin):
#     for j in range(n_col):
#         times[i][j] = random.randint(190, 235)/100

# # Percorrendo a matriz e escrevendo (PROVA)
# # for i in range(n_lin):
# #     for j in range(n_col):
# #         times[i][j] = float(input(f'Digite a altura de J[{i},{j}]: '))

# m_alturas = [None]*n_lin

# for i in range(n_lin):
#     soma = 0
#     for j in range(n_col):
#         soma += times[i][j]
#     media = soma/n_col
#     m_alturas[i] = media

# maior = m_alturas[0]
# indice = 0
# for i in range(1, n_lin):
#     if m_alturas[i] > maior:
#         maior = m_alturas[i]
#         indice = i

# print(m_alturas)
# print()
# print(f'Time {indice + 1}: {maior}')

# -------------------------------------------------------------------------------------------------------- #
# # 3 - Ler uma matriz de ordem 5, salvar a diagonal principal em um vetor e a secundária em outro
# n = 5
# mat = [[None]*n for i in range(n)]

# d_prin = [None]*n
# d_sec = [None]*n

# for i in range(n):
#     for j in range(n):
#         mat[i][j] = random.randint(0, 10)
#         if i == j:
#             d_prin[i] = mat[i][j]
#         if i + j == n - 1:
#             d_sec[i] = mat[i][j]

# for i in range(n):
#     for j in range(n):
#         print(f'{mat[i][j]}\t', end='')
#     print()

# print()
# print(f'D. Principal: {d_prin}\nD. Secundária: {d_sec}')
