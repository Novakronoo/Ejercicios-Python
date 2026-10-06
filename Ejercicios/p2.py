#Problema 2 — Preparar un café.
#Detallá el proceso completo, desde juntar los materiales hasta el primer sorbo. Pensá qué pasa si te
#falta algún ingrediente a mitad de camino.
#   Variables: Agua, Café, Azúcar, Taza
#   Funciones: pedir_taza, pedir_agua, pedir_cafe

import time


def pedir_taza():
    taza = float(input("Ingrese la capacidad de la taza en ml: "))
    if taza <= 40:
        print("La taza debe tener una capacidad aceptable.")
        exit()
    else:return taza

def pedir_agua():
    agua = float(input("Ingrese la cantidad de agua en ml: "))
    if agua <= 20:
        print("No hay suficiente agua para preparar un café.")
        exit()
    else:return agua

def pedir_cafe():
    cafe = int(input("Ingrese la cantidad de café en cucharadas: "))
    if cafe <= 0:
        print("No hay suficiente café para preparar un café.")
        exit()
    else:return cafe

taza = pedir_taza()
agua = pedir_agua()
cafe = pedir_cafe()
azucar = int(input("Ingrese la cantidad de azúcar en cucharadas: "))
print("Preparando café con los siguientes ingredientes:")
print(f"- Colocando Taza: {taza} ml")
time.sleep(1)
print(f"- Hirviendo Agua: {agua} ml")
time.sleep(4)
print(f"- Agregando Café: {cafe} cucharadas")
time.sleep(2)
print(f"- Agregando Azúcar: {azucar} cucharadas")
time.sleep(2)

print(f"¡Listo! Disfrutá tu café de {taza} ml con {cafe} cucharadas de café y {azucar} cucharadas de azúcar.")
