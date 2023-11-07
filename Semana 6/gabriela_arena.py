# Gabriela Arenas
#!/usr/bin/env python

import json

# Función para cargar el archivo JSON
def cargar_base_datos():
    try:
        with open('user_pass.json', 'r') as f:
            data = json.load(f)
        return data
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return {}

# Función para validar un usuario
def validar_usuario(bd, username):
    return username in bd

# Función para validar un password
def validar_password(bd, username, password):
    return bd.get(username) == password

# Función para registrar un nuevo usuario
def registrar_usuario(bd, username, password):
    bd[username] = password
    with open('user_pass.json', 'w') as f:
        json.dump(bd, f)

# Cargar la base de datos
bd = cargar_base_datos()

username = input('Ingrese su usuario: ')

if validar_usuario(bd, username):
    password = input("Ingrese su password: ")
    if validar_password(bd, username, password):
        print("Bienvenido, {}, se acaba de loguear correctamente".format(username))
    else:
        print("Contraseña incorrecta para el usuario ingresado")
else:
    print("El usuario {} no existe.".format(username))
    nuevo_usuario = input('¿Desea registrar un nuevo usuario? (Sí/No): ')
    if nuevo_usuario.lower() == 'si':
        password = input('Ingrese la contraseña para {}: '.format(username))
        registrar_usuario(bd, username, password)
        print("Usuario {} registrado con éxito.".format(username))