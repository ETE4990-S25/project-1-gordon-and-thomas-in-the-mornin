import json

class Item:
    def __init__(self, name, description, items_needed, rarity):
        self.name = name
        self.description = description
        self.items_needed = items_needed
        self.rarity = rarity

    def __repr__(self):
        return f"Item(name={self.name}, description={self.description}, items_needed={self.items_needed}, rarity={self.rarity})"

    def get_item_name(self):
        return self.name

    def get_item_description(self):
        return self.description
    
    def get_item_items_needed(self):
        return self.items_needed
    
    def get_item_rarity(self):
        return self.rarity
    
      
    
class ItemManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.items = []
        self.load_items()

    def load_items(self):
        with open(self.file_path, 'r') as file:
            items_data = json.load(file)
            self.items = [Item(
                name=item['name'],
                description=item['description'],
                items_needed=item['itemsNeeded'],
                rarity=item['rarity']
            ) for item in items_data]

    def get_item(self, name):
        for item in self.items:
            if item.name == name:
                return item
        raise ValueError(f"Item with name '{name}' not found")
    
   
    



# Example usage
if __name__ == "__main__":
    item_manager = ItemManager('items.json')
    print(item_manager.get_item("stick").get_item_items_needed())  # Retrieve item by name
    print(item_manager.get_item("stone pickaxe"))  # Retrieve another item by name


