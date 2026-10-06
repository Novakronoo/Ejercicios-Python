import random
import time
valijas = {"Roja": 3, "Azul": 4, "Amarilla": 5}
mudas = {"Invierno", "Verano", "Lluvia" , "Casual", "Deportiva"}
pronósticos = {"Soleado", "Lluvioso", "Templado", "Frio"}
mudas_elegidas=[]
pronósticos_por_dia = {}
print(" "),print(" ")
print("--Enciendes la TV y ves el pronóstico del clima para los próximos 3 días--")
time.sleep(1)
print(" ")
def pronostico(pronósticos):
    return f"El clima será {pronósticos}"
for dia in range(1, 4):
    pronostico_elegido = random.choice(list(pronósticos))
    pronósticos_por_dia[dia] = pronostico_elegido
    mensaje_clima = pronostico(pronostico_elegido)
    time.sleep(1)
    print(f"Día {dia}: {mensaje_clima}")

print(" ")
time.sleep(1)
print("--Ahora, elige una valija y las mudas que deseas llevar contigo--")
print(" ")
time.sleep(1)
print("---Valijas disponibles---")
print(" ")
time.sleep(1)
for valija, capacidad in valijas.items():
    print(f"-{valija}: Capacidad para {capacidad} mudas")
print(" ")
elegir_valija = input(f"--Elige una de estas 3 valijas {list(valijas.keys())}: ")
if elegir_valija in valijas:
    print(f"--Has elegido la valija {elegir_valija} con capacidad para {valijas[elegir_valija]} mudas.")
else:
    print("--Por favor, elige una valija válida.")
print(" ")
time.sleep(1)
print("---Mudas disponibles---")
for muda in mudas:
    print(f"        -{muda}-")
print(" ")
time.sleep(1)
print("--Puede elegir hasta 3 mudas para llevar en su valija--")
print(" ")
for i in range(capacidad := valijas[elegir_valija]):
    elegir_muda = input(f"--Elige la muda {i} de {list(mudas)}: ")
    if elegir_muda in mudas:
        mudas_elegidas.append(elegir_muda)
        print(f"--Has elegido la muda {elegir_muda}.")
    else:
        print("--Por favor, elige una muda válida--")
        
compatibles = {
    "Soleado": {"Verano", "Deportiva"},
    "Lluvioso": {"Lluvia"},
    "Templado": {"Casual", "Verano"},
    "Frio": {"Invierno"}
}
print(" ")
for dia, clima in pronósticos_por_dia.items():
    mudas_necesarias = compatibles[clima]
    mudas_disponibles = mudas_necesarias & set(mudas_elegidas)

    if not mudas_disponibles:
        print(
            f"--Para el día {dia}, con clima {clima}, "
            f"--falta una muda necesaria: {', '.join(mudas_necesarias)}."
        )
    else:
        print(f"--La muda elegida para el día {dia} ({clima}) es {', '.join(mudas_disponibles)}.")
print(" ")
time.sleep(1)
print("--Resumen de mudas elegidas--")
if mudas_elegidas:
    for muda in mudas_elegidas:
        print(f"        -Muda {muda.capitalize()}-")
print(" ")
print("  Buena suerte en tu viaje!")
print(" ")