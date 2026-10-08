print("Bienvenido al programa")

print("Debe ingresar una contraseña que contenga: " \
"\n Al menos 8 caracteres \n Al menos una mayúscula \n Al menos un numero")

while True:
    contraseña = input("Ingrese una contraseña:")

    tiene_mayúscula= False
    tiene_numero = False

    for letra in contraseña:
        if letra.isupper():
           tiene_mayúscula = True
        if letra.isdigit():
           tiene_numero = True

    if len(contraseña) >= 8 and tiene_mayúscula and tiene_numero:
       print("Su contraseña es correcta")
       break
    else:
        print("La contraseña debe contener al menos 8 caracteres, una mayúscula y un número")