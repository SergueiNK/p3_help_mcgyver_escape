from maze import Maze
import constants


class Heroes:
    # coordonnée initiales de l'heros
    # logique du déplacement de l'heros :
    # définir la logique du déplacemen vers la droite, gauche, bas, haut
    # récuperation des coordonnées du déplacement
    heroes_position = ()
    heroes_inventory = 0

    def __init__(self, laby):
        self.heroes_position = laby.position_departure_coord
        print('INIT HERO')
        # print(self.heroes_position)

