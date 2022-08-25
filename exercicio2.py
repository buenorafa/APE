# 1: A Companhia de Carros Usados João Honesto paga seus empregados um salário de R$
# 1.000,00 por mês mais uma comissão de R$ 200,00 por cada carro vendido mais 5% do
# valor da venda.
# Escreva um programa que leia o nome, o número de carros vendidos e o valor total das
# vendas de um vendedor, e calcule e exiba o seu salário.

# nome = input('Digite o nome do vendedor: ')
# carros = int(input('Digite o numero de carros vendidos: '))
# vendas = float(input('Digite o valor total das vendas: '))
# comissao =  carros * 200
# salario = 1000 + comissao + (vendas * 0.05)
# print(f'O salario de {nome} foi R$ {salario:.2f}')

# 2: Escreva um programa para calcular e exibir a média ponderada de 2 notas dadas. Sabe-
# se que nota1 possui peso 6 e nota2 possui peso 4.

# nota1 =  float(input('Digite a nota 1: '))
# nota2 =  float(input('Digite a nota 2: '))
# media = ((nota1 * 6) + (nota2 * 4))/ 10
# print(f'A media ponderada eh: {media}')

# 3: Escreva um programa que leia duas variáveis inteiras e troque o conteúdo entre elas,
# mostrando o resultado.

# var1 =  int(input('Digite a primeira variavel inteira: '))
# var2 =  int(input('Digite a segunda variavel inteira: '))
# aux = var1
# var1 = var2
# var2 = aux
# print(f'var1: {var1} e var2: {var2}')

# 4: Um motorista anota a marcação do hodômetro do seu veículo antes e após uma viagem,
# bem como o número de litros de combustível gastos.
# Escreva um programa que leia os 3 dados acima, o preço do litro de combustível, a
# capacidade do tanque e mostre:
# a) Quilometragem rodada.
# b) Quantos quilômetros por litro faz o veículo.
# c) Autonomia do veículo.
# d) Custo da viagem.

# hod_inicial =  float(input('Digite a marcacao inicial do hodometro: '))
# hod_final = float(input('Digite a marcacao final do hodometro: '))
# litros = float(input('Digite a quantidade de litros usada: '))
# preco_litro = float(input('Digite o preco do litro: '))
# tanque = int(input('Digite a capacidade do tanque de combustivel: '))

# # a) Quilometragem rodada
# quilometragem = hod_final - hod_inicial
# #b) Km/L
# km_l = quilometragem / litros
# #c) Autonomia
# autonomia = km_l * tanque
# #d) Custo da viagem 
# custo = (quilometragem / km_l) * preco_litro

# print(f' Quilometragem: {quilometragem:.2f} Km\n Km/l: {km_l:.2f}\n Autonomia: {autonomia:.2f} Km\n Custo da viagem: R$ {custo:.2f}')

# 5. Escreva um programa que, dado um número inteiro representando uma quantidade de
# segundos, calcule quantas horas, minutos e segundos estão contidos nesta quantidade.
# Ex: 7.388 segundos = 2 horas, 3 minutos e 8 segundos.

# seg =  int(input('Digite a quantidade de segundos: '))
# hora =  seg // 3600
# seg %= 3600
# min = seg//60
# seg %= 60

# print(f'{hora} horas, {min} minutos, {seg} segundos.')


# 6. As Ilhas Weblands formam um reino independente nos mares do Pacífico. Como é um
# reino recente, a sociedade é muito influenciada pela informática. A moeda oficial é o Bit;
# existem notas de B$ 50, B$ 10, B$ 5 e B$ 1. Você foi contratado(a) para ajudar na
# programação dos caixas automáticos de um grande banco das Ilhas Weblands.
# Os caixas eletrônicos das Ilhas Weblands operam com todos os tipos de notas
# disponíveis, mantendo um estoque para cada valor de cédula. Os clientes do banco
# utilizam os caixas eletrônicos para efetuar retiradas de um certo número inteiro de Bits.
# Sua tarefa é escrever um programa que, dado o valor de Bits desejado pelo cliente,
# determine o número de cada uma das notas necessário para totalizar esse valor, de
# modo a minimizar a quantidade de cédulas entregues.
# Exemplo:
# Para B$ 72 seriam as seguintes notas:
# - 1 nota de B$ 50
# - 2 notas de B$ 10
# - 0 notas de B$ 5
# - 2 notas de B$ 1

bits = int(input('Digite a quantidade de bits: '))
n_50 = bits // 50
bits %= 50
n_10 = bits // 10
bits %= 10
n_5 = bits // 5
bits %= 5
n_1 = bits

print(f'- {n_50} notas de B$ 50\n- {n_10} notas de B$ 10\n- {n_5} notas de B$ 5\n- {n_1} notas de B$ 1')