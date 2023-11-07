# try:
#     f = open("archivo_clase_8.txt", "w")
# except Exception as err:
#     print("El archivo no se pudo acceder:", err)

# f.write("Esto es un texto.\n")
# f.write("Esto es mas texto.\n")
# f.write("Un renglon mas no estaria mal.\n")
# f.close()

try:
    f = open("archivo_clase_8.txt", "r")
except Exception as err:
    print("El archivo no se pudo acceder:", err)
    
print(f.readline())
print(f.readline())
f.close()

