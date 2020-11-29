
class Heroes:

    heroes_position = ()
    #Inventaire gyver
    heroes_inventory = 0

    def __init__(self, laby):
        #définition de la position de l'heros
        self.heroes_position = laby.position_departure_coord
        print('INIT HERO')


