import random

class Items:

    ether_coord = ()
    plastic_tube_coord = ()
    syringe_coord =()


    def __init__ (self,laby):
            num_random_positions_items = 3
            random_items_coord = random.sample(laby.list_floors_coord, 3)
            self.ether_coord = random_items_coord[0]
            self.plastic_tube_coord = random_items_coord[1]
            self.syringe_coord = random_items_coord[2]
            laby.update_list_floors_coord(random_items_coord)
