# Por medio de enumerate le asignamos una numeración a las frutas de un diccionario y las guardamos en una lista de tuplas para
# no olvidar el código asignado.

stock_de_frutas = {'banana': 567, 'anana': 363, 'naranja': 123, 'manzana': 435, 'mango': 345}

lista_frutas = []

for indice, fruta in enumerate(stock_de_frutas):
    lista_frutas.append((indice, fruta, stock_de_frutas[fruta]))

print(lista_frutas)

# Ahora voy a agregar más frutas a la lista, pero para seguir numerandolas empezar a contar a donde nos quedamos antes.

stock_de_frutas_2 = {'sandía': 345, 'durazno':127, 'frutilla': 900, 'pera': 341}

# enumerate puede tomar dos datos: enumerate(iterable, inicio). El inicio es el número a partir del cual
# empieza a contar. En este caso, quiero que la numeración continúe donde terminó el conteo anterior, para eso utilizo el largo
# de la lista actual

inicio = len(lista_frutas)

for indice, fruta in enumerate(stock_de_frutas_2, inicio):
    lista_frutas.append((indice, fruta, stock_de_frutas_2[fruta]))
    
print(lista_frutas)