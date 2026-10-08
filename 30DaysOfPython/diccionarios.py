# Acceder a elementos del diccionario
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(person['first_name']) # Asabeneh
print(person['country'])    # Finland
print(person['skills'])     # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'][0])  # JavaScript
print(person['address']['street']) # Space street
print(person['city'])       # Error
# primero compruebe si existe la clave o use el método get. El método get devuelve None si la clave no existe
print(person.get('first_name')) # Asabeneh
print(person.get('country'))    # Finland
print(person.get('skills')) #['HTML','CSS','JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get('city'))   # None

# Podemos añadir nuevos pares clave-valor al diccionario
person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person)

# Modificar elementos del diccionario
person['first_name'] = 'Eyob'
person['age'] = 252
del person['is_married']  # elimina el elemento is_married

#El método items() convierte el diccionario en una lista de tuplas.
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])

#Podemos usar el método copy() para copiar un diccionario. Usar copy evita que el diccionario original sea modificado.
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

#El método values() nos da una lista con todos los valores del diccionario
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values) # dict_values(['value1', 'value2', 'value3', 'value4'])