from .items import ItemManager
from .backpack import Backpack

iM = ItemManager('.\items_and_backpack\items.json')

def crafting_list():
    """
    Creates a list of all items that can be crafted in the game.
    Small db so it can be manipulated in the future.

    Returns:
        list: A list of all items that can be crafted in the game.
    """
    possible_items = []
    for item in iM.items:
        name = item.get_item_name()
        item_needed = item.get_item_items_needed()
        item_list = []

        for needed_item in item_needed:
            found = False
            for i in item_list:
                if i['name'] == needed_item:
                    i['count'] += 1
                    found = True
                    break
            if not found:
                item_list.append({'name': needed_item, 'count': 1})

        possible_items.append({'name': name, 'items_needed': item_list})

    return possible_items

def craftable_items(bp):
    """
    Determines which items can be crafted based on the items in the backpack.

    Args:
        bp (Backpack): The player's backpack.

    Returns:
        list: A list of craftable item names.
    """
    possible_items = []
    for item in crafting_list():
        name = item['name']
        items_needed = item['items_needed']
        can_craft = True

        for needed_item in items_needed:
            try:
                if bp.get_item_count(needed_item['name']) < needed_item['count']:
                    can_craft = False
                    break
            except TypeError:
                can_craft = False
                break

        if can_craft:
            possible_items.append(name)

    return possible_items

def craft_item(bp, item_name):
    """
    Crafts an item if the player has enough resources.

    Args:
        bp (Backpack): The player's backpack.
        item_name (str): The name of the item to craft.
    """
    for item in iM.items:
        if item.get_item_name() == item_name:
            for item_needed in item.get_item_items_needed():
                if bp.get_item_count(item_needed) == 0:
                    print(f"You do not have enough {item_needed} to craft {item_name}")
                    return
            for item_needed in item.get_item_items_needed():
                bp.remove_item(item_needed, 1)
            bp.add_item(item_name, 1)
            print(f"{item_name} crafted")
            return

def crafting_menu(bp):
    """
    Displays the crafting menu and allows the player to craft items.

    Args:
        bp (Backpack): The player's backpack.
    """
    print("You can craft the following items:")
    pos_items = craftable_items(bp)
    
    for i, item in enumerate(pos_items, start=1):
        print(f"{i}) {item}")
    print("Enter '0' to go back")
    
    choice = input()
    if choice == '0':
        return
    else:
        craft_item(bp, pos_items[int(choice) - 1])
        bp.save_backpack()

if __name__ == "__main__":
    bp = Backpack('back.json')
    crafting_menu(bp)




