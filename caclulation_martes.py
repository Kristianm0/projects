#Calculado tu peso en Marte

#Mostrar en pantalla: “¿Quieres saber tu peso en Marte?”

print("Hola, espero que estes bien 🙂.")
print("¿Quieres saber cuantos pesas en Martes?")

# Mostrar dos opciones: “Si” “No”

print("Elige una opcion")
print("""
1) Si 
2) No
""")

#Poner condiciones: 
# No:
# Apagar el programa.
# Si:
#  Pedir datos: “¿Cuánto pesas en la tierra?”

user = input(">>> ")

if user == "1":
    print("¿Cuánto pesas en la tierra?")
    #  Poner en una variable el peso del usuario.
    peso = float(input(">>> "))

    #  Calcular el peso del usuario: Peso del usuario * 3,711 m/s^2 gravedad de Marte / 9,81/s^2 gravedad en la tierra.
    
    peso = round(peso * 3.711/9.11)

    print ("Tu peso en Marte es " + str(peso) + " kg.")
    print("Gracias por jugar ⭐")
    
    # #  Apagar el programa.

if user == "2":
    print("Off")

else: 
    print("Gracias por jugar ⭐")
