# break y continue

count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1

count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number) # imprime 0, 1, 2, 3
    if number == 3:
        break

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # En resumen: para condiciones cortas se puede usar if y else en línea
print('outside the loop')

# Bucle for
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number es un nombre temporal que referencia el elemento de la lista dentro del bucle
    print(number)       # number se imprimirá línea por línea, de 0 a 5

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)

language = 'Python'
for letter in language:
    print(letter)

for i in range(len(language)):
    print(language[i])

numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key) # sólo imprime las claves

for key, value in person.items():
    print(key, value) # así podemos acceder a claves y valores durante la iteración



#Bucles anidados

for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

    
# Range()

lst = list(range(11)) 
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # start y stop, paso por defecto 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}

for number in range(11):
    print(number)   # imprime 0 a 10, no incluye 11.

for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)

# Cuando se requiere una instrucción (por ejemplo después de :) pero no queremos ejecutar código, usamos pass para evitar errores. 
# También sirve como marcador para rellenar más adelante.
for number in range(6):
    pass