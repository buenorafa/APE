# 1. Escreva um programa que solicite a digitação de um número (de 1 a 7) correspondente a um dia
# da semana e imprima o nome do dia da semana e se é dia útil (de segunda a sexta) ou final de
# semana (sábado e domingo). Considere que o dia 1 é o domingo.

dia = int(input('Digite o dia da semana (De 1 a 7): '))
if(dia == 1):
    print('Final de semana\nDomingo')
elif(dia == 2):
    print('Dia util\nSegunda-feira')
elif(dia == 3):
    print('Dia util\nTerca-feira')
elif(dia == 4):
    print('Dia util\nQuarta-feira')
elif(dia == 5):
    print('Dia util\nQuinta-feira')
elif(dia == 6):
    print('Dia util\nSexta-feira')
elif(dia == 7):
    print('Final de semana\nSábado')

# 2. Escreva um programa que solicite a digitação de um caractere qualquer do teclado e imprima
# sua classificação: vogal, consoante, número e caractere especial.

# SOLUCAO USANDO REGEX

import re 

char = input('Digite um caractere: ')

if(re.search('[a-zA-Z]', char)):
    if(re.search('[aeiou]')):
        print('Vogal')
    else:
        print('Consoante')
elif(re.search('[0-9]', char)):
    print('Numero')
else:
    print('Caractere especial')

# 3. Escreva um programa que solicite a digitação de um ano e imprima sua classificação como
# bissexto ou não bissexto.
# Obs: um ano é bissexto se for divisível por 4, mas não por 100. Um ano também é bissexto se
# for divisível por 400.

ano =  int(input('Digite o ano: '))

if(ano % 4 == 0):
    if(ano % 100 != 0):
        print('Bissexto')
    elif(ano % 100 == 0):
        if(ano % 400 == 0):
            print('Bissexto')
        else:
            print('Nao eh bissexto')
else:
    print('Nao eh bissexto')

# 4. Escreva um programa que leia a hora de início de um jogo e a hora do final do jogo (considerando
# apenas horas inteiras), calcula a duração do jogo em horas, sabendo-se que o tempo máximo de
# duração do jogo é de 24 horas e que o jogo pode iniciar em um dia e terminar no dia seguinte.
# O programa deve mostrar o resultado obtido.

h_inicial = int(input('Digite a hora de inicio: '))
h_final = int(input('Digite a hora do final: '))

if(h_inicial < h_final):
    print(f'Duracao: {h_final - h_inicial}h')
elif(h_inicial == h_final):
    print('Duracao: 24h')
else:
    print(f'Duracao: {(24 - h_inicial) + h_final}h')

# 5. Escreva um programa para determinar as raízes de uma equação de segundo grau, dados os
# seus coeficientes.

import math

a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

delta = b**2 - 4*a*c

x_1 = (-b + math.sqrt(delta))/ 2*a
x_2 = (-b - math.sqrt(delta))/ 2*a

if(delta < 0):
    print('Delta negativo')
else:
    print(f'X = {x_1:.2f}')
    print(f'X\' = {x_2:.2f}')

# 6. Na primeira etapa de um concurso, o candidato tem que fazer duas provas. Dessas duas notas é
# tirada a média do candidato. Caso essa média seja maior ou igual a 7.0, ele estará apto a fazer a
# segunda etapa do concurso. Na segunda etapa, ele fará mais uma prova, onde deverá obter uma
# nota maior ou igual a 8.0 para ser aprovado no concurso.
# Escreva um programa que leia as notas da primeira etapa, calcule a média da primeira etapa, e
# se o candidato for aprovado na primeira etapa, leia a nota dele na segunda etapa e diga se ele
# foi aprovado ou não no concurso.

# Primeira etapa
n_1 =  float(input('Digite a primeira nota: '))
n_2 = float(input('Digite a segunda nota: '))

media = (n_1 + n_2)/2

if(media < 7):
    print('O candidato nao obteve a media necessaria para prox etapa')
else:
    n_3 = float(input('Candidato aprovado na etapa 1\nDigite a terceira nota: '))
    if(n_3 >= 8):
        print('Candidato aprovado no concurso')
    else:
        print('Nao foi dessa vez')