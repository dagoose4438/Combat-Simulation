import time
import numbers
import random
import sys
#imports the modules needed for the program


thief_dmg = 5
thief_hp = 10

weak_goblin_dmg = 5
weak_goblin_hp = 15

goblin_dmg = 10
goblin_hp = 25

golem_dmg = 10
golem_hp = 50

dragon_dmg = 25
dragon_hp = 250

monster_num = 1
enemy_health = 0
enemy_dmg = 0
health = 0
damage = 0
move = 0
moves = []
#initiates and sets all the variables and lists for the program


def invalid():
    print("Please enter a valid input")
#tells user to enter a valid input when called

def list_moves():
    global move
    print("Listing moves...")
    time.sleep(1)
    for items in moves:
        print(moves[move])
        move += 1
        time.sleep(0.05)
    sys.exit(0)

def enemy_turn():
    global health
    global enemy_dmg
    global monster_type_1
    print("Enemy turn...")
    time.sleep(2)
    health -= enemy_dmg
    print(f"{monster_type_1} hit you for {enemy_dmg} damage!")
    time.sleep(1)
    if health < 0:
        health = 0
        print("You have 0 health left")
        time.sleep(1)
        battle_end()
    else:
        print(f"You have {health} health left")
#code for the enemies turn during fight

def battle_end():
    if health <= 0:
        print(f"You have died to the {monster_type_1}!")
        time.sleep(1)
        print(f"{monster_type_1} had {enemy_health} health left")
        time.sleep(1)
        menu_input = input("Press enter to see the moves you did during the game or restart the program to try again!")
        list_moves()
    elif enemy_health <= 0:
        print(f"You have slain the {monster_type_1}!")
        time.sleep(1)
        print(f"You had {health} health left")
        time.sleep(1)
        menu_input = input("Press enter to see the moves you did during the game or restart the program to play again!")
        list_moves()
#code to end the battle if users health or enemies health is at 0

def start_battle(monster):
    global monster_type_1
    global enemy_health
    global enemy_dmg
    global chosen_class_1
    global chosen_class
    global damage
    global health
    print(f"{monster} has {enemy_health} health left")
    time.sleep(1)
    print(f"You have {health} health left")
    while health > 0 or enemy_health > 0:
        time.sleep(1)
        player_move = input(f"What would you like to do?\n1. Damage {monster} for {damage} damage\n2. Heal for 50 health\n")
        if player_move == "1":
            enemy_health -= damage
            print(f"You hit {monster} for {damage} damage!")
            time.sleep(1)
            if enemy_health <= 0:
                enemy_health = 0
                print(f"{monster} has 0 health left")
                moves.append("Attack")
                time.sleep(1)
                battle_end()
            else:
                print(f"{monster} has {enemy_health} health left")
                moves.append("Attack")
                time.sleep(1)
                enemy_turn()
        elif player_move == "2":
            health += 50
            if chosen_class == 1:
                if health > 150:
                    health = 150
            elif chosen_class == 2:
                if health > 100:
                    health = 100
            print(f"You have healed and are now at {health} health")
            moves.append("Heal")
            time.sleep(1)
            enemy_turn()
        else:
            invalid()
            time.sleep(1)
            start_battle()
    battle_end()

