plantas = {"Jazmín" : 3, "Glandularia": 3, "Duranta": 2, "Ceibo": 5, "Mburucuyá": 4, "Kalanchoe": 6}
plantas_regadas=[]
plantas_no_regadas=[]

print("Bienvenido al regadero de plantas!")

def debe_regar(dia: int, frecuencia: int) -> bool:
        return dia % frecuencia == 0

for dia in range(1, 8):
    print("." * 25)
    print(f"Día numero: {dia}")
    for planta, frecuencia in plantas.items():
          if debe_regar(dia, frecuencia):
                print(f"La planta {planta} se debe regar")
                while True:
                    respuesta = input("Desea regadla?(Si o No): ")
                    print("." * 25)
                    if respuesta.lower() == "si":
                     plantas_regadas.append((planta, dia))
                     break
                    if respuesta.lower() == "no":
                      plantas_no_regadas.append((planta, dia))
                      break
                    else: print("Por favor ingrese Si o No")
print("." * 25)
print("." * 25)


print("\n" + "=" * 32)
print("     REPORTE FINAL DE RIEGO     ")
print("=" * 32)

print("\n--- Plantas Regadas ---")
if plantas_regadas:
    for planta, dia in plantas_regadas:
        print(f" • {planta} en el Día {dia}")
else:
    print(" (Ninguna planta fue regada)")

print("\n--- Plantas No Regadas ---")
if plantas_no_regadas:
    for planta, dia in plantas_no_regadas:
        print(f" • {planta} en el Día {dia}")
else:
    print(" (No hubo descuidos)")

print("\n" + "=" * 32)

