
lista_compras = {
    "Jabón",
    "Tomate",
    "Leche",
    "Queso",
    "Esponja",
    "Yogur",
    "Zapallo",
}
pasillos = {
    "Pasillo de Verdulería": 1,
    "Pasillo de Lácteos": 2,
    "Pasillo de Limpieza": 3,
}
Supermercado = {
"Verdulería": {
    "Lechuga": 3,
    "Tomate": 2,
    "Sandia": 3,
    "Zapallo": 5,
},
"Lácteos": {
    "Leche": 2,
    "Yogur": 3,
    "Chocolatada": 3,
    "Queso": 4,
},
"Limpieza" :{
    "Jabón": 2,
    "Alcohol": 3,
    "Esponja": 1,
    "Limpiador": 3,
 }, 
}



productos_elegidos = []
pasillo_visitado = []

print("Lista de Compras: ")
for producto in lista_compras:
     print(f"- {producto}")
print("---------------------------\n")

print("Entras a un supermercado llamado TATA")

while True:
    print(f"(1) {'[VISITADO] Pasillo de Verdulería' if 1 in pasillo_visitado else 'Pasillo de Verdulería'}")
    print(f"(2) {'[VISITADO] Pasillo de Lácteos' if 2 in pasillo_visitado else 'Pasillo de Lácteos'}")
    print(f"(3) {'[VISITADO] Pasillo de Limpieza' if 3 in pasillo_visitado else 'Pasillo de Limpieza'}")

    print("(4) Ver Carrito")
    print("(5) Finalizar compra")

    ir_pasillo = input("Opción: ")

    if ir_pasillo == "1":
                if 1 in pasillo_visitado:
                    print("\n❌ Ya visitaste la Verdulería, no puedes volver a entrar.")
                    continue
                else:
                    pasillo_visitado.append(1)
                    print("\n--- PASILLO VERDULERÍA ---")
                    print("Escriba Salir si desea volver a los pasillos")
                    for producto, precio in Supermercado["Verdulería"].items():
                        print(f"- {producto}: ${precio}")
    
                    while True:
                        elegido_verdulería = input("Elige un producto: ").capitalize()
                        if elegido_verdulería in Supermercado["Verdulería"]:
                                productos_elegidos.append(elegido_verdulería)
                                print(f"-> {elegido_verdulería} agregado al carrito.")
                        elif elegido_verdulería.lower() == "salir":
                            break
                        else: print("Elija un producto que este en el pasillo!")
    
    elif ir_pasillo == "2":
                if 2 in pasillo_visitado:
                    print("\n❌ Ya visitaste Lácteos, no puedes volver a entrar.")
                    continue
                pasillo_visitado.append(2)
                print("\n--- PASILLO LÁCTEOS ---")
                print("Escriba Salir si desea volver a los pasillos")
                for producto, precio in Supermercado["Lácteos"].items():
                    print(f"- {producto}: ${precio}")
                while True:
                    elegido_lácteos = input("Elige un producto: ").capitalize()
                    if elegido_lácteos in Supermercado["Lácteos"]:
                            productos_elegidos.append(elegido_lácteos)
                            print(f"-> {elegido_lácteos} agregado al carrito.")
                    elif elegido_lácteos.lower() == "salir":
                        break
                    else: print("Elija un producto que este en el pasillo!")

    elif ir_pasillo == "3":
                if 3 in pasillo_visitado:
                    print("\n❌ Ya visitaste Limpieza, no puedes volver a entrar.")
                    continue
                pasillo_visitado.append(3)
                print("\n--- PASILLO LIMPIEZA ---")
                print("Escriba Salir si desea volver a los pasillos")
                for producto, precio in Supermercado["Limpieza"].items():
                    print(f"- {producto}: ${precio}")
                while True:
                    elegido_limpieza = input("Elige un producto: ").capitalize()
                    if elegido_limpieza in Supermercado["Limpieza"]:
                            productos_elegidos.append(elegido_limpieza)
                            print(f"-> {elegido_limpieza} agregado al carrito.")
                    elif elegido_limpieza.lower() == "salir":
                        break
                    else: print("Elija un producto que este en el pasillo!")

    elif ir_pasillo == "4":
        print("Este es su carrito: ")
        if not productos_elegidos:
            print("El carrito está vacío.")
        else:
            for producto in productos_elegidos:
                for pasillo, productos in Supermercado.items():
                    if producto in productos:
                        print(f"- {producto}: ${productos[producto]}")
                        break

    elif ir_pasillo == "5":
        if not productos_elegidos:
            print("No hay productos para realizar una compra")
            continue
        else:
         total_a_pagar = 0
         for producto in productos_elegidos:
            for pasillo, productos in Supermercado.items():
                if producto in productos:
                    total_a_pagar += productos[producto]
                    break

         print(f"\nTotal a pagar: ${total_a_pagar}")
         while True:
            try:
                pago = float(input("Ingrese su pago: "))

                if pago < total_a_pagar:
                    print("Dinero insuficiente!")
                else:
                    vuelto = pago - total_a_pagar
                    print(f"Pago realizado con éxito! Su vuelto es: ${vuelto}")
                    break
            except ValueError:
                    print("Monto inválido. Ingrese un número.")

         print("\n==========================================")
         print("         RESUMEN DE TU COMPRA             ")
         print("==========================================")

         comprados = []
         faltantes = []

         for item in lista_compras:
            if item in productos_elegidos:
                comprados.append(item)
            else:
                faltantes.append(item)
        print(" Productos de tu lista que COMPRASTE:")
        if comprados:
            for prod in comprados:
                print(f"   [✓] {prod}")
        else:
            print("   Ninguno")

        print("\n Productos de tu lista que FALTARON:")
        if faltantes:
            for prod in faltantes:
                print(f"   [X] {prod}")
        else:
            print("   ¡Felicidades! Compraste todo lo de la lista.")

        print("==========================================")
        break


    else: print("\n¡Opción inválida! Elija un número del menú!")

