def anio_bisiesto():
    try:
        anio = int(input('Ingrese el año: '))
    except:
        print("No se ingreso un dato valido.")
        return None
    else:
        print("El dato es válido.")
    finally:
        print('Esta linea se deberia ejecutar siempre')
                
    if anio % 400 == 0 or (anio %4 == 0 and anio % 100 != 0):
            print(f"el año {anio} es bisiesto")
    else:
        print(f"El año {anio} no es bisiesto")

anio_bisiesto()

Pre-entrega 1:

Formato de diccionario recomendado para la base de datos:
{
    "nombre_de_usuario": "contraseña",
    "otro_usuario": 'otra_contraseña',
    }

Funciones necesarias para aprobar la entrega:
    - Una funcion de registro de usuarios
    - Una función de ingreso o login
    - Una funcion para mostrar los datos por consola.