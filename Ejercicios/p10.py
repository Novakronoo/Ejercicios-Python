materiales = {
    "Cerámica 30x60": 12,
    "Binda 5kg": 8,
    "Pastina 1kg": 2.5,
    "Separadores 100u": 2, 
}
cantidad_materiales = {
    "Cerámica 30x60": 1, 
    "Binda 5kg": 5, 
    "Pastina 1kg": 1, 
    "Separadores 100u": 100
}
material_por_metro = {
    "Cerámica 30x60": 1.1, 
    "Binda 5kg": 4.5, 
    "Pastina 1kg": 0.3, 
    "Separadores 100u": 22
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


def materiales_necesarios(superficie, materiales):
    materiales_requeridos = {}
    for material, consumo in material_por_metro.items():
        cantidad_necesaria = superficie * consumo
        materiales_requeridos[material] = cantidad_necesaria
    return materiales_requeridos

def calcular_costo_materiales(superficie, materiales, material_por_metro, cantidad_materiales):
    costo_total = 0
    for material, precio in materiales.items():
        cantidad_necesaria = superficie * material_por_metro.get(material, 0)
        capacidad_por_unidad = cantidad_materiales.get(material, 1.0)

        capacidad_necesaria = cantidad_necesaria / capacidad_por_unidad
        costo_material = capacidad_necesaria * precio
        costo_total += costo_material
    return costo_total

def calcular_costo_mano_obra(superficie, costo_por_hora, horas_x_m2):
    horas_necesarias = superficie * horas_x_m2
    costo_mano_obra = horas_necesarias * costo_por_hora
    return costo_mano_obra



while True:
    colocación = input("Por favor, ingresa el tipo de colocación 'diagonal' o 'recta': " ).strip().lower()
    
    if colocación == "diagonal":
        print("Se aplicará un aumento por m2 del 10% en la cerámica, 35% en los separadores y 60% en la mano de obra.")
        material_por_metro["Cerámica 30x60"] = 1.20
        material_por_metro["Separadores 100u"] = 30
        hora_x_m2 = 0.80
        break
    elif colocación == "recta":
        print("Se aplicará la colocación recta de la cerámica sin cambios(10% ya agregado de cerámica por recortes).")
        break
    else:
        print("Opción inválida. Por favor, ingresa 'diagonal' o 'recta'.")

while True:
    elección = input("Por favor, ingresa el tipo de elección 'cliente' o 'empresa': " ).strip().lower()
    if elección in ["cliente", "empresa"]:
        break
    else: 
        print("Opción inválida. Por favor, ingresa 'cliente' o 'empresa'.")   

def presupuesto_final(superficie, materiales, costo_por_hora, elección, material_por_metro, cantidad_materiales, horas_x_m2):
    costo_materiales = calcular_costo_materiales(superficie, materiales, material_por_metro, cantidad_materiales)
    costo_mano_obra = calcular_costo_mano_obra(superficie, costo_por_hora, horas_x_m2)
    if elección == "cliente":
        return costo_mano_obra
    elif elección == "empresa":
        return costo_materiales + costo_mano_obra
    
print("==========================================")
print(f"La superficie de la pared es : {superficie_pared:.2f} m2")
print("==========================================")
print(f"Los materiales necesarios para cubrir la pared son: ")
for material, cantidad in materiales_necesarios(superficie_pared, materiales).items():
    print(f" • {material}: {cantidad:.2f} unidades")
print("==========================================")
print(f"El costo total de los materiales es: ${calcular_costo_materiales(superficie_pared, materiales, material_por_metro, cantidad_materiales):.2f}")
print("==========================================")
print(f"El costo de la mano de obra es: ${calcular_costo_mano_obra(superficie_pared, hora_mano_obra, hora_x_m2):.2f}")
print("==========================================")
print(f"El presupuesto final es: ${presupuesto_final(superficie_pared, materiales, hora_mano_obra, elección, material_por_metro, cantidad_materiales, hora_x_m2):.2f}")
print("==========================================")
