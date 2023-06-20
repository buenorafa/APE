'''
### 1) Receber um nome completo e criar um login, seguindo o modelo abaixo: 
Entrada:     
Nome: Rafael Limeira de Castro Bueno     
Saída:     
Login: rafael.bueno
'''
# 1
# print(login)

'''
### 2) 
Receber uma data no formato DD/MM/AAAA e retornar a data formatada:

Ex.:      
Entrada: 22/09/1999         
Saída: 22 de setembro de 1999
'''


'''
3) A obesidade ocorre quando o imc é superior a 26, escreva uma função que retorne True se for obeso ou false caso contrário. E o programa principal deve receber peso e altura de várias pessoas e calcular o percentual de obesos no grupo. (P/ encerrar o programa, deve-se digitar 0 no peso)
'''


def imc(peso, altura):
    return peso/(altura**2)


def obeso(imc):
    return imc > 26


num_pessoas = 0
num_obesos = 0
while True:
    peso = float(input('Peso: '))
    if peso == 0:
        break
    altura = float(input('Altura: '))
    num_pessoas += 1
    i_m_c = imc(peso, altura)
    print(i_m_c)
    if obeso(i_m_c):
        num_obesos += 1

print(f'Percentual de obesos: {(num_obesos/num_pessoas)*100}%')


# def login_prov(email):
#     email = email.split('@')
#     login = email[0]
#     provedor = email[1]
#     print(f'Login: {login}\nProvedor: {provedor}')


# def email(login, provedor):
#     return f'{login}@{provedor}'


# aux = []
# while True:
#     login = input('Digite o seu login: ')
#     if (login == 'x'):
#         break
#     provedor = input('Digite o provedor: ')
#     aux.append(email(login, provedor))

# for i in aux:
#     login_prov(i)
