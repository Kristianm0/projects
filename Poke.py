#juego pokemon 

#tarea 
#- ciclo while 
# iniciar mas batallas 
# mas pokemones 
# elegirr que pokemon usar 
# no permitir usar el mismo pokemno a los usuarios
# agregar clases a los pokemon, tierra, agua, fuego
# darle a cada clase superiodida ante toda clase, un poke agua es mas fuerte contra uno fuego 
# Que los pokemones esten en otro documento







import random


#Ciclo while


inicio = """Hi, this is the game most similar to Pokemon"
Do you want to play
1. Yes 
2. No"""
print(inicio)
user = int(input(">>> "))



if user == 1:
    class Pokemon:
        def __init__(self, name, attack):
            self.name = name 
            self.attack = attack
            self.life = 100 
        
        def win(self):
            print(f"{self.name} Won this battle")
            print("Good look the next time")

    Amokrus = Pokemon("Amokrus", 30)
    Rodosh = Pokemon("Rodosh", 30)

    Amokrus.life = 150
    Rodosh.life = 150


    print("The battle has been initiated")

    print("About the pokemos:" )
    #Amokrus
    print("1. 🐕 Amokrus: ")
    print(f"💥 The attack is bitus with {Amokrus.attack} of the power") 
    print(f"❤️  The life is {Amokrus.life}")
    print("")

    #Rodosh
    print("2. 😺 Rodosh: ")
    print(f"💥 The attack is clawer with {Rodosh.attack} of the power")
    print(f"❤️  The life is {Rodosh.life}")
    print("")

    print("The firts number is the pokemon to play firts")

    turn = random.randint(1, 2) 
    print(turn)

    while Amokrus.life > 0 and Rodosh.life > 0:
        if turn == 1:
            print(f"😺 Rodosh attack tp {Amokrus.name} with clawer {Rodosh.attack} 💥")
            Amokrus.life = Amokrus.life - Rodosh.attack
            turn = 2
            print(f"🐕 The life of Amokrus is {Amokrus.life} ❤️")
            print("")

        else: 
            print(f"🐕 Amokrus attack to {Rodosh.name} with bitus {Amokrus.attack}💥" )
            Rodosh.life = Rodosh.life - Amokrus.attack 
            turn = 1
            print(f"😺 The life of Rodosh is {Rodosh.life} ❤️")
            print("")

    #Vemos quien perdio o gano.
    if Amokrus.life <= 0:
        Rodosh.win()
        
    else:
        Amokrus.win()
        


if user == 2:
    print("Ok")
