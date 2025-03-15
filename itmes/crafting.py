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
    for item in iM.items:
        name = item.get_item_name()
        print(item.get_item_name())
        item_needed = item.get_item_items_needed()
        item_list = []
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

        possible_items.append({'name': name, 'items_needed': item_list})
    
    print(possible_items)
    return possible_items

def craftable_items(bp):
    print("You can craft the following items:")
    possible_items = []
    for item in crafting_list():
        

        name = item['name']
        item_needed = item['items_needed']
        
        for needed_item in item_needed:
            can_craft = False
            try:
                print("looking for" ,needed_item, "name: ", needed_item['name'], " count: ", needed_item["count"],  "\t\t| bp found:", bp.get_item_count(needed_item['name']))
                if (bp.get_item_count(needed_item['name']) > needed_item['count']):
                    can_craft = True
                else:
                    can_craft = False
                    break
            except TypeError:
                can_craft = False
                break
            

        if can_craft:
            # print("items ", bp)
            print("item count ", bp.get_item_count(needed_item['name']))
            print(bp.get_item_count(needed_item['name']) , " and ", needed_item['count'])
            possible_items.append(name)
    
    print(possible_items)

    

def craft_item(self,bp,item_name):
    for item in iM.items:
        if item.get_item_name() == item_name:
            for item_needed in item.get_item_items_needed():
                if bp.get_item_count(item_needed) == 0:
                    print(f"You do not have enough {item_needed} to craft {item_name}")
                    return
            for item_needed in item.get_item_items_needed():
                bp.remove_item(item_needed,1)
            bp.add_item(item_name,1)
            print(f"{item_name} crafted")
            return

if __name__ == "__main__":
    bp = Backpack('back.json')
  
    # crafting_list()


    craftable_items(bp)
    



