import random
base_dmg = 10
defense = 1
mana = 0
enemy_attack = 0
enemy_crit_counter = 0
input("Welcome to RNG sword fights!!!")
input("Instructions:")
input("When askes what you want to do, type 'D' to defend(maybe gear up is a better name) (and sharpen your sword). ")
input("When askes what you want to do, type 'A' to attack (but your sword will become more blunt.)")
input("When askes what you want to do, type 'Q' to gain 1 mana")
input("When askes what you want to do, type 'R'to use 2 mana to use your ability. If you have insufficient mana, you do a normal attack." )
input("Instead of pressing 'R', you could press 'G' to spend 1 mana to heal. If you have insufficient mana, you will defend.")
input("Should you put in an invalid input, we would assume you wanted to defend.")
while True:
    mode = input("Now, choose your difficulty: 'E' for easy, 'M' for medium and 'H' for hard. An invalid input will result in impossible mode.")
    if mode == 'E':
        hp = 150
        enemy_hp = 120
        enemy_base_damage = 1
    elif mode == 'M':
        hp = 100
        enemy_hp = 200
        enemy_base_damage = 3
    elif mode == 'H':
        hp = 75
        enemy_hp = 350
        enemy_base_damage = 4.5
    else:
        hp = 1
        enemy_hp = 10000
        enemy_base_damage = 100
    run = True
    while run == True:
        i = input('Its your turn. Do something!!! ')
        if i == 'D':
            defense *= 2
            if base_dmg <= 15:
                base_dmg += 5
            else:
                base_dmg = 20
        elif i == 'A':
            if random.randint(1,4) == 4:
                enemy_hp -= base_dmg*3
                print(f'''You did a critical attack and did {base_dmg*3} dmg!!!

    The enemy has {enemy_hp} hp left. ''')
            else:
                enemy_hp -= base_dmg
                print(f'''You dealt{base_dmg} dmg. 
    The enemy has {enemy_hp} hp left.''')
            if base_dmg > 1:
                base_dmg -= 1
        elif i == 'Q':
            mana += 1
            print(f"You now have {mana} mana")
        elif i == 'R':
            if mana >= 2:
                mana -= 2
                if random.randint(1,5) == 3:
                    enemy_hp -= base_dmg*11
                    print(f'''You did a critical attack and dealt {base_dmg*11} dmg!!!
    The enemy has {enemy_hp} hp left.''')
                else:
                    enemy_hp -= base_dmg*3
                    print(f'''You dealt {base_dmg*3} dmg.
    The enemy has {enemy_hp} hp left.''')
        elif i == 'G':
            if mana >= 1:
                hp += 15
            else:
                defense *= 2
                base_dmg += 5
        else:
            defense *= 2
            base_dmg += 5
        if enemy_hp <= 0:
            print("YOU WIN!")
            break
        print("Now its the enemy's turn!!!")
        if enemy_attack == 0:
            if not random.randint(1,4) == 4:
                if not enemy_crit_counter >= 5:
                    hp -= enemy_base_damage
                    print(f'''The enemy dealt {enemy_base_damage/defense} damage to you.
    You have {hp}hp left''')
                    enemy_crit_counter += 1
                    enemy_base_damage -= 1
                    defense = 1
                else:
                    hp -= {enemy_base_damage*2.5}/defense
                    print(f'''The enemy did a critical attack and dealt {enemy_base_damage*2.5/defense} damage to you.
    You have {hp}hp left''')
                    enemy_crit_counter = 0
                    enemy_base_damage -=1
                    defense = 1
        if enemy_attack == 1:
            enemy_base_damage += 3
            print(f'''The enemy sharpened his sword!
    He now deals {enemy_base_damage} damage per attack.''')
        if enemy_attack == 2:
            print(f"The enemy is charging up!")
        if enemy_attack == 3:
            enemy_hp += 10
            if not enemy_crit_counter >= 5:
                hp -= enemy_base_damage* 2.5
                print(f'''The enemy healed 10hp and dealt {enemy_base_damage*2.5/defense} damage to you.
    You have {hp} hp left.''')
                defense = 1
            else:
                hp -= enemy_base_damage* 5.5
                print(f'''The enemy did a critical attack and dealt {enemy_base_damage* 5/defense} damage to you
    You have {hp} hp left.''')
                defense = 1
        if hp <= 0:
            print("You lose :(")
            break
        enemy_attack += 1
        if enemy_attack > 3:
            enemy_attack = 0
    #Updates log:
    #v1.1 : set limit to damage increase and 
