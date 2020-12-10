# import game
from maze import Maze

class Heroes:

    heroes_position = ()
    #Inventaire gyver
    heroes_inventory = 0
    laby = Maze()

    def __init__(self, laby):
        #définition de la position de l'heros
        self.heroes_position = laby.position_departure_coord
        print('INIT HERO')

    def manag_heroes_move(self, laby):
        # Fonction de gestion des mouvements de l'heros et du rammassage d'objets
        # Définition initiales de coordonnées de gyver
        coord_hero_T1 = list(self.heroes_position)
        self.direction = 0
        mouv_validate = False
        if self.direction == "up":
            coord_hero_T1[1] = coord_hero_T1[1] - 45
            # on rentre dans la position du tuple index [1] qui correspond aSCREEN.blit(show_floor, coord)u déplacement sur y
        elif self.direction == "left":
            coord_hero_T1[0] = coord_hero_T1[0] - 45
            # on rentre dans la position du tuple inde
            # x [0] qui correspond au déplacement sur x
        elif self.direction == "down":
            coord_hero_T1[1] = coord_hero_T1[1] + 45
        elif self.direction == "right":
            # Modifier le tuple pour avoir la futur position
            coord_hero_T1[0] = coord_hero_T1[0] + 45

        if laby.validate_new_position(coord_hero_T1) == True:
            self.heroes_position = coord_hero_T1

        if tuple(coord_hero_T1) not in laby.list_walls_coord:
            # fin de la partie je veux que gyver aille sur la case de guard
            if tuple(coord_hero_T1) == laby.position_guard_coord:
                #Appelle de l'affichage de fin de partie
                self.finish = "finish"
                # game.end_game(laby)
                # sinon si les coordonnées correspondent à ceux d'un objet alors
            elif tuple(coord_hero_T1) == laby.ether_coord:
                #on appel et modifie la liste des floors en lui enlévant la position de laby.ether_coord
                laby.update_list_floors_coord([laby.ether_coord])
                laby.ether_coord = ()
                #on rajoute +1 à l'inventaire de gyver
                #c'est la même methode pour les autres objets
                self.heroes_inventory += 1
            elif tuple(coord_hero_T1) == laby.syringe_coord:
                laby.update_list_floors_coord([laby.syringe_coord])
                laby.syringe_coord = ()
                self.heroes_inventory += 1
            elif tuple(coord_hero_T1) == laby.plastic_tube_coord:
                laby.update_list_floors_coord([laby.plastic_tube_coord])
                laby.plastic_tube_coord = ()
                self.heroes_inventory += 1

            # On appel et modifie la fonction floors pour mettre à jours la position de l'heros
            laby.update_list_floors_coord([self.heroes_position, tuple(coord_hero_T1)])
            self.heroes_position = tuple(coord_hero_T1)
            # On appel la fonction pour actualiser l'affichage géneral du labyrinthe
            # game.set_case_definition(laby)

