import random
import math
from items_and_backpack.crafting import crafting_menu
from items_and_backpack.backpack import Backpack
import json

# Create map of a circle with radius of 100
# Create position at any point from the center of the circle
# Create a home at 0,0 
# Create an angle finder where loot changes based on angle
# Create movement system
# Create a go home function
# Create a distance finder
# Create a loot finder
# Create a crafting system
# Create an inventory system
# Create a health system
# EMPTY

map_Radius = 100
map_Area = 3.14 * map_Radius * map_Radius
position = [0, 0]

def get_position():
    return position

radius = math.sqrt(position[0] * position[0] + position[1] * position[1])

# Loot based on angles so this finds the angle you are at so we know what loot to give
def get_Angle():
    angle = 0
    if position[0] == 0:
        if position[1] > 0:
            angle = 90
        else:
            angle = 270
    else:
        angle = math.degrees(math.atan(position[1] / position[0]))
    return angle

# Basic function for moving around the map and finding enemies
def move_Direction(bp):
    while True:
        print("\nChoose a direction to walk")
        print("N) Walk North")
        print("S) Walk South")
        print("E) Walk East")
        print("W) Walk West")
        print("GH) Go Home")

        choice = input("Select an option (N,S,E,W,GH): ").lower()

        if choice == "n":
            position[0] += 1
        elif choice == "s":
            position[0] -= 1
        elif choice == "e":
            position[1] += 1
        elif choice == "w":
            position[1] -= 1
        elif choice == "gh":
            go_Home(bp)
        else:
            print("Invalid direction")
        
        if random.randint(1, 6) == 1:
            print("You were attacked by a wild animal")
            fighting(bp)

# Takes the player back to the home base
def go_Home(bp):
    position[0] = 0
    position[1] = 0
    print("You are home")
    print("What would you like to do?")
    print("1) Explore")
    print("2) Go back to main screen")
    choice = input("Select an option (1-2): ")
    if choice == "1":
        move_Direction(bp)
    elif choice == "2":
        intro_screen(bp)
    else:
        print("Invalid choice")

# Finds the distance from the home base for loot-based functions
def get_position_Radius():
    return math.sqrt(position[0]**2 + position[1]**2)

# Searches for loot from fallen enemies and/or ground
def search_Loot(bp):
    angle = get_Angle()
    distance = get_position_Radius()

    # TODO: add different tier loot for later, if have time

    low_Loot_number_generator = random.randint(1, 5)
    amount_of_items = random.randint(1, 3)
    if low_Loot_number_generator == 1:
        (lambda items: print(f"You found {items} {'stick' if items == 1 else 'sticks'}"))(amount_of_items)
        bp.add_item("stick", amount_of_items)
    elif low_Loot_number_generator == 2:
        (lambda items: print(f"You found {items} {'rock' if items == 1 else 'rocks'}"))(amount_of_items)
        bp.add_item("rock", amount_of_items)
    elif low_Loot_number_generator == 3:
        print("You found nothing")
    else:
        print("You found nothing")

# Intro screen for the game
def intro_screen(bp):
    player = Character()  # Create a character instance and choose gender
    play = True
    while play:
        print("\n--- Welcome to the Adventure Game ---")
        print("1) Explore")
        print("2) Examine Backpack")
        print("3) Search Item description")
        print("4) Craft Items")
        print("5) Exit and Save")
        print("10) HARD RESET BACKPACK")
        
        choice = input("Select an option (1-5): ")

        if choice == "1":
            print("\n[Exploring the world...]\n")
            go_Home(bp)
        elif choice == "2":
            print("\n[Opening your backpack...]\n")
            bp.to_table()
        elif choice == "4":
            print("\n[Crafting items...]\n")
            crafting_menu(bp)
        elif choice == "3":
            print("\n[Viewing item description...]\n")
            view_item_description(bp)
        elif choice == "5":
            bp.save_backpack()
            print("\n[Game saved. Exiting...]\n")   
            play = False  # Exit the loop and save progress
            break
       
        elif choice == "10":
            bp.reset_backpack()
            print("\n[Reseting Backpack]\n")
            
        else:
            print("\nInvalid choice. Please select a number between 1 and 5.")

