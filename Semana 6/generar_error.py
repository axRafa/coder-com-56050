# print("Elija la opcion 1, 2 , 3 o 4.")
# print("1. Soy un string - 4")
# print("2. 4/0")
# print("3. prnt('Mostrando Codigo'")
# print("4. int('Quiero ser un Numero")

# opcion = input("Que numero de opcion desea seleccionar: ")

# if opcion == "1" or "2" or "3" or "4":
#     if opcion == "1":
#         print("El error se produce porque estas realizando una operacion matematica entre un string y un int")
        
#     if opcion == "2":
#         print("Se esta realizando una división por cero")
        
#     if opcion == "3":
#         print("Error de typeo")
        
#     if opcion == "4":
#         print("Operacion no soportada")

def menu():
    print("Selecciona una opción:")
    print("1. 'Soy un string' - TypeError")
    print("2. 4/0 - ZeroDivisionError")
    print("3. prnt('Mostrando código') - NameError")
    print("4. int('Quiero ser un número') - ValueError")
    
    opcion = input("Ingrese el número de opción: ")
    
    if opcion == '1':
        try:
            resultado = 'Soy un string' - 4
        except TypeError as e:
            print(f"Error: {e}")
    
    elif opcion == '2':
        try:
            resultado = 4 / 0
        except ZeroDivisionError as e:
            print(f"Error: {e}")
    
    elif opcion == '3':
        try:
            prnt('Mostrando código')
        except NameError as e:
            print(f"Error: {e}")
    
    elif opcion == '4':
        try:
            resultado = int('Quiero ser un número')
        except ValueError as e:
            print(f"Error: {e}")
    
    else:
        print("Opción no válida")
        
menu()