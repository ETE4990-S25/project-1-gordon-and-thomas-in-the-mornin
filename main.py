
from itmes.items import ItemManager


item_manager = ItemManager('itmes\\items.json')
print(item_manager.get_item("stick"))  # Retrieve item by name
print(item_manager.get_item("stone pickaxe"))