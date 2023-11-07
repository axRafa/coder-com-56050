if True:
    print(' hola mundo ')

if False:
    print(' esto lo va a ignorar ')

if False:
    print(' esto tambien lo va a ignorar ')
else:
    if True:
        print(" Esto esta en el 'else' ")

if False:
    print( ' Ignorado ')
elif True:
    print(' esto tambien esta ignorado ')
elif True:
    print(' esto sí se va a imprimir ')

if True:
    if False:
        print(' acá hay un false ')
    if True:
        print(' esto sí se imprime')