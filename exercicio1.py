# 1. Faça um programa que exiba na tela do computador a mensagem “Bem-vindo ao
# mundo da programação! ”.

# print("OLA MUNDO")

# 2. Escreva um programa que leia um número inteiro e exiba o dobro dele.

# numero = int(input('Digite um numero inteiro: '))
# resultado = numero * 2
# print(f'O dobro de {numero} eh {resultado}')

# 3. Faça um programa que leia dois números reais, calcule e exiba a soma deles.

# num1 = float(input('Digite o primeiro numero:'))
# num2 = float(input('Digite o segundo numero:'))
# print(f'A soma deles eh: {num1 + num2}')

# 4. Escreva um programa para calcular a área de um triângulo, dados os valores de
# base e altura. 

# base = float(input('Digite a base: '))
# altura = float(input('Digite a altura: '))
# area = (base*altura)/2
# print(f'A area eh: {area}')

# 5. Escreva um programa para ler o nome e o sobrenome de uma pessoa e escrevê-
# los na seguinte forma: sobrenome seguido por uma vírgula e pelo nome

# nome = input('Digite o nome: ')
# sobrenome = input('Digite o sobrenome: ')
# print(f'{sobrenome}, {nome}')

# 6. Faça um programa que efetue a apresentação do valor da conversão em real (R$)
# de um valor lido em dólar (US$). O algoritmo deverá solicitar o valor da cotação do
# dólar e também a quantidade de dólares disponíveis com o usuário.

# dolar = float(input('Digite a cotacao do dolar: '))
# quant_dolar = float(input('Digite a quantidade de dolar: '))
# print(f'O valor em reais é: {dolar * quant_dolar}')

# 7. O restaurante a quilo Bem-Bão cobra R$25,00 por cada quilo de refeição. Faça um
# programa que leia o peso do prato montado pelo cliente (em quilos) e exiba o valor
# a pagar. Assuma que a balança já desconte o peso do prato.

# valor_do_prato =  float(input('Digite o valor do prato em kg: '))
# print(f'O valor total é {valor_do_prato*25:.2f}')

# 8. Faça um programa que leia o nome de um aluno e as notas das três provas que ele
# obteve no semestre. No final informar o nome do aluno e a sua média (aritmética).

nome = input('Digite o nome: ')
nota_1 = float(input('Digite a nota 1: '))
nota_2 = float(input('Digite a nota 2: '))
nota_3 = float(input('Digite a nota 3: '))
media = (nota_1 + nota_2 + nota_3)/3
print(f'Media aritmetica: {media:.2f}')