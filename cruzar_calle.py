#Problema 1 — Cruzar la calle de forma segura
#Describí, paso a paso, el proceso completo para cruzar una calle con semáforo de forma segura,
#desde que llegás a la esquina hasta que estás del otro lado.
#   Variables: Persona, Semaforo
#   Funciones; Calle

persona = input("Ingrese su nombre: ")
semaforo = input("Ingrese el color del semáforo(rojo, amarillo, verde) :")

def cruzar_calle(semaforo):
    if semaforo == "verde":
        return f"{persona} puede cruzar la calle de forma segura."
    elif semaforo == "amarillo":
        return f"{persona} debe esperar, el semáforo está en amarillo."
    elif semaforo == "rojo":
        return f"{persona} debe esperar, el semáforo está en rojo."

print(cruzar_calle(semaforo))