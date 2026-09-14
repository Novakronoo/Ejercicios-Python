import random

valijas = {"roja": 3, "azul": 4, "amarilla": 5}
mudas = {"invierno", "verano", "lluvia" , "casual", "formal", "deportiva"}
pronósticos = {"soleado", "lluvioso", "templado", "frio"}
mudas_elegidas=[]


def pronostico(pronósticos):
    return f"El clima será {pronósticos}"
for dia in range(1, 4):
    pronostico_elegido = random.choice(list(pronósticos))
    mensaje_clima = pronostico(pronostico_elegido)
    print(f"Día {dia}: {mensaje_clima}")

print("Valijas disponibles:")
for valija, capacidad in valijas.items():
    print(f"{valija}: {capacidad} mudas")

elegir_valija = input(f"Elige una valija {list(valijas)}: ")
if elegir_valija in valijas:
    print(f"Has elegido la valija {elegir_valija} con capacidad para {valijas[elegir_valija]} mudas.")
else:
    print("Por favor, elige una valija válida.")

print("Mudas disponibles:")
for muda in mudas:
    print(f"{muda}")

print("Puede elegir hasta 3 mudas para llevar en su valija.")
for i in range(3):
    elegir_muda = input(f"Elige la muda {i} de {list(mudas)}: ")
    if elegir_muda in mudas:
        mudas_elegidas.append(elegir_muda)
        print(f"Has elegido la muda {elegir_muda}.")
    else:
        print("Por favor, elige una muda válida.")

print("Resumen de mudas elegidas:")
if mudas_elegidas:
    for muda in mudas_elegidas:
        print(f"Muda {muda}: {mudas_elegidas.count(muda)}")
    
def calcular_mudas(valija, muda):
    capacidad_valija = valijas[valija]
    cantidad_mudas = mudas[muda]
    if cantidad_mudas > capacidad_valija:
        return f"No puedes llevar {cantidad_mudas} mudas en la valija {valija}. Solo puedes llevar {capacidad_valija} mudas."
    else:
        return f"Puedes llevar {cantidad_mudas} mudas en la valija {valija}."