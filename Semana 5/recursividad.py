# def factorial(numero):
#     print('valor inicial', numero)
#     if numero > 1:
#         numero = numero * factorial(numero-1)
#     print('valor final', numero)
#     return numero

# print(factorial(4))

# 1! = 1

# 2! = 2 * 1 = 2 * 1! = 2

# 3! = 3 * 2 * 1 = 3 * 2! = 6

# 4! = 4 * 3 * 2 * 1 = 4 * 3! = 24

# 5! = 5 * 4 * 3 * 2 * 1 = 5 * 4! = 120


def es_par():
    numero = int(input('Ingrese un numero impar: '))
    if numero % 2 != 1:
        es_par()
    else:
        print('Bien hecho!')
        
es_par()