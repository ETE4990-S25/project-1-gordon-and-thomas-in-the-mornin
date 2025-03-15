



# back pack storing format 

# json notation 
# [{
# name: string,
# count: int,
# description: item pointer to a singualr items.json item
# },
# ...
# ]



import json
from items import ItemManager

class Backpack:
    def __init__(self, file_path):
        self.file_path = file_path
        self.items = []
        self.capacity = 5
        self.load_items()

    def load_items(self):
        try:
            with open(self.file_path, 'r') as file:
                jsn = json.load(file)
                self.items = jsn.get('items')
                self.capacity = jsn.get('capacity')
        except FileNotFoundError:
            self.items = []

    def add_item(self, item, count):
            
            item_added = False
            for backpack_item in self.items:
                print("looking for item")
                if backpack_item['name'] == item:
                    backpack_item['count'] += count
                    item_added = True
                    return
            if not item_added:
                print("adding item")
                self.items.append({
                    'name': item,
                    'count': count
                })
                    

    def remove_item(self, item_name, count):
        for backpack_item in self.items:
            if backpack_item['name'] == item_name:
                print(backpack_item)
                print(backpack_item['name'])
                if backpack_item['count'] > count:
                    backpack_item['count'] -= count
                elif backpack_item['count'] == count:
                    backpack_item['count'] = 0
                else:
                    raise ValueError("Not enough items to remove")
                return
        raise ValueError("Item not found in backpack")

    def get_item(self, name):
        for item in self.items:
            if item['name'] == name:
                return item
        raise ValueError(f"Item with name '{name}' not found")
    
    def get_item_description(self, name):
        iM = ItemManager('items.json')
        try:
            return iM.get_item(name).get_item_description()
        except:
            return "Item not found"
       
    def get_item_count(self, name):
        
        try:
            # print("getting item count")
            for item in self.items:
                if item['name'] == name:
                    return item['count']
        except:
            return 0
        

    def upgrade_backpack(self):
        if (self.capacity == 5):
            if (self.get_item_count("stick") >= 5):
                x = input("backpack can be upgraded to a capacity of 6. \n Upgrade?(y/n)   ")
                print(x)
                if (x.lower() == ("y")):
                    print("Upgrading backpack")
                    self.capacity = 6
                    self.remove_item("stick", 5)
                    print("Backpack upgraded to a capacity of 6 \n")
            else: 
                print("Not enough sticks to upgrade backpack. For this level you need 5 sticks \n")

        elif (self.capacity == 6):
            if (self.get_item_count("rock") >= 5):
                x = input("backpack can be upgraded to a capacity of 10. \n Upgrade?(y/n)   ")
                if (x.lower() == "y"):
                    self.capacity = 7
                    self.remove_item("rock", 5)
                    print("Backpack upgraded to a capacity of 7 \n")
            else: 
                print("Not enough rocks to upgrade backpack. For this level you need 5 rocks \n")


    def save_backpack(self):
        with open(self.file_path, 'w') as file:
            json.dump({
                'items': self.items,
                'capacity': self.capacity
            }, file, indent=4)


    def reset_backpack(self):
        self.items = []
        self.capacity = 5
        self.save_backpack()





    # print methods
    def __repr__(self):

        return json.dumps(self.items, indent=4)
        
    
    def toString(self):
        for item in self.items:
            print(f"Item: {item['name']} Count: {item['count']}")


    def toTable(self):
        # use pretty tables??? -pip install prettytable 
        print("Item \t\t| Count \n----------------")
        for item in self.items:
            # print(item)
            if ((item == None)):
                break

            else :
                print(f"{item['name']} \t\t| {item['count']}")



        
    

    

# Example usage
if __name__ == "__main__":
    bp = Backpack("back.json")
    print(bp.toString())

    print(bp.get_item_count("stick"))
    
    # bp.upgrade_backpack()
    # bp.add_item("stick", 5)
    # print(bp.toTable())
    # print(bp.toString())
    # bp.upgrade_backpack()
    # bp.save_backpack()
    # print(bp.toString())
    # bp.reset_backpack()

    


