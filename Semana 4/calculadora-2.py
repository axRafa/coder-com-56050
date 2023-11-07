numero1= int(input('Elija el primer numero: '))
numero2= int(input('Elija el segundo numero: '))

print("""
     Opcion 1 - Mostrar suma de los numeros,
     Opcion 2 - Mostrar resta de los numeros,
     Opcion 3 - Mostrar multiplicacion de los numeros,
     Opcion 4 - Finalizar programa""")

print('')


opciones= 0

while opciones !='4':
    opciones = input('Elija una opcion: ')
    if opciones == '1':
        print(numero1 + numero2)
    elif opciones == '2':
        print(numero1 - numero2)
    elif opciones == '3':
        print(numero1 * numero2)
    elif opciones == '4':
        print('Programa Finalizado')
    else:
        print('Esa opcion no existe')