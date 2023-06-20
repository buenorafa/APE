
# Input: DD/MM/AAAA
# Output: DD do mês do ano
def encontraMes(data: str) -> str:
    data = data.split('/')
    meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
             'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    dia = data[0]
    mes = int(data[1])
    ano = data[2]
    if mes > 0 and mes < 13:
        return f'{dia} de {meses[mes - 1]} de {ano}'
    return None


def menor(n1, n2, n3):
    menor = n1
    if menor > n2:
        menor = n2
    if menor > n3:
        menor = n3
    return menor

# def menor(n1, n2, n3):
#     return min(n1, n2, n3)

# >= 8 - A
# >= 5 e <8 - B
# <5 - C


def batatinha():
    print('Batatinha')


def media(n1, n2, n3):
    return (n1+n2+n3)/3


def conceito(media) -> str:
    if media >= 8:
        return 'A'
    elif media >= 5 and media < 8:
        return 'B'
    else:
        return 'C'


# n_1 = float(input('Nota 1: '))
# n_2 = float(input('Nota 2: '))
# n_3 = float(input('Nota 3: '))
# media = media(n_1, n_2, n_3)
# print(f'Média: {media}')
# print(f'Conceito: {conceito(media)}')

def soma(vetor: list) -> float:
    soma = 0
    for i in vetor:
        soma += i
    return soma


# def fatorial(num):
#     fat = 1
#     for i in range(1, num+1):
#         fat *= i
#     return fat

def fatorial(num):
    if num == 1:
        return 1
    return num * fatorial(num - 1)


def num(num):
    if num == 1:
        print(1)
    print(num)
    num(num - 1)


print(num(5))
