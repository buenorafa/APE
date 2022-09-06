dia = int(input('Digite o dia: '))
mes = int(input('Digite o mes: '))
ano = int(input('Digite o ano: '))

data = False

if(ano <= 2022 and dia > 0): 
    # VERIFICA SE O ANO EH BISSEXTO:  
    if(ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        if(mes == 2 and dia <= 29):
            data = True 
    elif(mes == 2 and dia <= 28):
        data = True
    elif(mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 \
         or mes == 10 or mes == 12 ) and (dia <= 31):
        data = True
    elif(mes == 4 or mes == 6 or mes == 9 or mes == 11) and (dia <= 30):
        data = True

if data:
    print('A data eh valida')
else: 
    print('A data eh invalida')
