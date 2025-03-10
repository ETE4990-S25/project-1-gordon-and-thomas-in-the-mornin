
if __name__ == "__main__":
    from items import Item, load_items_from_json

    items = load_items_from_json('c:\\Users\\gum12\\Documents\\CS\\project-1-gordon-and-thomas-in-the-mornin\\itmes\\items.json')
    backpack = Backpack()
    backpack.add_item(items[0], 3)  # Add 3 of the first item
    backpack.add_item(items[1], 2)  # Add 2 of the second item
    print(backpack)
    backpack.remove_item(items[0].name, 1)  # Remove 1 of the first item
    print(backpack)