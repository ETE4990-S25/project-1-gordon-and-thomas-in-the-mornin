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


def move_Direction(direction, distance):
    if direction == "N":
        postion[0] += distance
    elif direction == "S":
        postion[0] -= distance
    elif direction == "E":
        postion[1] += distance
    elif direction == "W":
        postion[1] -= distance
    else:
        print("Invalid direction")

def go_Home():
    postion[0] = 0
    postion[1] = 0
    print("You are home")

def get_postion_Radius():
    return math.sqrt(postion[0]**2 + postion[1]**2)

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

# Run the intro screen


intro_screen() 




    