# 1. Faça um programa que calcule e mostre os números múltiplos de 5 do
# intervalo 50 a 300, juntamente com suas raízes e seus cubos.
# import math

# for i in range(50, 300, 5):
#     print(f'N: {i}')
#     print(f'Raíz: {math.sqrt(i):.2f}')
#     print(f'Cubo: {i**3}')

# 2. Faça um programa que leia um número N, inteiro, e some todos os números
# de 1 até N, mostrando o resultado.

# n = int(input('Digite um numero inteiro: '))
# aux = 0
# for i in range(n+1):
#     aux += i
# print(f'A soma dos numeros foi: {aux}')

# 3. Faça um programa que calcule e mostre o fatorial de um número N, fornecido
# pelo usuário. A definição de fatorial é mostrada a seguir:

# n = int(input('Digite um numero inteiro: '))
# aux = 1
# for i in range(1 , n+1):
#     aux *= i
# print(f'{n}! = {aux}')

# 4. Faça um programa que leia 20 números inteiros, determine e mostre o maior
# deles.

# aux = 0
# for i in range(20):
#     n = int(input('Digite um numero inteiro: '))
#     if(aux < n):
#         aux = n
# print(f'O maior numero: {aux}')

# 5. Faça um programa que, para um grupo de N pessoas (obs: N será lido):
# • Leia o sexo (M ou F) de cada pessoa;
# • Calcule e escreva o percentual de homens;
# • Calcule e escreva o percentual de mulheres.

# n = int(input('Digite o numero de pessoas: '))
# homens = 0
# mulheres = 0
# for i in range(n):
#     sexo = input(f'Digite o sexo (M ou F) da pessoa {i + 1}: ')
#     sexo = sexo.upper()
#     if(sexo == 'M'):
#         homens += 1
#     elif(sexo == 'F'):
#         mulheres += 1
# print(f'Total de pessoas: {n}\
#     \nPercentual de homens: {(homens/n)*100:.2f}%\
#     \nPercentual de mulheres: {(mulheres/n)*100:.2f}%')

# 6. Faça um programa que leia 3 números inteiros (N, X, Y) e mostre todos os
# números múltiplos de N entre X e Y.

# n = int(input('Digite N: '))
# x = int(input('Digite X: '))
# y = int(input('Digite Y: '))
# for i in range(x, y+1):
#     if(i%n == 0):
#         print(i)

# 7. Um número é, por definição, primo se ele não tem divisores, exceto 1 e ele
# próprio. Faça um programa que leia um número e determine se ele é ou não
# primo.

# numero =  int(input('Digite um numero: '))
# aux = 0
# for i in range(2, numero - 1):
#     if(numero % i == 0):
#         aux += 1
# resultado = 'Eh primo'
# if(aux > 0):
#     resultado = 'Nao eh primo'
# print(resultado)

# 8. Faça um programa que leia um número inteiro N, calcule e mostre o maior
# quadrado perfeito menor ou igual a N. Por exemplo, se N for igual a 38, o
# resultado é 36.

# n = int(input('Digite um numero: '))
# quadrado = 0
# for i in range(n, 1, -1):
#     if(i**2 <= n):
#         quadrado = i**2
#         break
# print(f'Quadrado perfeito: {quadrado}')