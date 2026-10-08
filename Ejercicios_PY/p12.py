print("El local acepta reservas limitadas por mesa y franja horaria")

local_horarios = {
    "Mañana": ["9:00", "10:00", "11:00", "12:00", "13:00"],
    "Tarde": ["14:00", "15:00", "16:00", "17:00", "18:00"],
    "Noche": ["19:00", "20:00", "21:00", "22:00", "23:00"]
}
local_mesas = {
    "Mesa 1": 2,
    "Mesa 2": 4,
    "Mesa 3": 6,
    "Mesa 4": 6,
}
reservas = []

def ocupar_mesa(mesa, horario):
    if mesa in local_mesas and horario in local_horarios["Mañana"] + local_horarios["Tarde"] + local_horarios["Noche"]:
        reservas.append((mesa, horario))
    else:
        print("Por favor, elige una mesa y un horario válidos.")

while True:
    print("Para salir del programa ingresa 'Salir' en cualquier momento.")
    print("Horarios disponibles:")
    for franja, horarios in local_horarios.items():
        print(f"{franja}: {', '.join(horarios)}")
    print("Mesas disponibles:")
    for mesa, capacidad in local_mesas.items():
        print(f"{mesa}: Capacidad para {capacidad} personas")

    input_franja = input("Elige una franja horaria: ")
    if input_franja.lower() == "salir":
        break
    if input_franja in local_horarios:
        print(f"Has elegido la franja horaria {input_franja}.")
        input_horario = input(f"Elige un horario de la franja {input_franja}: ")
        if input_horario in local_horarios["Mañana"] + local_horarios["Tarde"] +local_horarios["Noche"]:
            print(f"Has elegido el horario {input_horario}.")
            input_mesa = input(f"Elige una mesa disponible {list(local_mesas.keys())}: ")
            if input_mesa in local_mesas:
                ocupar_mesa(input_mesa, input_horario)
                input_personas = input("Ingresa la cantidad de personas para la reserva: ")
                if input_personas.isdigit() and int(input_personas) > 0 and int(input_personas) <= max(local_mesas.values()):
                    for mesa, capacidad in local_mesas.items():
                        if int(input_personas) <= capacidad:
                            ocupar_mesa(mesa, input_horario)
                            print(f"Reserva realizada para {input_personas} personas en {mesa} a las {input_horario}.")
                            break
                else:
                    print("Por favor, ingresa un número válido de personas.")
                    continue
            else: 
                print("Por favor, elige una mesa válida.")
        else:
            print("Por favor, elige un horario válido.")
    else:
        print("Por favor, elige una franja horaria válida.")
    