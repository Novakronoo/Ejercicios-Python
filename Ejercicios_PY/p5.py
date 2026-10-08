herramientas = []
herramientas_ordenadas = []

print("Ingrese las herramientas y su tamaño que desea agregar a la lista (escriba 'fin' para terminar):")

while True:
    herramienta = input("Ingrese una herramienta: ")
    if herramienta.lower() == 'fin':
        break
    while True:
            tamaño = float(input(f"Ingrese el tamaño de {herramienta}: "))
            break
    herramientas.append((herramienta, tamaño))


    if not herramientas:
        print("No se han ingresado herramientas.")
        exit()

def ordenar_herramientas(herramientas):
    return sorted(herramientas, key=lambda x: x[1])


herramientas_ordenadas = ordenar_herramientas(herramientas)

print("\nLista de herramientas ordenadas por tamaño de menor a mayor:")
for herramienta, tamaño in herramientas_ordenadas:
    print(f"- {herramienta}: {tamaño} cm")