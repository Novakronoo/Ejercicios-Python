# If Abreviación
a = 3
print('A es positivo') if a > 0 else print('A es negativo') # Se cumple la primera condición, imprimirá 'A es positivo'

# If Condicionales anidados

a = 0
if a > 0:
    if a % 2 == 0:
        print('A es un número positivo y par')
    else:
        print('A es un número positivo')
elif a == 0:
    print('A es cero')
else:
    print('A es un número negativo')


# If y operadores lógicos

a = 0
if a > 0 and a % 2 == 0:
    print('A es un número positivo y par')
elif a > 0 and a % 2 != 0:
    print('A es un número positivo')
elif a == 0:
    print('A es cero')
else:
    print('A es un número negativo')

user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
    print('Acceso concedido!')
else:
    print('Acceso denegado!')
