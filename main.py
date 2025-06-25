import random 

elementos = "+-/*!&$#?=@<>abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

longitud = int(input("introduce la longitud de tu contraseña segura: "))

contraseña = ""

for i in range(longitud):
    contraseña += random.choice(elementos)

print(f"Tu nueva contraseña segura es : {contraseña}")
