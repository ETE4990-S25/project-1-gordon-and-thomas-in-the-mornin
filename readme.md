# Project 1 - Oooga Booga Farming Simulator
## Description
Here you are the start of civilzation. You have to wander around the lands and look for materials to eventually craft the ultimate weapon to defeat the final boss. Along the way as you craft items you will be able to collect more resources to craft more items. 

## How to use
Run the game by running the main method in the Main class. The game will start and you will be able to play.

``` python
python main.py
```

## Things that the games uses
- Importing
- Classes
  - Polymorphism
  - Dot methods
  -  
- Screen Prompt Handling
- Loops
- Lists
- Dicts
- JSON Manipulation
  - JSON file is used to store the items that can be crafted
  - JSON is also being used to store backpack items
- File Saving
- 

## Game Logic





### Backpack 
- The backpack is used to store the items that you have collected
  - A limit of 5 items in the beginning
  - Can be upgraded to hold more items
- Can be converted to a JSON file to save the items that you have collected
- 

### Items
- Items are stored in a JSON file
- An Item Manager has been made to manage the 
- Items have a name, description, a list of materials needed to craft the item, and a ratity
  - Rarity is used to determine what tier the item is
    - common can be found in the lands
    - uncommon can be crafted from common items
    - rare can be crafted from uncommon or common items 
    - And so on
- Each item has a get method to call 

### Crafting
- Crafting is a finction that cross references two lists to figure out what items the player can craft
  - The algorithm works by first compiling a list of items and their needed ingredients then checking the players backpack with the list to see what are items are craftable
  
### Saving 
- The game saves the items that you have collected in a JSON file
- The name of the object is important

## Team Members
- [Gordon](https://github.com/Gizmofire)
- [Thomas](https://github.com/ThomasHakwins ) 


