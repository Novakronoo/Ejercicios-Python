
lista_compras = {
    "Jabón": 1,
    "Tomate": 3,
    "Leche": 2,
    "Bolsa de Papas": 1
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
supermercado = False
pasillo_visitado = []

print("Lista de Compras: ")
print(f"{lista_compras}")

print("Entras a un supermercado llamado TATA")

print("Ves tres pasillos con distintos productos")
while supermercado == False:
    ir_pasillo = input(
        "Cual eliges?\n"
        "(1) Pasillo de Verdulería\n"
        "(2) Pasillo de Lácteos\n"
        "(3) Pasillo de Limpieza\n"
        "(4) Ver Carrito "
    )

            
    if ir_pasillo == "1":
            if "1" in pasillo_visitado:
                print("Ya visitaste este pasillo, elegí otro")
                break
            else:
                pasillo_visitado.append(1)
                print("Escriba Salir si desea volver a los pasillos")
                print("Estos son los productos de la Verdulería: ")
                for producto, precio in Supermercado["Verdulería"].items():
                    print(f"- {producto}: ${precio}")
                while True:
                    elegido_verdulería = input("Elige un producto: ")
                    if elegido_verdulería in Supermercado["Verdulería"]:
                            productos_elegidos.append(elegido_verdulería)
                            print(f"Producto elegido: {elegido_verdulería}")
                    elif elegido_verdulería.lower() == "salir":
                        break
                    else: print("Elija un producto correcto!")
    
    elif ir_pasillo == "2":
            if "2" in pasillo_visitado:
                print("Ya visitaste este pasillo, elegí otro")
                break
            else:
                pasillo_visitado.append(2)
                print("Escriba Salir si desea volver a los pasillos")
                print("Estos son los productos Lácteos: ")
                for producto, precio in Supermercado["Lácteos"].items():
                    print(f"- {producto}: ${precio}")
                while True:
                    elegido_lácteos = input("Elige un producto: ")
                    if elegido_lácteos in Supermercado["Lácteos"]:
                            productos_elegidos.append(elegido_lácteos)
                            print(f"Producto elegido: {elegido_lácteos}")
                    elif elegido_verdulería.lower() == "salir":
                        break
                    else: print("Elija un producto correcto!")

    elif ir_pasillo == "3":
            if "3" in pasillo_visitado:
                print("Ya visitaste este pasillo, elegí otro")
                break
            else:
                pasillo_visitado.append(3)
                print("Escriba Salir si desea volver a los pasillos")
                print("Estos son los productos de Limpieza: ")
                for producto, precio in Supermercado["Limpieza"].items():
                    print(f"- {producto}: ${precio}")
                while True:
                    elegido_limpieza = input("Elige un producto: ")
                    if elegido_limpieza in Supermercado["Limpieza"]:
                            productos_elegidos.append(elegido_limpieza)
                            print(f"Producto elegido: {elegido_limpieza}")
                    elif elegido_verdulería.lower() == "salir":
                        break
                    else: print("Elija un producto correcto!")
    elif ir_pasillo == "4":
         print(f"Productos en su carrito: {productos_elegidos}")
    else: print("Elija un pasillo válido!")



        
            



         
#decision = input("Puedes seguir, ver tu carrito o volver a los pasillos")
#                    print("Continuar comprando")
#                    if decision.lower == "pasillo":
#                        break
#                    elif decision.lower == ""

