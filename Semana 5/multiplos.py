def es_multiplo_1(a,b):
  if a % b == 0:
      resultado = f"El nro {a} es multiplo de {b}"
  elif b % a == 0:
      resultado = f"El nro {b} es multiplo de {a}"
  else:
      resultado = f"¡El nro {a} no es multiplo de {b} ni vice versa!"
  return resultado

#a = input('ingrese un numero')
#b = input('ingrese otro numero')

print(es_multiplo_1(int(input('ingrese el numero')), int(input('ingrese el numero'))))
print(es_multiplo_1(5, 4))
print(es_multiplo_1(10, 2))
print(es_multiplo_1(10, 10))

# def es_multiplo_2():
#     numero1= int(input('Escribe un numero entero: '))
#     numero2= int(input('Escribe el 2° numero entero: '))
#     numero3= int(numero1/numero2)
#     if numero3 == True:
#         print('Es multiplo')
#     else:
#         print('No es multiplo')
# es_multiplo_2()