def ask_monster_type():
    global monster_type
    global monster_type_1
    global monster_num
    global enemy_health
    global enemy_dmg
    monster_type = input("What monster would you like to fight? You can only choose one type:\n1. Thief (5 DMG, 10 HP)\n2. Weak Goblin (5 DMG, 15 HP)\n3. Goblin (10 DMG, 25 HP)\n4. Golem (10 DMG, 50 HP)\n5. Dragon (25 DMG, 250 HP)\n")
    if monster_type == "1" or monster_type == "2" or monster_type == "3" or monster_type == "4" or monster_type == "5":
        if monster_type == "1":
            monster_type_1 = "Thief"
            monster_type = 1
            enemy_health = thief_hp
            enemy_dmg = thief_dmg
        elif monster_type == "2":
            monster_type_1 = "Weak Goblin"
            monster_type = 2
            enemy_health = weak_goblin_hp
            enemy_dmg = weak_goblin_dmg
        elif monster_type == "3":
            monster_type_1 = "Goblin"
            monster_type = 3
            enemy_health = goblin_hp
            enemy_dmg = goblin_dmg
        elif monster_type == "4":
            monster_type_1 = "Golem"
            monster_type = 4
            enemy_health = golem_hp
            enemy_dmg = golem_dmg
        elif monster_type == "5":
            monster_type_1 = "Dragon"
            monster_type = 5
            enemy_health = dragon_hp
            enemy_dmg = dragon_dmg
        #checks what monster was selected and assigns the appropriate variables
        print(f"Fighting as: {chosen_class_1}")
        time.sleep(1)
        print(f"Fighting against: {monster_num} {monster_type_1}(s)")
        time.sleep(1)
        input("Press enter when you are ready\n")
        print("Starting battle...")
        time.sleep(3)
        start_battle(monster_type_1)
    elif monster_type == "back":
        print("Already confirmed class selection!")
        time.sleep(1)
        ask_monster_type()
    else:
        invalid()
        time.sleep(1)
        ask_monster_type()
#asks the user what monster they want to fight

def change_stats(x):
    global chosen_class
    global chosen_class_1
    global damage
    global health
    if x == 1:
        print("Now fighting as Berserker")
        chosen_class = 1
        chosen_class_1 = "Berserker"
        damage = 20
        health = 150
        ask_monster_type()
    elif x == 2:
        print("Now fighting as Archer")
        chosen_class = 2
        chosen_class_1 = "Archer"
        damage = 30
        health = 100
        ask_monster_type()
#changes the stats of the player depending on the class they selected
        
def start_game():
    class_select = input("What class would you like to play? (Use numbers to navigate)\n1. Berserker\n2. Archer\n")
    if class_select == "1":
        confirm = input("You have selected the Berserker class. Confirm?\n1. Confirm\n2. Go back\n")
        if confirm == "1":
            print("Setting your class to Berserker...")
            time.sleep(2)
            change_stats(1)
        elif confirm == "2":
            print("Going back to class selection...")
            time.sleep(1)
            start_game()
        else:
            invalid()
            time.sleep(1)
            start_game()
    elif class_select == "2":
        confirm = input("You have selected the Archer class. Confirm?\n1. Confirm\n2. Go back\n")
        if confirm == "1":
            print("Setting your class to Archer...")
            time.sleep(3)
            change_stats(2)
        elif confirm == "2":
            print("Going back to class selection...")
            time.sleep(1)
            start_game()
        else:
            invalid()
            time.sleep(1)
            start_game()
    else:
        invalid()
        time.sleep(1)
        start_game()
#asks the user what class they want to play

def startup_info():    
    menu_input = input("To view information on how to play the game, type 'tutorial'\nTo view information on the different classes, type 'class'\n")
    if menu_input == "tutorial":
        print("You will be able to select your class.\nThen you will be able to select the monster you wish to fight.\nYou will then take turns between yourself and the monster damaging eachother, until either you or the monster die.\nDuring your turn, you will have the option to either heal for 50 health or damage the enemy.")
        time.sleep(1)
        startup()
    elif menu_input == "class":
        print("Berserker: You are given a sword, as well as increased health.\nArcher: You are given a bow, as well as increased damage.")
        time.sleep(1)
        startup()
    else:
        invalid()
        time.sleep(1)
        startup_info()
#code for the info section of the main menu

def startup():
    menu_input = input("To start, type 'start'\nFor more information on how to play, type 'info'\n")
    if menu_input == "start":
        start_game()
    elif menu_input == "info":
        startup_info()
    else:
        invalid()
        time.sleep(1)
        startup()
#asks the user whether they would like to start the program or view the info
        
print("Welcome to Combat Simulation!")
#welcome screen
time.sleep(1)
startup()