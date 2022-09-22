
#juego pokemon 
# Poner a que vuelva a elegir otro pokemon si ya es que elige los mismos


import random


#Ciclo while
##Definimos un ciclo while para que el juego se repita y no pare.
u = "u"
while u == 1 or "1 ": 
        inicio = """Hi, this is the game most similar to Pokemon
        Do you want to play
        1. No 
        2. Yes"""
        print(inicio)

        
        #Ya definimos el menu para que el usuario le de le de inicio al juego o no. 
        # Pero en verda el uno va a ejecutar ya para que se elige la siguiente accion.

## Creamos las carateristicas para crear los objetos de los pokemones.
        user = int(input(">>> "))
        
        if user == 1:
                print("Ok, the game is finished. ")
                break
        if user == 2:
                class Pokemon:
                        def __init__(self, name, attack, life, type):
                                self.name = name 
                                self.attack = attack
                                self.life = life 
                                self.type = type
        #Definimos los valores que van a tener los pokemoes. 

        Amokrus = Pokemon("Amokrus", 30, 150, "Water")
        Rodosh = Pokemon("Rodosh", 20, 90, "Fire")
        Katalish = Pokemon ("Katalish", 70, 65, "Magic")
        tuqueboo = Pokemon ("Tuqueboo", 9, 40, "Metal")

        # Creamos los pokemones y le damos a cada uno un nombre, ataque, vida y tipo.


        ## the menu of the pokemons infomation
        menu_a = """Write the number of the pokemon to know more about it, 
                and write 0 to get off of the menu

                ---About---
                0. To get off 📌.
                11. Menu about elements 💧🔥🪄🔩.
                111. View this menu.

                ---Pokemons---
                1. Amokrus 🐕.
                2. Rodosh 😺.
                3. Katalish 😾.
                4. Tuqueboo 🦎.
                """
        print(menu_a)

        
        ## Creamos un menu con el ciclo while para los pokemones, el ciclo while para que el usuario 
        #pueda saber sobre todos lo pokemones hasta cuando el decida salirse del menu.
        LIMITE = 2
        potencia_2 = 1 
        while potencia_2 < LIMITE:
                
                user_about = int(input(">>> "))

                if user_about == 111:
                        print(menu_a)
                
                #Creamos el menu con la informacion de los elementos y su funcionamiento.
                if user_about == 11:
                        print("""
                        Here is the table of the elements the pokemons:
                        💧 Water increase your attack 80% and your life 60% vs pokemon of the fire.
                        🔥 Fire increase your attack 40% and your life 10% vs pokemons magic.
                        🪄  Magic increase your attack 60% wiht pokemons that isnt maigcs.
                        🔩 Metal increase your life 500% vs pokemons magic, and water.
                        
                        """)
                
                # Creamos el menu los pokemones con sus valores.
                if user_about == 1:
                        a_amokrus = print(f"""
                1. 🐕 Amokrus: 
                💥 The attack is bitus with {Amokrus.attack} of the power.
                ❤️ The life is {Amokrus.life}.
                💧 Type: {Amokrus.type}.
                """)

                if user_about == 2: 
                        a_rodosh = print(f"""
                2. 😺 Rodosh: 
                💥 The attack is clawer with {Rodosh.attack} of the power.
                ❤️ The life is {Rodosh.life}.
                🔥 The type: {Rodosh.type}.

                """)

                if user_about == 3: 
                        a_Katalish = print(f"""
                3. 😾 Katalish:
                💥 The attack is clawer with {Katalish.attack} of the power.
                ❤️ The life is {Katalish.life}.
                🪄 The type: {Katalish.type}
                """)
                if user_about == 4: 
                        a_tuqueboo = print(f"""
                4. 🦎 Tuqueboo:
                💥 The attack is clawer with {tuqueboo.attack} of the power.
                ❤️ The life is {tuqueboo.life}.
                🔩 The type: {tuqueboo.type}
                """)
                
                #Creamos el break para que el usuario se pueda salir del menu cuando los decida.
                if user_about == 0:
                        break

                #Creamos un mensaje para guiar al usuario a elegir los pokemones o para salir.       
                else:
                        print("""
                _____________________________________
                - Get off of the menu, write 0.
                - See the menu again, write 111.
                """)
                                


        ## Menu para eligir pokemones
        # Mostramos un menu indicandole al usuario que eliga un pokemon.
        # Creamos un while para que eliga un pokemon si o si

        pokemon_a = 0
        pokemon_b = 0
        cho_po_menu = """
                Now you have to choose two pokemons to the battle, 
                choose the pokemon by the number

                1. Amokrus 🐕.
                2. Rodosh 😺.
                3. Katalish 😾.
                4. Tuqueboo 🦎.
                        """                

        while pokemon_a != 1 or 2 or 3 or 4:                 
                print(cho_po_menu)
                # Creamos las condiciones para el pokemon a indicar que si el usuario elige un numero sea un pokemone en especifico.
                pokemon_a = int(input("Pokemon A: "))
                if pokemon_a == 1:
                        pokemon_a = Amokrus
                        break
                elif pokemon_a == 2:
                        pokemon_a = Rodosh
                        break
                elif pokemon_a == 3:
                        pokemon_a = Katalish
                        break
                elif pokemon_a == 4:
                        pokemon_a = tuqueboo
                        break
                #Creamos una condicion extra para eliga uno de la lista.
                elif pokemon_a != 1 or 2 or 3 or 4:
                        print("🤔 no hay ese pokeom. ***Error***")
                        print("Elege de nuevo")
                
        while pokemon_b != 1 or 2 or 3 or 4: 
                print(cho_po_menu)
        # Creamos lo mismo pero para el pokemon b
                pokemon_b = int(input("Pokemon B: "))
                if pokemon_b == 1:
                        pokemon_b = Amokrus
                        break
                elif pokemon_b == 2:
                        pokemon_b = Rodosh
                        break
                elif pokemon_b == 3:
                        pokemon_b = Katalish
                        break
                elif pokemon_b == 4:
                        pokemon_b = tuqueboo
                        break
                elif pokemon_b != 1 or 2 or 3 or 4:
                        print("🤔 ***Error*** There is not that pokemon")
                        print("Choose again")

        #condicion para decirle que no tenemos ese pokemon.
        
        # Creamos una condicion para que no pueda elegir a el mismo pokemon para luchar.
                        
        if pokemon_a == pokemon_b or pokemon_b == pokemon_a:
                print("***Error***")
                print("😤 You can not choose the same pokemon.")
                print("Star again")
                break 

