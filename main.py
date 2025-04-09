
from items_and_backpack.backpack import Backpack


from game import intro_screen

bp = Backpack('.\\items_and_backpack\\back.json')



if __name__ == "__main__":
    intro_screen(bp)

