from items import ItemManager
from backpack import Backpack

iM = ItemManager('items.json')


'''
Creates a list of all items that can be crafted in the game
Small db so it can manipulated in the future


Returns:
    list: A list of all items that can be crafted in the game

'''
def crafting_list():


    possible_items = []
    # pulls the lost of possible items in the game
    for item in iM.items:
        name = item.get_item_name()
        print(item.get_item_name())
        item_needed = item.get_item_items_needed()
        item_list = []

        # fixes the list notation for the items needed and converts it to a dict with naeme and count keys
        for needed_item in item_needed:
            found = False
            for i in item_list:
                if i['name'] == needed_item:
                    i['count'] += 1
                    found = True
                    print("inc count for " + i['name'])
                    break
            if not found:
                item_list.append({'name': needed_item, 'count': 1})
                print("adding new item")

        # adds each item to the list of possible items to craft in the game
        possible_items.append({'name': name, 'items_needed': item_list})
    
    print(possible_items)
    return possible_items

def craftable_items(bp):

    print("You can craft the following items:")
    possible_items = []

    # searched through the list of items that can be crafted and checks if the player has the items needed to craft it
    for item in crafting_list():
    
        name = item['name']
        item_needed = item['items_needed']
        
        # compares the items need to craft the item to the items in the players backpack
        for needed_item in item_needed:
            can_craft = False
            try:
                print("looking for" ,needed_item, "name: ", needed_item['name'], " count: ", needed_item["count"],  "\t\t| bp found:", bp.get_item_count(needed_item['name']))
                if (bp.get_item_count(needed_item['name']) > needed_item['count']):
                    can_craft = True

                # IF ANY TIME IT FAILS TO MEET THE REQUIREMENT TO CRAFT THE ITEM IT WILL BREAK OUT OF THE LOOP AND BE FALSE
                else:
                    can_craft = False
                    break
            except TypeError:
                can_craft = False
                break
            
        # adds the item as a possible item to craft if the player has ingredients
        if can_craft:
            # print("items ", bp)
            print("item count ", bp.get_item_count(needed_item['name']))
            print(bp.get_item_count(needed_item['name']) , " and ", needed_item['count'])
            possible_items.append(name)
    
    return(possible_items)

    

def craft_item(bp,item_name):
    # from the list of possible items in the game, it will craft the item if the player has the items needed
    for item in iM.items:

        # matches the item name
        if item.get_item_name() == item_name:
            for item_needed in item.get_item_items_needed():
                if bp.get_item_count(item_needed) == 0:
                    print(f"You do not have enough {item_needed} to craft {item_name}")
                    return
                
            # removes the items needed to craft the item and adds the crafted item to the backpack object=
            for item_needed in item.get_item_items_needed():
                bp.remove_item(item_needed,1)
            bp.add_item(item_name,1)
            print(f"{item_name} crafted")
            return
        


def crafting_menu(bp):
    # nice pretty menu for the player to craft items
    print("You can craft the following items:")
    pos_items = craftable_items(bp)
    
    # print(pos_items) - testing



    # prints the list of items that can be crafted
    print("Which item would you like to craft?")
    for i in range(len(pos_items)):
        print(f"{i+1}) {pos_items[i]}")
    print("Enter '0' to go back")
    choice = input()
    if choice == '0':
        return
    else:
        # instantly craft items thats possible witht the items in the players backpack
        craft_item(bp,pos_items[int(choice)])
        bp.save_backpack()
        return



# TEST TES TES T
if __name__ == "__main__":
    bp = Backpack('back.json')
  
    # crafting_list()


    # craftable_items(bp)
    crafting_menu(bp)




    # TODO: Clean up the print statments
    



