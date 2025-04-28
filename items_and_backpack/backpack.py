
import json
from .items import ItemManager

class Backpack:
    def __init__(self, file_path):
        self.file_path = file_path
        self.items = []
        self.capacity = 5
        self.load_items()

    def load_items(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                self.items = data.get('items', [])
                self.capacity = data.get('capacity', 5)
        except FileNotFoundError:
            self.items = []

    def add_item(self, item, count):
        item_added = False
        if count > self.capacity:
            print(f"You dropped {item} because your backpack is full")
            raise ValueError("Cannot add more items than backpack capacity")
        for backpack_item in self.items:
            if backpack_item['name'] == item:
                backpack_item['count'] += count
                item_added = True
                self.save_backpack()
                return
        if not item_added:
            self.items.append({'name': item, 'count': count})

    def remove_item(self, item_name, count):
        for backpack_item in self.items:
            if backpack_item['name'] == item_name:
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
        iM = ItemManager('.\items_and_backpack\items.json')
        try:
            return iM.get_item(name).get_item_description()
        except:
            return "Item not found"

    def get_item_count(self, name):
        try:
            for item in self.items:
                if item['name'] == name:
                    return item['count']
        except:
            return 0


    
    def upgrade_backpack(self):
        backpackUpgrade = {
            5: "stick",
            6: "rock",
            8: "magic stone",
            7: None
        }
        
        if backpackUpgrade[self.capacity] is not None:
            if self.get_item_count(backpackUpgrade[self.capacity]) >= 5:
                choice = input(f"Backpack can be upgraded to a capacity of {self.capacity + 1}. Upgrade? (y/n): ")
                if choice.lower() == "y":
                    self.capacity += 1
                    self.remove_item(backpackUpgrade[self.capacity - 1], 5)
                    print(f"Backpack upgraded to a capacity of {self.capacity}")
                else:
                    print("Backpack upgrade cancelled.")
            else:
                print(f"Not enough {backpackUpgrade[self.capacity]} to upgrade backpack. You need 5 {backpackUpgrade[self.capacity]}s.")
        else:
            print("You already have the max backpack size!!!!")

    def save_backpack(self):
        try:
            with open(self.file_path, 'w') as file:
                json.dump({'items': self.items, 'capacity': self.capacity}, file, indent=4)
        except:
            # file should be overwritten no matter what, but just in case of an edge case
            print("Error saving backpack. Please check the file path and permissions.")

    def reset_backpack(self):
        self.items = []
        self.capacity = 5
        self.save_backpack()

    def __repr__(self):
        return json.dumps(self.items, indent=4)

    def to_string(self):
        for item in self.items:
            print(f"Item: {item['name']} Count: {item['count']}")

    def to_table(self):
        print("Item \t\t| Count \n----------------")
        for item in self.items:
            if item is None:
                break
            else:
                print(f"{item['name']} \t\t| {item['count']}")

# Example usage
if __name__ == "__main__":
    bp = Backpack("back.json")
    bp.to_string()
    print(bp.get_item_count("stick"))

    
    





