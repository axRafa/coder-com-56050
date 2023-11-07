def promedio(*args):
    print(args)
    return sum(args) / len(args)

resultado = promedio(8, 9, 14, 64)
print(resultado)

print(promedio(int(input("ingrese valores: "))))

# lista_numeros = []

# while True:
#     numero = input('Ingrese un valor: ')
#     if numero == 'exit':
#         break
#     numero = int(numero)
#     lista_numeros.append(numero)
    
# print(promedio(lista_numeros))