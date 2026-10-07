web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) #Resultado: HTML CSS JavaScript React

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '# '.join(web_tech)
print(result) #Resultado: HTML# CSS# JavaScript# React

challenge = 'thirty days of python'
print(challenge.strip('noth')) # 'irty days of py' (elimina los caracteres dados del inicio y final)

challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
challenge = 'thirty, days, of, python'
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']

challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) #'thirty days of coding'

challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True

challenge = '30 days of python'
print(challenge.startswith('thirty')) # False (no empieza con 'thirty')