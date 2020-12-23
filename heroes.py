#!/usr/bin/python3.9
# -*-coding:utf-8 -
import pygame


class Heroes:
    """
    class Heroes who defined the hero behavior.

    Methods : __init__, manag_heroes_move,
             do_heroes_move
    """
    heroes_position = ()
    heroes_inventory = 0
    laby = ()

    def __init__(self, laby):
        """
        Defined the initial hero position
        Initialised laby use to connection class Maze with Heroes
        """
        self.heroes_position = laby.position_departure_coord
        self.laby = laby

    def manag_heroes_move(self, key_pressed):
        """Management of hero move"""

        """Defined the initial hero pisition"""
        coord_hero_t1 = list(self.heroes_position)
        """It's depend of move the title size is removed or add.
        For move on x it use coord_hero_t1[0].
        For move on y it use coord_hero_t1[1]."""
        if key_pressed == pygame.K_UP:
            coord_hero_t1[1] = coord_hero_t1[1] - 45
        elif key_pressed == pygame.K_LEFT:
            coord_hero_t1[0] = coord_hero_t1[0] - 45
        elif key_pressed == pygame.K_DOWN:
            coord_hero_t1[1] = coord_hero_t1[1] + 45
        elif key_pressed == pygame.K_RIGHT:
            coord_hero_t1[0] = coord_hero_t1[0] + 45

        """ Call the heroes coordinates """
        return self.do_heroes_move(tuple(coord_hero_t1))

    def do_heroes_move(self, coord_hero_t1):
        """
        Management of hero items.
        Management of items in floors.
        Update the hero position.
        """
        if coord_hero_t1 not in self.laby.list_walls_coord:
            if coord_hero_t1 == self.laby.position_guard_coord:
                """Call the display of end game"""
                return 'end'
            elif coord_hero_t1 in [self.laby.ether_coord,
                                   self.laby.syringe_coord,
                                   self.laby.tube_coord]:

                """Modification of list-floors with remove of  coord_hero_t1"""
                self.laby.update_list_floors_coord([coord_hero_t1])
                """Modification of heroes inventory"""
                self.heroes_inventory += 1

                """Conditions of remove of items coordinates"""
                self.laby.ether_coord = () \
                    if coord_hero_t1 == self.laby.ether_coord \
                    else self.laby.ether_coord
                self.laby.syringe_coord = () \
                    if coord_hero_t1 == self.laby.syringe_coord \
                    else self.laby.syringe_coord
                self.laby.tube_coord = () \
                    if coord_hero_t1 == self.laby.tube_coord\
                    else self.laby.tube_coord

            """Update the heroes position"""
            self.laby.update_list_floors_coord([self.heroes_position,
                                                coord_hero_t1])
            self.heroes_position = coord_hero_t1
