def anio_bisiesto():
    try:
        anio = int(input('Ingrese el año: '))
    except:
        print("No se ingreso un dato valido.")
        return None
    
    if anio % 400 == 0 or (anio %4 == 0 and anio % 100 != 0):
            print(f"el año {anio} es bisiesto")
    else:
        print(f"El año {anio} no es bisiesto")

anio_bisiesto()
