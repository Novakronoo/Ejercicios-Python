tipos_correos = {
    "Trabajo": [], 
    "Personal": [], 
    "Promociones": [], 
    "Urgente": [],
}
opciones = {
    "1": "Trabajo",
    "2": "Personal",
    "3": "Promociones",
    "4": "Urgente"
}

while True:
    print("\n(1) Trabajo" \
    "      \n(2) Personal" \
    "      \n(3) Promociones" \
    "      \n(4) Urgente" \
    "      \n(5) Salir")

    tipos = input("Ingresa los tipos separados por coma (ej. 1,2): ")

    if tipos.strip() == "5":
            print("Saliendo..")
            break
    
    lista_num = [num.strip() for num in tipos.split(",") if num.strip()]
    if not lista_num or not all(num in opciones for num in lista_num):
        print("Opción inválida. Solo debes ingresar números del 1 al 5 separados por coma.")
        continue
    
    desc = input("Ingresa la descripción del correo: ")
    while not desc:
        desc = input("La descripción no puede estar vacía. Inténtalo de nuevo: ").strip()
    
    for num in tipos.split(","):
        num = num.strip()
        if num in opciones:
            categoría = opciones[num]
            tipos_correos[categoría].append(desc)


print("\n Correos clasificados por categoría: ")

print("==========================================")

print("Trabajo: ")
for desc in tipos_correos["Trabajo"]:
    print(f"{desc}")

print("==========================================")

print("Personal: ")
for desc in tipos_correos["Personal"]:
    print(f"{desc}")

print("==========================================")

print("Promociones: ")
for desc in tipos_correos["Promociones"]:
    print(f"{desc}")

print("==========================================")

print("Urgente: ")
for desc in tipos_correos["Urgente"]:
    print(f"{desc}")

print("==========================================")
