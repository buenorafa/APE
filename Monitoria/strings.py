'''
 - split
 - count 
 - slice
'''
x = 10
y = True
ar = [1, 2, 3]

frase = 'Olá mundo!'

# print(frase[0])  # Primeiro elemento
# print(frase[-1])  # Ultimo
# print(ar[-1])  # Ultimo

# print(frase[4:-1])

'''
### 1. Faça um programa que leia o email de uma pessoa e mostre, separadamente, qual o login e qual o domínio. Por exemplo, suponha que o email seja "fulano@provedor.com.br", então o login será "fulano" e o domínio será "provedor.com.br".
'''
# email = input('Informe o email: ')
# email = email.split('@')
# login = email[0]
# provedor = email[1]
# print(f'Login: {login}\nProvedor: {provedor}')


'''
### 4. Faça um programa que leia uma string S e um valor inteiro N, e exiba na tela a string S com as suas vogais repetidas N vezes.

Exemplo:     
Entrada: S: Hoje tem aula de Python   
     
N: 3        
Saída: Hooojeee teeem aaauuulaaa deee Pythooon    
'''
frase = input('Frase: ').lower()
num = int(input('Numero: '))

vogais = 'aeiou'
aux = ''
for i in frase:
    if i in vogais:
        aux += i*num
    else:
        aux += i
print(aux)
