cantidad_de_numeros = int(input("Cuántos números quiere introducir?: "))

lista = []

for i in range(cantidad_de_numeros):
    numero = int(input("Ingrese el numero: "))
    lista.append(numero)
    
print("Lista de numeros: ", lista)

promedio = sum(lista) / len(lista)

print("El promedio de los numeros ingresados es:", promedio)


cant = int(input('Ingrese la cantidad de números a introducir: '))

lista = [0]*cant # Tengo que definirlo antes del loop?

for i in range(cant):
#    j = i+1
    lista[i] = float(input(f'Ingrese el número {i+1}: ')) # Por que no puedo poner {i+1}

media = sum(lista)/len(lista)
print('La media aritmética es: ',media)