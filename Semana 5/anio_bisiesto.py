def anio_bisiesto(anio):
    if type(anio) != int:
        print('El dato ingresado no es váldio')
        return False
    
    if anio % 400 == 0 or (anio %4 == 0 and anio % 100 != 0):
        print(f"el año {anio} es bisiesto")
    else:
        print(f"El año {anio} no es bisiesto")

anio_bisiesto(2012)
anio_bisiesto(2010)
anio_bisiesto(2000)
anio_bisiesto(1900)