# Function to view item description
def view_item_description(bp):
    item_name = input("Enter the name of the item to view its description: ")
    try:
        description = bp.get_item_description(item_name)
        print(f"Description of {item_name}: {description}")
    except ValueError as e:
        print(e)

# Dice roll for fighting
def dice_Roll():
    total = 0
    for _ in range(5):
        total += random.randint(1, 6)
    return total

# New fighting function that uses classes to determine which enemy to fight and how many wins are needed to beat
def fighting(bp):
    distance = get_position_Radius()
    enemy = which_Enemy_(distance)
    wins_needed = enemy.wins_to_beat
    wins = 0
    
    print(f"\n\n --------------  \n You encountered a {enemy.name} (Level {enemy.level})!")
    print(f"You need {wins_needed} wins to defeat it.")
    
    while wins < wins_needed:
        computer_roll = dice_Roll()

        # Debug
        # print(f"Enemy rolled: {computer_roll}") 
        
        try:
            print("\n --------------  \n")
            user_guess = int(input("Enter your guess for the sum of 5 dice (6-30): "))
        except ValueError:
            print("Invalid input. Enter a number.")
            continue
        
        if computer_roll == user_guess:
            print("Wow! Lucky guess, you got it exactly right!")
            wins += 1
        elif computer_roll - 2 <= user_guess <= computer_roll + 2:
            print(f"You won this round! Your guess was {user_guess}, total sum was {computer_roll}.")
            wins += 1
        else:
            print("You lost this round!")
            
        print(f"Wins to beat: {wins}/{wins_needed}")
        print(f"Reminder: You need {wins_needed} wins to defeat the {enemy.name}")
    
    print(f"You defeated the {enemy.name}!")
    search_Loot(bp)

# Function to determine which enemy to fight based on distance from home
def which_Enemy_(distance):
    if distance < 10:
        return low_level_enemy(distance)
    elif distance < 20:
        return mid_level_enemy(distance)
    else:
        return high_level_enemy(distance)

# Main class for enemies name, level, and wins to beat should be based on distance from home. So the further you are from home the more wins you need to beat the enemy
class enemy:
    def __init__(self, name, level, wins_to_beat):
        self.name = name
        self.level = level
        self.wins_to_beat = wins_to_beat
        
    def __str__(self):
        return f"{self.name} (Level {self.level})"
    
# Low level enemies only need 1 win to beat them
class low_level_enemy(enemy):
    enemy_names = ["Cave Rat", "Wolf", "Wild Boar", "Angry Giant Sloth"]
    def __init__(self, distance):
        self.name = random.choice(self.enemy_names)
        self.level = 1
        self.wins_to_beat = 1
    
# Mid level enemies need 3 wins to beat them
class mid_level_enemy(enemy):
    enemy_names = ["Hyena", "Raptor", "Rival Caveman", "Sabertooth Tiger"]
    def __init__(self, distance):
        self.name = random.choice(self.enemy_names)
        self.level = 1
        self.wins_to_beat = 3
    
# High level enemies need 5 wins to beat them
class high_level_enemy(enemy):
    enemy_names = ["Wooly Mammoth", "Cave Bear", "Giant Eagle", "Mega Cave Rat"]
    def __init__(self, distance):
        self.name = random.choice(self.enemy_names)
        self.level = 1
        self.wins_to_beat = 5

class Character:
    def __init__(self):
        self.gender = self.choose_gender()

    def choose_gender(self):
        while True:
            gender = input("Choose your gender (male/female): ").lower()
            if gender in ["male", "female"]:
                print(f"You have chosen {gender} as your gender.")
                with open("gender.json", "w") as file:
                    json.dump({"Gender": gender}, file)
                return gender
            else:
                print("Invalid input. Please choose 'male' or 'female'.")

        def save_gender_to_file(self, filename="gender.json"):
            with open(filename, "w") as file:
                json.dump({"Gender": self.gender}, file)