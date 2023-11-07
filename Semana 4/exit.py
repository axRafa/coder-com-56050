numero = 0

condicion= True

while condicion:
    entrada = input('Elije un numero: ')
    if entrada == 'exit':
        condicion = False
    else:
        entrada = int(entrada)
        numero += entrada

print('El resultado es: ', numero)