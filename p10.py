materiales = {
    "Cerámica 30x60": 12,
    "Binda 5kg": 8,
    "Pastina 1kg": 2.5,
    "Separadores 100u": 2, 
}

hora_mano_obra = 15
hora_x_m2 = 0.50

print("Tienes que presupuestar un trabajo de revestimiento de una pared")
while True:
    try:
        largo_pared = float(input("Ingresa el largo de la pared en metros: "))
        ancho_pared = float(input("Ingresa el ancho de la pared en metros: "))
        if largo_pared <=0 or ancho_pared <=0:
            print("Por favor, ingresa valores positivos para el largo y ancho de la pared.")
        else:
            break
    except ValueError: 
        print("Por favor, ingresa un número válido para el largo y ancho de la pared.")

superficie_pared = largo_pared * ancho_pared
material_por_metro = {"Cerámica 30x60": 1.1, "Binda 5kg": 4.5, "Pastina 1kg": 0.3, "Separadores 100u": 22}

def materiales_necesarios(superficie, materiales):
    materiales_requeridos = {}
    for material, precio in materiales.items():
        cantidad_necesaria = superficie * material_por_metro.get(material, 0)
        materiales_requeridos[material] = cantidad_necesaria
    return materiales_requeridos

def calcular_costo_materiales(superficie, materiales):
    costo_total = 0
    for material, precio in materiales.items():
        cantidad_necesaria = superficie * material_por_metro.get(material, 0)
        costo_material = cantidad_necesaria * precio
        costo_total += costo_material
    return costo_total

def calcular_costo_mano_obra(superficie, costo_por_hora):
    horas_necesarias = superficie * hora_x_m2
    costo_mano_obra = horas_necesarias * costo_por_hora
    return costo_mano_obra

colocación = input("¿Desea colocar la cerámica en forma recta o diagonal? (recta/diagonal): ").strip().lower()
elección = input("¿Los materiales los provee el cliente o la empresa? (cliente/empresa): ").strip().lower()


while True:
    if colocación not in ["diagonal", "recta"]:
        colocación = input("Opción inválida. Por favor, ingresa 'diagonal' o 'recta'" )
        break
    elif colocación == "diagonal":
        print("Se aplicará un aumento por m2 del 10% en la cerámica, 35% en los separadores y 60% en la mano de obra.")
        material_por_metro["Cerámica 30x60"] = 1.20
        material_por_metro["Separadores 100u"] = 30
        hora_x_m2 *= 0.80
        break
    elif colocación == "recta":
        print("Se aplicará la colocación recta de la cerámica sin cambios(10% ya agregado de cerámica por recortes).")
        break
    else:
        break

while True:
    if elección not in ["cliente", "empresa"]:
        elección = input("Opción inválida. Por favor, ingresa 'cliente' o 'empresa'" )
        break
    else:
        break

def presupuesto_final(superficie, materiales, costo_por_hora, elección):
    costo_materiales = calcular_costo_materiales(superficie, materiales)
    costo_mano_obra = calcular_costo_mano_obra(superficie, costo_por_hora)
    if elección == "cliente":
        return costo_mano_obra
    elif elección == "empresa":
        return costo_materiales + costo_mano_obra
    
print("==========================================")
print(f"La superficie de la pared es : {superficie_pared} m2")
print("==========================================")
print(f"Los materiales necesarios para cubrir la pared son: ")
for material, cantidad in materiales_necesarios(superficie_pared, materiales).items():
    print(f" • {material}: {cantidad}")
print("==========================================")
print(f"El costo total de los materiales es: ${calcular_costo_materiales(superficie_pared, materiales)}")
print("==========================================")
print(f"El costo de la mano de obra es: ${calcular_costo_mano_obra(superficie_pared, hora_mano_obra)}")
print("==========================================")
print(f"El presupuesto final es: ${presupuesto_final(superficie_pared, materiales, hora_mano_obra, elección)}")
print("==========================================")
