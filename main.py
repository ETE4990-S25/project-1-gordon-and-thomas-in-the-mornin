
from itmes.backpack import Backpack
from itmes.items import ItemManager

bp = Backpack("back.json")


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
            
            
            # fighting()
        elif choice == "2":
            print("\n[Opening your backpack...]\n")
            # Calls backpack function
            bp.toTable




            
        elif choice == "3":
            print("\n[Crafting items...]\n")
            # Call crafting function
        elif choice == "4":
            print("\n[Game saved. Exiting...]\n")
            break  # Exit the loop and save progress
        else:
            print("\nInvalid choice. Please select a number between 1 and 4.")


