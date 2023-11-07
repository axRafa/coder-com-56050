numero_1 = int(input("elige el 1er numero: "))
numero_2 = int(input("elige el 2do numero: "))

while True:

    txt = input("elige una opcion, suma, resta, multiplicacion, o finalizar: ")
    if txt == "suma":
        print(numero_1 + numero_2)
    elif txt == "resta":
        print(numero_1 - numero_2)
    elif txt == "multiplicacion":
        print(numero_1 * numero_2)
    elif txt == "finalizar":
        break
    else:
        print("esa opcion no es valida")
        
## Otra opcion

numero1 = int(input("escriba su primer numero,  "))
numero2 = int(input("escriba su segundo numero,  "))
opcion_de_cuenta = int(input("escriba 0 para sumar, 1 para restar, 2 para multiplicar, 3 para finalizar el programa, "))

while True:
    if opcion_de_cuenta == 0:
        print(numero1 + numero2)
        break
    elif opcion_de_cuenta == 1:
        print(numero1 - numero2)
        break
    elif opcion_de_cuenta == 2:
        print(numero1 * numero2)
        break
    elif opcion_de_cuenta == 3:
        print("programa finalizado")
        break
    else:
        print("opcion no valida")
        opcion_de_cuenta = int(input("escriba 0 para sumar, 1 para restar, 2 para multiplicar, 3 para finalizar el programa, "))