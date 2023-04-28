'''
1. Programa pede 3 nota e calcula a média das duas notas maiores

'''
# O primeiro passo é pegar as 3 notas
# Abaixo eu atribuo o valor da primeira nota a variável menor e nota1, dessa forma a cada nota que o usuário digitar eu já vou atualizando quem o menor.
menor = nota1 = float(input('Digita a nota 1: '))
nota2 = int(input('Digita a nota 2: '))
# Pego a nota2 e verifico se ela é menor que a variável menor
if nota2 < menor:
    menor = nota2
# Mesmo caso p/ nota3
nota3 = int(input('Digita a nota 3: '))
if nota3 < menor:
    menor = nota3
# Aqui irei calcular a soma das notas, somo as 3 notas e diminuo a menor nota
total = nota1 + nota2 + nota3 - menor
# Por fim, calculamos a média
media = total/2

# Agora iremos calcular o conceito e o resultado
conceito = ''
# O resultado começa como Aprovado, caso o conceito seja D ou E atualizamos o valor para 'Reprovado'
resultado = 'Aprovado'
if media >= 90 and media <= 100:
    conceito = 'A'
elif media >= 70 and media < 90:
    conceito = 'B'
elif media >= 60 and media < 80:
    conceito = 'C'
elif media >= 40 and media < 60:
    conceito = 'D'
    resultado = 'Reprovado'
else:
    conceito = 'E'
    resultado = 'Reprovado'

print(f'Média: {media}')
print(f'Conceito: {conceito}\nResultado: {resultado}')

'''
2. Ler 100 numeros, mostrar o nº de pares o nº de impares, e também o maior par e o  maior impar

(Abaixo testarei com 5 numeros apenas, mas bastaria mudar no range do for)

(Zero é par? [https://www.matematica.pt/faq/numero-par.php])
'''
pares = impares = 0
maior_par = maior_impar = 0
for i in range(5):
    num = int(input(f'Digite o nº {i+1}: '))
    # Verifico se é par e adiciono +1 nos pares
    if num % 2 == 0:
        pares += 1
        # Se o num for maior par, ele passar a ser o maior par
        if num > maior_par:
            maior_par = num
    # Se ele não é par, ele só pode ser impar
    else:
        impares += 1
        # Novavemnte verifico se o num digitado é maior que o maior_impar
        if num > maior_impar:
            maior_impar = num
# Por fim printamos o resultado
print(f'Pares: {pares}\nMaior par: {maior_par}')
print(f'Impares: {impares}\nMaior par: {maior_impar}')

'''
3. Ingressos - Homens pagam 50 e mulheres pagam 20, ler o nome e o sexo até a condição de parada (nome = 'x') e calcular o lucro da casa.

'''
lucro = 0
while True:
    # Utilizei o title, pq sempre vai formatar o nome corretamente e caso o usuário digite 'x' ele transformará para 'X'
    nome = input('Digite o nome (P/ encerrar digite X): ').title()
    if nome == 'X':
        break
    sexo = input('Digite o sexo (M ou F): ').upper()
    if sexo == 'M':
        lucro += 50
    elif sexo == 'F':
        lucro += 20
    else:
        print('Entrada inválida.')
print(f'Lucro: {lucro}')
