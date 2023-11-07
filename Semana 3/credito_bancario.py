edad = 20
antiguedad = 7
ingreso = 2600

ingreso_minimo = 2500
ingreso_minimo_sin_antiguedad = 4000

# if (edad >= 18 and antiguedad >= 3 and ingreso >= ingreso_minimo) or (edad >= 18 and not antiguedad >= 3 and ingreso >= ingreso_minimo_sin_antiguedad):
#     print('El crédito ha sido aprobado!!')
# else:
#     print(' Crédito denegado. :(')

if edad >= 18 and antiguedad >= 3 and ingreso >= ingreso_minimo:
    print('apto credito')

elif edad >= 18 and ingreso >= ingreso_minimo_sin_antiguedad:
    print('apto credito')

else:
    print('credito no aprobado')
