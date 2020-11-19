import constants


class Maze:

    list_walls_coord = []
    list_floors_coord = []
    position_guard_coord = ()
    position_departure_coord = ()

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

    def update_list_floors_coord(self, list_items_coord):
        for coord in list_items_coord:
            self.list_floors_coord.remove(coord)

