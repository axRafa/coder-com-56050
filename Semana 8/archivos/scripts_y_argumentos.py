import sys

print(sys.argv)

try:
    f = open("archivo_clase_8.txt", "w")
except Exception as err:
    print("El archivo no se pudo acceder:", err)

for texto in sys.argv[1:]:
    f.write(texto+"\n")