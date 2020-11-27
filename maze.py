import constants
import random

class Maze:

    list_walls_coord = []
    list_floors_coord = []
    position_guard_coord = ()
    position_departure_coord = ()
    ether_coord = ()
    plastic_tube_coord = ()
    syringe_coord = ()
    heroe_position = ()

    def __init__(self):
        with open(constants.STRUCTURE_FILE, 'r') as data:
            for index_y, line in enumerate(data):
                # segmentation par ligne en ordonnées.
                for index_x, case_type in enumerate(line.strip('\n')):
                    # résegmentation par ligne en abcisse + retour à la ligne auto (index_case == parcourir selon index,
                    # cases_type==valeur)
                    coordinate = (index_x * constants.TILE_SIZE, index_y * constants.TILE_SIZE)
                    # attribution des coordonées pour chaque valeur
                    if case_type == '#':
                        self.list_walls_coord.append(coordinate)
                    elif case_type == '.':
                        self.list_floors_coord.append(coordinate)
                    elif case_type == 'X':
                        self.position_departure_coord = coordinate
                    else:
                        self.position_guard_coord = coordinate

            self.init_items_coord()


    def init_items_coord(self):
        random_items_coord = random.sample(self.list_floors_coord, 3)
        #print(random_items_coord)
        self.ether_coord = random_items_coord[0]
        self.plastic_tube_coord = random_items_coord[1]
        self.syringe_coord = random_items_coord[2]
        self.update_list_floors_coord(random_items_coord)


    def update_list_floors_coord(self, list_items_coord):
        for coord in list_items_coord:
            #condition Ajout/suppression de coord

            if coord in self.list_floors_coord:
                self.list_floors_coord.remove(coord)
            else:
                self.list_floors_coord.append(coord)

            # if self.heroe_position  in self.list_floors_coord:
            # self.heroes_position = ((self.index_x + 1) * constants.TILE_SIZE, self.index_y * constants.TILE_SIZE)



