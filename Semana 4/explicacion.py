# while True:
#    print('Este mensaje.')

# while False:
#     print('Este mensaje nunca se va a imprimir.')

# contador = 0

# while contador != 5:
#     print('Esto se va a imprimir')
#     contador += 1
    
# lista = [1, 2, 3, 4, 5]

# nombres = ['uno', 'dos', 'tres', 'cuatro', 'cinco']

# diccionario_numeros = dict(zip(nombres, lista))

# print(diccionario_numeros)

# for numero in diccionario_numeros.values():
#     print('Este mensaje es el numero:', numero)
    
# lista = [1, 2, 3, 4, 5]
# limite = len(lista)
# cursor = 0

# while cursor != limite:
#     print('Este es el mensaje numero:', lista[cursor])
#     cursor += 1
    
# # SOlucion Microdesafio
numero=int(input("Ingresa un numero impar:"))

while numero%2 != 1:
     numero=int(input("Ingresa un numero impar:"))
else:
  print("Bien hecho")
  
def es_par(numero):
    return (numero & 1) == 0

1100

1: 1
2: 0 
4: 1
8: 1
