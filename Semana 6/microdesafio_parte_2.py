def dividir(a, b):
    try:
        resultado = c # Esta linea va a forzar la excepción NameError
        return a / b
    except ZeroDivisionError:
        print("La operación no se pudo completar porque hay una división por cero.")
    except TypeError:
        print("Hubo un error en los tipos de dato.")
    except NameError:
        print("El argumento apunta a una variable intexistente.")
    except Exception as e:
        print("La operacion no se pudo completar porque: ")
        
print(dividir(67, 23))
print(dividir(67, 0))
print(dividir(67, (45, 'asdf')))
