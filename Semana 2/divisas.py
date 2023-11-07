#Ejercicio Divisas

divisas = {'Dolar':'$','Euro':'€', 'Libra':'£'}

solicitud = input('Qué moneda necesita ver?: ')

print('Este es el valor de la variable: ', solicitud)

resultado = divisas.get(solicitud)

print('Símbolo: ', resultado)