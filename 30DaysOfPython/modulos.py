#Importar funciones y renombrarlas
from sets import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Asabneh','Yetayeh'))
print(total(1, 9))
mass = 100
weight = mass * g
print(weight)
print(p)
print(p['firstname'])

# Imports útiles

import math
print(math.pi)           # 3.141592653589793, constante pi
print(math.sqrt(2))      # 1.4142135623730951, raíz cuadrada
print(math.pow(2, 3))    # 8.0, potencia
print(math.floor(9.81))  # 9, redondeo hacia abajo
print(math.ceil(9.81))   # 10, redondeo hacia arriba
print(math.log10(100))   # 2, logaritmo base 10

from math import pi#*(all)
print(pi)

from random import random, randint # as RANDOM, RANDINT
print(random())   # no necesita parámetros; devuelve un valor entre 0 y 0.9999
print(randint(5, 20)) # devuelve un entero aleatorio en [5, 20] (inclusive)

import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~