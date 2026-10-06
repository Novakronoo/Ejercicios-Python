productos = {"Chocolate": 1.5, "M&M": 2.0, "Coca-Cola": 1.0, "Galletas": 1.2, "Agua": 0.5}
billetes = [100, 50, 20, 10, 5, 2, 1]
print("Productos disponibles:")
for producto, precio in productos.items():
    print(f"{producto}: ${precio}")
    
def calcular_vuelto(precio, billete):
    vuelto = billete - precio
    if vuelto < 0:
        return "El billete no alcanza para cubrir la compra."
    elif vuelto == 0:
        return "No hay vuelto."
    else:
        return vuelto
    
producto = input("Ingrese el nombre del producto que desea comprar: ")
if producto in productos:
    precio = productos[producto]
    print(f"El precio de {producto} es: ${precio}")
    billete = float(input("Ingrese el valor del billete que va a utilizar para pagar: "))
    vuelto = calcular_vuelto(precio, billete)
    print(f"Su vuelto es: {vuelto}")
    print("Gracias por su compra. ¡Que tenga un buen día!")
else:
    print("Ingrese un producto válido de la lista.")
    print("¡Que tenga un buen día!")


