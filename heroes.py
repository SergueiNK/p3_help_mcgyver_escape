import pygame


class Heroes:
    """
    class Heroes who defined the hero behavior.

    That class has tree methods.
    The init method defined the hero
    initial position.
    The second is in charge of hero move
    The third is in charge to do the hero move
    and take items

    """

    heroes_position = ()
    heroes_inventory = 0
    laby = ()

    def __init__(self, laby):
        """
        Defined the initial hero position
        Initialised laby use to connection class Maze with Heroes
        """

        # définition de la position de l'heros
        self.heroes_position = laby.position_departure_coord
        # Labyrinth initialisé je le met dans l'heros
        self.laby = laby


    def manag_heroes_move(self, key_pressed):
        """
        Management of hero move.
        """
        # Fonction de gestion des mouvements de l'heros et du rammassage d'objets
        # Définition initiales de coordonnées de gyver
        coord_hero_t1 = list(self.heroes_position)
        if key_pressed == pygame.K_UP:
            coord_hero_t1[1] = coord_hero_t1[1] - 45
            # on rentre dans la position du tuple index [1]
            # qui correspond aSCREEN.blit(show_floor, coord)u déplacement sur y
        elif key_pressed == pygame.K_LEFT:
            coord_hero_t1[0] = coord_hero_t1[0] - 45
            # on rentre dans la position du tuple inde
            # x [0] qui correspond au déplacement sur x
        elif key_pressed == pygame.K_DOWN:
            coord_hero_t1[1] = coord_hero_t1[1] + 45
        elif key_pressed == pygame.K_RIGHT:
            # Modifier le tuple pour avoir la futur position
            coord_hero_t1[0] = coord_hero_t1[0] + 45
        return self.do_heroes_move(tuple(coord_hero_t1))

    def do_heroes_move(self, coord_hero_t1):
        """
        Management of hero items.
        Management of items in floors.
        Update the hero position.
        """
        if coord_hero_t1 not in self.laby.list_walls_coord:
            # fin de la partie je veux que gyver aille sur la case de guard
            if coord_hero_t1 == self.laby.position_guard_coord:
                return 'end'
                # Appelle de l'affichage de fin de partie
            # sinon si les coordonnées correspondent à ceux d'un objet alors
            elif coord_hero_t1 in [self.laby.ether_coord, self.laby.syringe_coord, self.laby.tube_coord]:
                # on appel et modifie la liste des floors en lui enlévant la position du hero
                self.laby.update_list_floors_coord([coord_hero_t1])
                # on rajoute +1 à l'inventaire de gyver
                self.heroes_inventory += 1
                # condition d'enlevement des coordonnées d'objets de la liste
                self.laby.ether_coord = () if coord_hero_t1 == self.laby.ether_coord else self.laby.ether_coord
                self.laby.syringe_coord = () if coord_hero_t1 == self.laby.syringe_coord else self.laby.syringe_coord
                self.laby.tube_coord = () if coord_hero_t1 == self.laby.tube_coord else self.laby.tube_coord

            # On appel et modifie la fonction floors pour mettre à jours la position de l'heros
            self.laby.update_list_floors_coord([self.heroes_position, coord_hero_t1])
            self.heroes_position = coord_hero_t1
