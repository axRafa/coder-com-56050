# Microdesafío

def dividir(a, b):
    if b == 0:
        return None
    return a / b

print(dividir(34, 0))
print(dividir(7, 2))

def dividir_2(a, b):
    try:
        return a / b
    except Exception as error:
        print("La operación no se pudo completar porque: ", error)


print(dividir_2(34, 0))
print(dividir_2(7, 2))