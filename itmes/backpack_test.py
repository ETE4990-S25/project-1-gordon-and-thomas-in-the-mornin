import unittest
from backpack import Backpack

class TestBackpack(unittest.TestCase):

    def setUp(self):
        self.backpack = Backpack("test_backpack.json")
        self.backpack.reset_backpack()


    # testing add method to add 3 sticks to the bp 
    def test_add_item(self):
        self.backpack.add_item("stick", 3)
        self.assertEqual(self.backpack.get_item_count("stick"), 3)

    # testing if the bp will remove added items correctly
    def test_remove_item(self):
        self.backpack.add_item("stick", 3)
        self.backpack.remove_item("stick", 2)
        self.assertEqual(self.backpack.get_item_count("stick"), 1)

    # check the edge case if more items are called to be removed
    def test_remove_item_not_enough(self):
        self.backpack.add_item("stick", 3)
        with self.assertRaises(ValueError):
            self.backpack.remove_item("stick", 4)

    # testing the edge case that an error will be rasied 
    #  if an item not in inv is called to be removed
    def test_remove_item_not_found(self):
        with self.assertRaises(ValueError):
            self.backpack.remove_item("rock", 1)

    # testing the add item func and if it can be called with the get item func
    def test_get_item(self):
        self.backpack.add_item("stick", 3)
        item = self.backpack.get_item("stick")
        self.assertEqual(item['name'], "stick")
        self.assertEqual(item['count'], 3)

    # testing the edge case if an item not in bp can be called
    def test_get_item_not_found(self):
        with self.assertRaises(ValueError):
            self.backpack.get_item("rock")

    #  testing if the bp will upgrade to one capacity up
    def test_upgrade_backpack(self):
        self.backpack.add_item("stick", 5)
        self.backpack.upgrade_backpack()
        self.assertEqual(self.backpack.capacity, 6)

    # testing to see if the upgrade function will ignore the possibilty of upgrading
    def test_upgrade_backpack_not_enough_items(self):
        self.backpack.add_item("stick", 4)
        self.backpack.upgrade_backpack()
        self.assertEqual(self.backpack.capacity, 5)


    # testing the bp can add 3 items, save, and reopen with the same 3 items
    def test_save_and_load_backpack(self):
        self.backpack.add_item("stick", 3)
        self.backpack.save_backpack()
        new_backpack = Backpack("test_backpack.json")
        self.assertEqual(new_backpack.get_item_count("stick"), 3)


    #  method to run after each to test to reset the backpack state to none
    def tearDown(self):
        self.backpack.reset_backpack()

if __name__ == "__main__":
    unittest.main()
