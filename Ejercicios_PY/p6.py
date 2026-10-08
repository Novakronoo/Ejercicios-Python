print("Un grupo de amigos se encuentran para comprar un asado")

personas = {}
total_asado = float(input("¿Cuánto cuesta el asado en total?"))


print("Ingresa el nombre de tus bros :")
while True:
    nombre = input("Nombre (o 'listo' para terminar): ")
    if nombre.lower() == "listo":
        if len(personas) == 0:
            print("Debes ingresar al menos una persona.")
            continue
        break
    if nombre != "":
        personas[nombre] = 0.0

print("Ahora ingresa cuanto dinero pondrá cada persona:")
for nombre in personas:
    monto = float(input(f"{nombre} aportó: "))
    personas[nombre] = monto

total_aportado = sum(personas.values())

while total_aportado < total_asado:
    print(f"Falta ${total_asado - total_aportado:.2f} para cubrir el asado.")
    nombre = input("¿Quien debe poner mas dinero")
    if nombre not in personas:
        print("Ese nombre no existe.")
        continue
    extra = float(input(f"¿Cuánto más pone {nombre}? "))
    personas[nombre] += extra
    total_aportado = sum(personas.values())

print("\n-------------------------------------------")
print("¡Se juntó la plata! Reciben el asado.")
print("Calculando quién debe pagar y quién recibe...")
print("-------------------------------------------\n")

promedio = total_asado / len(personas)

debe = []
recibe = []

for nombre, monto in personas.items():
    diferencia = monto - promedio
    if diferencia > 0:
        recibe.append([nombre, diferencia])
    elif diferencia < 0:
        debe.append([nombre, abs(diferencia)])

print("\nQuienes deben pagar:")
for nombre, monto in debe:
    print(f"- {nombre}: debe ${monto:.2f}")

print("\nQuienes deben recibir:")
for nombre, monto in recibe:
    print(f"- {nombre}: recibe ${monto:.2f}")

print("\nPlan de pagos: ")

i = 0
j = 0
while i < len(debe) and j < len(recibe):
    nombre_debe, monto_debe = debe[i]
    nombre_recibe, monto_recibe = recibe[j]

    pago = min(monto_debe, monto_recibe)
    print(f"👉 {nombre_debe} le paga a {nombre_recibe}: ${pago:.2f}")

    debe[i][1] -= pago
    recibe[j][1] -= pago

    if debe[i][1] < 0.01:
        i += 1
    if recibe[j][1] < 0.01:
        j += 1