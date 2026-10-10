# Un método 
language = 'Python'
lst = list(language)  # convertir la cadena en lista
print(type(lst))      # list
print(lst)            # ['P', 'y', 't', 'h', 'o', 'n']

# Segunda forma: comprensión de listas [i for i in iterable if expresión]

lst = [i for i in language]
print(type(lst))      # list
print(lst)            # ['P', 'y', 't', 'h', 'o', 'n']


# generar números
numbers = [i for i in range(11)]  # genera números de 0 a 10
print(numbers)                    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# también puedes hacer operaciones matemáticas durante la iteración
squares = [i * i for i in range(11)]
print(squares)                    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# también se pueden generar listas de tuplas
numbers = [(i, i * i) for i in range(11)]
print(numbers)                    # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# Funciones lambda

# función nombrada
def add_two_nums(a, b):
    return a + b

print(add_two_nums(2, 3))  # 5

# con lambda
add_two_nums = lambda a, b: a + b
print(add_two_nums(2, 3))  # 5

# lambda autoejecutable
print((lambda a, b: a + b)(2, 3))  # 5

square = lambda x: x ** 2
print(square(3))    # 9
cube = lambda x: x ** 3
print(cube(3))      # 27

# múltiples variables
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3))  # 22

#Funciones con lambda

def power(x):
    return lambda n: x ** n

cube = power(2)(3)   # la función power ahora se usa con dos pares de paréntesis
print(cube)          # 8
two_power_of_five = power(2)(5)
print(two_power_of_five)  # 32