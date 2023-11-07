edad = 25
antiguedad = 2
ingreso = 1500

# Por defecto el credito no esta aprobado.
aprobado = False

if edad >= 18:
    if antiguedad >= 3 and ingreso >= 2500:
        aprobado = True

    elif ingreso >= 4000:
        aprobado = True

#     else:
#         aprobado = False

# else:
#     aprobado = False


if aprobado:
    print('Credito aprobado!')
else:
    print('Credito denegado.')