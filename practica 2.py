numero = 1
cantidad = 0
suma = 0
while numero != 0:
    numero = int (input("ingrese un numero"))
    if numero != 0:
        suma = suma + numero
        cantidad = cantidad + 1

print (f"Usted ingreso{cantidad} y la suma es :{suma}")        