## Creamos los niveles y ventajas dependiendo de que tipo de pokemon se enfrenta cada uno.
        print(f"The battle going to be >> {pokemon_a.name} << vs >> {pokemon_b.name} <<")
        # 💧 Water increase your attack 80% and your life 60% vs pokemon of the fire.
        if pokemon_a.type == "Water" and pokemon_b.type == "Fire":
                #porcentaje de atauqe
                pokemon_a_type_attack = pokemon_a.attack*80/100 
                #se le agrega el porcentaje de ataque
                pokemon_a.attack += pokemon_a_type_attack
                #porcentaje de vida
                pokemon_a_type_life = pokemon_a.life*60/100
                #se le agrega el porcentaje de vida
                pokemon_a.life += pokemon_a_type_life
                print(f"""
        {pokemon_a.name}is Water so, increase your attack 80% and your 
        life 60% vs pokemon of the fire. """)
        
        if pokemon_a.type == "Fire" and pokemon_b.type == "Water":
                #Porcentaje de atauqe
                pokemon_b_type_attack = pokemon_b.attack*80/100
                #Se le agrega el porcentaje de ataque
                pokemon_b.attack += pokemon_b_type_attack
                # porcentaje de vida
                pokemon_b_type_life = pokemon_b.life*60/100
                #se le agrega el porcentaje de vida
                pokemon_b.life += pokemon_b_type_life
                print(f"""
        {pokemon_b.name}is Water so, increase your attack 80% and your 
        life 60% vs pokemon of the fire. """)
        

        #🔥 Fire increase your attack 40% and your life 10% vs pokemons magic.
        if pokemon_a.type == "Fire" and pokemon_b.type == "Magic":
                #porcentaje de atauqe
                pokemon_a_type_attack = pokemon_a.attack*40/100 
                #se le agrega el porcentaje de ataque
                pokemon_a.attack += pokemon_a_type_attack
                #porcentaje de vida
                pokemon_a_type_life = pokemon_a.life*10/100
                #se le agrega el porcentaje de vida
                pokemon_a.life += pokemon_a_type_life
                print(f"""
        {pokemon_a.name} is fire so, increase your attack 40% and your 
        life 10% vs pokemons magic. """)
        
        if pokemon_b.type == "Fire" and pokemon_a.type == "Magic":
                #porcentaje de atauqe
                pokemon_b_type_attack = pokemon_b.attack*40/100 
                #se le agrega el porcentaje de ataque
                pokemon_b.attack += pokemon_b_type_attack
                #porcentaje de vida
                pokemon_b_type_life = pokemon_b.life*10/100
                #se le agrega el porcentaje de vida
                pokemon_b.life += pokemon_b_type_life
                print(f"""
                {pokemon_b.name} is fire so, increase your attack 40% and your 
                life 10% vs pokemons magic. """)
        
        #🪄  Magic increase your attack 60% wiht pokemons that isnt maigcs.
        if pokemon_a.type == "Magic" and pokemon_b.type != "Magic":
                #porcentaje de atauqe
                pokemon_a_type_attack = pokemon_a.attack*60/100 
                #se le agrega el porcentaje de ataque
                pokemon_a.attack += pokemon_a_type_attack
                print(f"""
        {pokemon_a.name} is magic so, increase your attack 
        60% wiht pokemons that isnt maigcs.
        """)

        if pokemon_b.type == "Magic" and pokemon_a.type != "Magic":
                #porcentaje de atauqe
                pokemon_b_type_attack = pokemon_b.attack*60/100 
                #se le agrega el porcentaje de ataque
                pokemon_b.attack += pokemon_b_type_attack
                print(f"""
        {pokemon_b.name} is magic so, increase your attack 
        60% wiht pokemons that isnt maigcs.
        """)


        #🔩 Steal increase your life 500% vs pokemons magic, and water.
        if pokemon_a.type == "Metal" and pokemon_b.type == "Water":
                pokemon_a_type_life = pokemon_a.life*500/100
                #se le agrega el porcentaje de vida
                pokemon_a.life += pokemon_a_type_life
                print(f"""
        {pokemon_a.name} is steal so, increase your life 500% vs 
        pokemons magic, and water.
        """)

        if pokemon_b.type == "Metal" and pokemon_a.type == "Water":
                pokemon_b_type_life = pokemon_b.life*500/100
                #se le agrega el porcentaje de vida
                pokemon_b.life += pokemon_b_type_life
                print(f"""
        {pokemon_b.name} is steal so, increase your life 500% vs 
        pokemons magic, and water.
        """)


        #Creamos el turno para que empize un pokemon primero.  
        if pokemon_a != pokemon_b:        
                print("The firts number is the pokemon to play firts")
                turn = random.randint(1, 2) 
                print(turn)
                rounda = "⬇️"

        #Ponemos el ciclo para que los pokemones se ataquen entre si hasta que uno muera o su vida llegue a cero.
        while pokemon_a.life > 0 or pokemon_b.life > 0:
                if turn == 1:
                        print(rounda)
                        print(f"{pokemon_a.name} attack to {pokemon_b.name} with {pokemon_a.attack} 💥") 
                        pokemon_b.life = pokemon_b.life - pokemon_a.attack
                        turn = 2
                        print(f"The life of {pokemon_b.name} is {pokemon_b.life} ❤️")
                        print("")

                if turn == 2:
                        print(rounda)
                        print(f"{pokemon_b.name} attack to {pokemon_a.name} with {pokemon_b.attack} 💥")
                        pokemon_a.life = pokemon_a.life - pokemon_b.attack
                        turn = 1
                        print(f"The life of {pokemon_a.name} is {pokemon_a.life} ❤️")
                        print("")

                #Vemos quien perdio o gano con una condicion.
                # Si la vida del poke b es menor a cero, es que esta muerto. Y el poke a gano. 
                if pokemon_b.life <= 0:
                        print(f"{pokemon_a.name} won this battle")
                        print(f"{pokemon_b.name} lost this battle")
                        print("The battle is finished")
                        print("The game is ended ⭐⭐⭐")
                        break

                elif pokemon_a.life <= 0:
                        print(f"{pokemon_b.name} won this battle")
                        print(f"{pokemon_a.name} lost this battle")
                        print("The battle is finished")
                        print("The game is ended ⭐⭐⭐")
                        break

        
