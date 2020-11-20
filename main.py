from heroes import Heroes
from maze import Maze
# from heroes import Heroes
import game


# Pour créer main Maze
laby = Maze()
heroe = Heroes(laby)
# TODO: classe hero

# Pour rélier les fonctions du game avec main et faire passer les parametres
game.set_case_definition(
    laby.list_walls_coord,
    laby.list_floors_coord,
    laby.position_departure_coord,
    laby.position_guard_coord,
    laby.ether_coord,
    laby.plastic_tube_coord,
    laby.syringe_coord,
)
game.init_game_structure()
