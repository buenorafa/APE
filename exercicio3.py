# 1. Escreva um programa que leia um número inteiro e determine se ele é par ou ímpar.

# num = int(input('Digite um numero inteiro: '))

# if(num % 2 == 0):
#     print(f'O numero {num} eh par')
# else:
#     print(f'O numero {num} eh impar')

# 2. Escreva um programa que leia dois números e exiba-os em ordem crescente.

# num_1 = float(input('Digite o primeiro numero: '))
# num_2 = float(input('Digite o segundo numero: '))

# if(num_1 < num_2):
#     print(f'{num_1} {num_2}')
# else:
#     print(f'{num_2} {num_1}')

# 3. Escreva um programa que leia 3 números inteiros, determine e mostre o maior deles.

# num_1 = int(input('Digite o primeiro numero inteiro: '))
# num_2 = int(input('Digite o segundo numero inteiro: '))
# num_3 = int(input('Digite o terceiro numero inteiro: '))
# maior_num = 0

# if(num_1 > num_2):
#     maior_num = num_1
# maior_num = num_2
# if(maior_num < num_3):
#     maior_num = num_3
# print(f'O maior numero eh: {maior_num}')

# 4. Escreva um programa que leia o nome e o sexo (M ou F) de uma pessoa e exiba a mensagem
# "Olá, Sr. Fulano!" ou "Olá, Sra. Fulana!", de acordo com o sexo da pessoa. Obs: Fulano e Fulana
# são nomes exemplos.

# nome = input('Digite o seu nome: ')
# sexo = input('Se for mulher digite M, se for homem digite H: ')

# if(sexo == 'm' or sexo == 'M'):
#     print(f'Ola, Sra. {nome}')
# elif(sexo == 'h' or sexo == 'H'):
#     print(f'Ola, Sr. {nome}')

# 5. A empresa Vende Tudo Ltda paga o salário de cada vendedor com uma comissão de 5% sobre o
# total de vendas daquele vendedor, mas essa comissão nunca deve ser inferior ao salário-
# mínimo. Escreva um programa que leia o valor total das vendas de um vendedor e escreva seu
# salário.

# t_vendas = float(input('Digite o valor total das vendas: '))
# S_MIN = 1200.00
# comissao = t_vendas * 0.05

# if(comissao <=  S_MIN):
#     print(f'O salario eh: R$ {S_MIN}')
# else: 
#     print(f'O salario eh: R$ {comissao:.2f}')

# 6. Recomendam-se estudantes para bolsas de estudo em função de seu desempenho.
# A natureza das recomendações é baseada na seguinte tabela:
#             Conceito 
#             A: Fortemente recomendado 
#             B ou C: Recomendado 
#             D: Nao recomendado 
# Escreva um programa que leia o nome e o conceito de um estudante e exiba o nome do
# estudante e sua respectiva recomendação.

# nome = input('Digite o nome do aluno: ')
# conceito = input('Digite o conceito do aluno (A, B, C ou D): ')

# if(conceito == 'A'):
#     print(f'O aluno {nome} eh fortemente recomendado')
# elif(conceito == 'B' or conceito == 'C'):
#     print(f'O aluno {nome} eh recomendado')
# elif(conceito == 'D'):
#     print(f'O aluno {nome} nao eh recomendado')

# 7. Escreva um programa que leia o peso (kg) e a altura (m) de uma pessoa, determine e mostre o
# seu grau de obesidade, de acordo com a tabela seguinte. O grau de obesidade é determinado
# pelo índice de massa corpórea, cujo cálculo é realizado dividindo-se o peso da pessoa pelo
# quadrado da sua altura.
#         IMC 
#         < 26 : Normal
#         >= 26 e < 30: Obeso
#         >= 30: Obeso Morbido 

# peso = float(input('Digite o peso: '))
# altura = float(input('Digite a altura: '))
# imc = peso / (altura ** 2)

# if(imc < 26):
#     print('IMC: Normal')
# elif(imc >= 26 and imc < 30):
#     print('IMC: Obeso')
# elif(imc >= 30):
#     print('IMC: Obeso morbido')

# 8. Escreva um programa que tenha a funcionalidade de uma calculadora simples. O programa deve
# solicitar a digitação de dois operandos e um operador (+ - x * / %) e deve imprimir ao resultado
# da operação aritmética. Caso o usuário digite um operador inválido, o programa deve imprimir
# "Operador desconhecido".

num_1 = float(input('Digite o primeiro operando: '))
num_2 = float(input('Digite o segundo operando: '))
operador = input('Digite o operador (+ - * / %): ')

if(operador == '+'):
    print(f'{num_1} + {num_2} = {num_1 + num_2}')
elif(operador == '-'):
    print(f'{num_1} - {num_2} = {num_1 - num_2}')
elif(operador == '*'):
    print(f'{num_1} * {num_2} = {num_1 * num_2}')
elif(operador == '/'):
    print(f'{num_1} / {num_2} = {num_1 / num_2}')
elif(operador == '%'):
    print(f'{num_1} % {num_2} = {num_1 % num_2}')
else: print('Operador desconhecido')


