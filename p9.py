
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
productos_verdulería = {
    "Lechuga": 3,
    "Tomate": 2,
    "Sandia": 3,
    "Zapallo": 5,
}
productos_lácteos = {
    "Leche": 2,
    "Yogur": 3,
    "Chocolatada": 3,
    "Queso": 4,
}
productos_limpieza = {
    "Jabón": 2,
    "Alcohol": 3,
    "Esponja": 1,
    "Limpiador": 3,
}


productos_elegidos = []
supermercado = False
pasillo_visitado = []

def Cesta(productos_elegidos):
   return 
print(f"Tus productos elegidos son: {productos_elegidos}")

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
        "Opción: "
    )

    if ir_pasillo == "1":
        print("Estos son los productos de la Verdulería: ")
        print("Lechuga - $1",
                                  "Tomate - $1",
                                  "Sandia - $4",
                                  "Zapallo - $5",
                                  )
        for nombre_pa, numero_pa in pasillos.items():
            pasillo_visitado.append([nombre_pa, numero_pa])
        while True:
            mensaje_p_elegido = Cesta(productos_elegidos)
            elegido_verdulería = input("Elige uno de estos productos: ")
            if elegido_verdulería in productos_verdulería:
                for producto, precio in productos_verdulería.items():
                    print(f"Producto elegido: {mensaje_p_elegido}")
                else: print("Elija un producto correcto!")
                print("a")
                mensaje_p_elegido = Cesta(producto, precio)
                print({mensaje_p_elegido})
    else: print("Elija un producto correcto!")



        
            



         
#decision = input("Puedes seguir, ver tu carrito o volver a los pasillos")
#                    print("Continuar comprando")
#                    if decision.lower == "pasillo":
#                        break
#                    elif decision.lower == ""

