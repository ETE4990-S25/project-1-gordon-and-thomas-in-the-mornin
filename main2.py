import random
import math
#create map of a circle with radius of 100
#create postion at any point from the center of the circl
#Create a home at 0,0 
#create a angle finder where loot changes based on angle
#create movement system
#Create a go home function
#Create a distance finder
#Create a loot finder
#create a crafting system
#Create a inventory system
#Create a health system


map_Radius = 100

map_Area = 3.14 * map_Radius * map_Radius

postion = [0,0]

def get_postion():
    return postion

radius = math.sqrt(postion[0] * postion[0] + postion[1] * postion[1])
#loot based on angles so this finds the angle you are at so we know what loot to gove
def get_Angle():
    angle = 0
    if postion[0] == 0:
        if postion[1] > 0:
            angle = 90
        else:
            angle = 270
    else:
        angle = math.degrees(math.atan(postion[1]/postion[0]))
    return angle

#basic function for moving around the map and finding enemies
def move_Direction(direction, distance):
    while True:
        print("\nChoose a direction to walk")
        print("N) Walk North")
        print("S) Walk South")
        print("E) Walk East")
        print("W) Walk West")
        print("GH) Go Home")

        choice = input("Select an option (N,S,E,W,GH): ")

        if direction == "N":
         postion[0] += distance
        elif direction == "S":
            postion[0] -= distance
        elif direction == "E":
            postion[1] += distance
        elif direction == "W":
            postion[1] -= distance
        elif direction == "GH":
            go_Home()
        else:
            print("Invalid direction")
        random.randint(1,6)
        if random.randint(1,6) == 1:
            print("You were attacked by a wild animal")
        fighting()
    
    
#takes the player back to the home base
def go_Home():
    postion[0] = 0
    postion[1] = 0
    print("You are home")
    print("what would you like to do?")
    print("1) Explore")
    print("2) Go back to intro screen")
    choice = input("Select an option (1-2): ")
    if choice == "1":
        move_Direction()
    elif choice == "2":
        intro_screen()
    else:
        print("Invalid choice")

#finds the distance from the home base for loot based functions
def get_postion_Radius():
    return math.sqrt(postion[0]**2 + postion[1]**2)


#searches for loot from falled enemies and/or ground
def search_Loot():
    angle = get_Angle()
    distance = get_postion_Radius()
#    TODO: Gordon - I will change this to work with new item/backpack system
    
    if distance < 10 and angle > 0 and angle < 45:
        low_Loot_number_generator = random.randint(1, 30)
        if low_Loot_number_generator == 1:
            print("You found a stick")
        elif low_Loot_number_generator == 2:
            print("You found a rock")
        elif low_Loot_number_generator == 3:
            print("You found nothing")
        elif low_Loot_number_generator == 4:
            print("You found a feather")
        elif low_Loot_number_generator == 5:
            print("You found a twig")
        elif low_Loot_number_generator == 6:
            print("You found a shell")
        elif low_Loot_number_generator == 7:
            print("You found a bone")
        elif low_Loot_number_generator == 8:
            print("You found a nothing")
        elif low_Loot_number_generator == 9:
            print("You found a nothing")
        elif low_Loot_number_generator == 10:
            print("You found a nothing")
        else:
            print("You found nothing")

        ##### Gives item here#########

#intor screen for the game
def intro_screen():
    while True:
        print("\n--- Welcome to the Adventure Game ---")
        print("1) Explore")
        print("2) Examine Backpack")
        print("3) Craft Items")
        print("4) Exit and Save")
        
        choice = input("Select an option (1-4): ")

        if choice == "1":
            print("\n[Exploring the world...]\n")
            go_Home()
            # Call your explore function here
        elif choice == "2":
            print("\n[Opening your backpack...]\n")
            # Call backpack function
        elif choice == "3":
            print("\n[Crafting items...]\n")
            # Call crafting function
        elif choice == "4":
            print("\n[Game saved. Exiting...]\n")
            break  # Exit the loop and save progress
        else:
            print("\nInvalid choice. Please select a number between 1 and 4.")
 

#dice roll for fighting
def dice_Roll ():
    sum = 0
    for x in range (5):
        sum = sum + random.randint(1,6)
    return sum

#uses dice_roll as a fighting mechanica agaisnt enenmy enemy needs to be bested by 1/2,2/3 etc with higher level enemies
# def fighting():
#     while True:
#         wins_needed

#         wins = []

#         losses = []

#         games_Played = []

#         computer_Guess = dice_Roll()

#         print (computer_Guess)

#         user_Guess = int(input ("Enter a guess for the sum of 5 dice if youre within 2 numbers you win"))

#         print (computer_Guess)

#         #if computer_Guess - 2 <= user_Guess <=  computer_Guess + 2:
#             #print(f" You won! youre guess was {user_Guess} the total sum was {computer_Guess}")
#         if computer_Guess == user_Guess:
#             print (" wow lucky guess you got it exactly right!")
#             wins.append(1)
#             games_Played.append(1)

#         elif computer_Guess - 2 <= user_Guess <=  computer_Guess + 2:
#             print(f" You won! youre guess was {user_Guess} the total sum was {computer_Guess}")
#             wins.append(1)
#             games_Played.append(1)

#         else:
#             print(" you lost loser :p ")
#             losses.append(1)

#new fighting function that uses classes to determine which enemy to fight and how many wins are needed to beat
def fighting(which_Enemy_):
    enemy = which_Enemy_()
    wins_needed = enemy.wins_to_beat
    wins = 0
    
    print(f"You encountered a {enemy.name} (Level {enemy.level})!")
    print(f"You need {wins_needed} wins to defeat it.")
    
    while wins < wins_needed:
        computer_roll = dice_Roll()
        print(f"Enemy rolled: {computer_roll}")
        
        try:
            user_guess = int(input("Enter your guess for the sum of 5 dice: "))
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
            
        print(f"Wins: {wins}/{wins_needed}")
    
    print(f"You defeated the {enemy.name}!")


#function to determine which enemy to fight based on distance from home
def which_Enemy_(distance):
    if distance < 10:
        return low_level_enemy(distance)
    elif distance < 20:
        return mid_level_enemy(distance)
    else:
        return high_level_enemy(distance)




#main class for enemies name,level, and wins to beat should be based on distance from home. so the further you are from home the more wins you need to beat the enemy
class enemy:
    def __init__(self, name, level,wins_to_beat):
        self.name = name
        self.level = level
        self.wins_to_beat = wins_to_beat
        

    def __str__(self):
        return f"{self.name} (Level {self.level})"
    
#low level enemies only need 1 win to beat them
class low_level_enemy(enemy):

    enemy_names = ["Cave Rat", "Wolf", "Wild Boar", "Angry Giant Sloth"]
    def __init__(self,distance):
        self.name = random.choice(self.enemy_names)
        self.level = 1
        self.wins_to_beat = 1
    
#mid level enemies need 3 wins to beat them
class mid_level_enemy(enemy):
    enemy_names = ["Hyena", "Raptor", "Rival Caveman", "Sabertooth Tiger"]
    def __init__(self,distance):
        self.name = random.choice(self.enemy_names)
        self.level = 1
        self.wins_to_beat = 3
    
#high level enemies need 5 wins to beat them
class high_level_enemy(enemy):
    enemy_names = ["Wooly mammoth", "Cave Bear", "Giant Eagle", "Mega Cave Rat"]
    def __init__(self,distance):
        self.name = random.choice(self.enemy_names)
        self.level = 1
        self.wins_to_beat = 5


    