from maze import Maze

class Heroes:
    # coordonnée initiales de l'heros
    # logique du déplacement de l'heros :
    # définir la logique du déplacemen vers la droite, gauche, bas, haut
    # récuperation des coordonnées du déplacement
    heroes_position = ()

    def __init__(self, laby):
        self.heroes_position = laby.position_departure_coord

    def update_heroes_position (self):
        print('in')
        # for heroes_position in laby.list_floors_coord:
        #          if heroes_position == KEYRIGHT:
        #             self.heroes_position = ((laby.index_x + 1) * constants.TILE_SIZE, laby.index_y * constants.TILE_SIZE)
        #          elif heroes_position == KEYLEFT:
        #              self.heroes_position = ((laby.index_x - 1) * constants.TILE_SIZE, laby.index_y * constants.TILE_SIZE)
        #          elif heroes_position == KEYDOWN:
        #              self.heroes_position = ((laby.index_x + 1) * constants.TILE_SIZE, (laby.index_y + 1) * constants.TILE_SIZE)
        #          elif heroes_position == KEYUP:
        #              self.heroes_position = ((laby.index_x - 1) * constants.TILE_SIZE, (laby.index_y -1) * constants.TILE_SIZE)
        #          else:
        #              return()