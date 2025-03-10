



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

class Backpack:
    def __init__(self):
        self.items = []

    def add_item(self, item, count):
        for backpack_item in self.items:
            if backpack_item['name'] == item.name:
                backpack_item['count'] += count
                return
        self.items.append({
            'name': item.name,
            'count': count,
            'description': item.description
        })

    def remove_item(self, item_name, count):
        for backpack_item in self.items:
            if backpack_item['name'] == item_name:
                if backpack_item['count'] > count:
                    backpack_item['count'] -= count
                elif backpack_item['count'] == count:
                    self.items.remove(backpack_item)
                else:
                    raise ValueError("Not enough items to remove")
                return
        raise ValueError("Item not found in backpack")

    def __repr__(self):
        return json.dumps(self.items, indent=4)

# Example usage

