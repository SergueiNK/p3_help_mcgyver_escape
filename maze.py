import constants
import random


class Maze:
    """
    class Maze who define the labyrinth.

    That class has three methods.
    The init method generate the structure.
    The items coord generate the random coordinate for items.
    The theerd update the list floor coordinate

    Attributes
    ----------

    list_walls_coord : list
        coordinates of labyrinth walls
    list_floors_coord : list
        coordinates of labyrinthe floors
    position_guard_coord : tuple
        coordinates of guard position
    position_departure_coord : tuple
        coordinates of departure position of Gyver
    ether_coord : tuple
        coordinates of object ether
    tube_coord : tuple
        coordinates of object tube
    syringe_coord : tuple
        coordinates of object syring

    """
    list_walls_coord = []
    list_floors_coord = []
    position_guard_coord = ()
    position_departure_coord = ()
    ether_coord = ()
    tube_coord = ()
    syringe_coord = ()

    def __init__(self):
        """
        Create the structure of labyrinth.

        Open the file with labyrinth structure.
        Create the differents list in regard of the type of structure.
        Those lists will be coordinates.
        I
        Parameters
        ----------
        list_walls_coord : list
        coordinates of labyrinth walls
    list_floors_coord : list
        coordinates of labyrinthe floors
    position_guard_coord : tuple
        coordinates of guard position
    position_departure_coord : tuple
        coordinates of departure position of Gyver


        """
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
        # attribution aleatoires de coordonnées aux objets
        random_items_coord = random.sample(self.list_floors_coord, 3)
        self.ether_coord = random_items_coord[0]
        self.tube_coord = random_items_coord[1]
        self.syringe_coord = random_items_coord[2]

        # appel de la fonction update_list_floors_coord
        self.update_list_floors_coord(random_items_coord)

    def update_list_floors_coord(self, list_items_coord):
        for coord in list_items_coord:
            # condition Ajout/suppression de coord dans la list_floors_coord
            if coord in self.list_floors_coord:
                self.list_floors_coord.remove(coord)
            else:
                self.list_floors_coord.append(coord)
