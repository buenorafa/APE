'''
### 3. Escreva um programa que leia N números inteiros (máximo 20) e armazene em um vetor X. Calcule a média dos elementos do vetor e informe quantos elementos estão abaixo da média do conjunto.

Crie as seguintes funções:
* Uma função que faça a leitura dos elementos de um vetor de inteiros. Essa função
deve receber como parâmetro o número de elementos do vetor e deve retornar o
vetor preenchido.
* Uma função que calcule a média dos elementos de um vetor. Essa função deve
receber como parâmetro um vetor e retornar a média dos elementos dele.
* Uma função que receba um vetor e um número, e retorne quantos elementos do
vetor estão abaixo desse número.
'''
import random


# def leitura(tamanho: int):
#     vetor = []
#     for i in range(tamanho):
#         vetor.append(int(input('Digite o num: ')))
#     return vetor


# def media(vetor: list):
#     soma = 0
#     for i in vetor:
#         soma += i
#     return soma/len(vetor)


# def abaixo(vetor, num):
#     somatorio = 0
#     for i in vetor:
#         if i < num:
#             somatorio += 1
#     return somatorio


# n = int(input('N: '))

# v = leitura(n)
# media_v = media(v)
# ab = abaixo(v, media_v)

# print(f'''
# Vetor: {v}
# Média: {media_v}
# < Média: {ab}
# ''')


'''
4. Faça um programa que leia duas matrizes de inteiros e gere uma terceira matriz que corresponderá a soma das duas matrizes lidas. A ordem das matrizes também será lida.
O programa deverá conter as seguintes funções:

* Uma função para gerar -, sendo passados como parâmetros a ordem
da matriz.

* Uma função para exibir uma matriz em sua representação clássica (linhas e colunas).
* Uma função para somar duas matrizes.

'''


def exibe_matriz(matriz):
    ordem = len(matriz[0])
    for i in range(ordem):
        for j in range(ordem):
            print(matriz[i][j], end=' ')
        print()


def soma_matriz(mat1, mat2):
    ordem = len(mat1[0])
    mat_resultado = [[None]*ordem for i in range(ordem)]
    for i in range(ordem):
        for j in range(ordem):
            mat_resultado[i][j] = mat1[i][j] + mat2[i][j]
    return mat_resultado


def cria_matriz(ordem: int):
    return [[random.randint(0, 10)]*ordem for i in range(ordem)]


mat_1 = cria_matriz(3)
mat_2 = cria_matriz(3)
soma = soma_matriz(mat_1, mat_2)

exibe_matriz(mat_1)
print()
exibe_matriz(mat_2)
print()
exibe_matriz(soma)
