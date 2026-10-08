# Añadir y actualizar elementos al conjunto
# Una vez creado el conjunto no podemos cambiar elementos existentes, pero sí podemos añadir nuevos

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables) # Los elementos de vegetables se añaden a fruits

# Cambiar un conjunto a una lista

fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits) # {'mango', 'lemon', 'banana', 'orange'}

# La intersección devuelve un conjunto con los elementos que están presentes en ambos conjuntos

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
python.intersection(dragon)     # {'o', 'n'}

# Comprobar la diferencia entre conjuntos

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.difference(even_numbers) # {1, 3, 5, 7, 9}

python = {'p', 'y', 't', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
python.difference(dragon)     # {'p', 'y', 't'}  - El resultado es desordenado (propiedad de los conjuntos)
dragon.difference(python)     # {'d', 'r', 'a', 'g'}

# Comprobar conjuntos disjuntos 

even_numbers = {0, 2, 4, 6, 8}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers) # Verdadero, porque no comparten elementos

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
python.isdisjoint(dragon)  # Falso, comparten {'o', 'n'}