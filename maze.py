#!/usr/bin/python3.9
# -*-coding:utf-8 -
import constants
import random


class Maze:
    """
    class Maze who defined the labyrinth.

    Methods: __init__, init_items_coord,
            update_list_floors_coord

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
        """

        with open(constants.structure_file, 'r') as data:
            """y-line segmentation"""
            for index_y, line in enumerate(data):
                """x-line segmentation + line break auto"""
                for index_x, case_type in enumerate(line.strip('\n')):
                    coordinate = (index_x * constants.tile_size, index_y * constants.tile_size)
                    """assignment of coordinates for each value"""
                    if case_type == '#':
                        self.list_walls_coord.append(coordinate)
                    elif case_type == '.':
                        self.list_floors_coord.append(coordinate)
                    elif case_type == 'X':
                        self.position_departure_coord = coordinate
                    else:
                        self.position_guard_coord = coordinate
            """Call the function for items coordinates"""
            self.init_items_coord()

    def init_items_coord(self):
        """Define the random coordinates for items"""
        random_items_coord = random.sample(self.list_floors_coord, 3)
        self.ether_coord = random_items_coord[0]
        self.tube_coord = random_items_coord[1]
        self.syringe_coord = random_items_coord[2]
        self.update_list_floors_coord(random_items_coord)

    def update_list_floors_coord(self, list_items_coord):
        """
        Update the list floors coord with
        items coordinates
        """
        for coord in list_items_coord:
            if coord in self.list_floors_coord:
                self.list_floors_coord.remove(coord)
            else:
                self.list_floors_coord.append(coord)
