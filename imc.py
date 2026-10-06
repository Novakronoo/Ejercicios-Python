#1. Calculadora de IMC
#Pedí (con input()) peso en kg y altura en metros, calculá el IMC (peso / altura**2)
# e imprimí un mensaje según el resultado: "bajo peso" (<18.5), "normal" (18.5-24.9), "sobrepeso" (>25).

p = float(input("Ingrese su peso: "))
a = float(input("Ingrese su altura: "))

imc = p / a ** 2

def resultado(imc):
    if imc < 18.5:
        return "bajo peso"
    elif 18.5 <= imc <= 24.9:
        return "normal"
    else:
        return "sobrepeso"

print("Su resultado es: ", resultado(imc))
