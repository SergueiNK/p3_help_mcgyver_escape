from maze import Maze
import game


# Pour créer main Maze
laby = Maze()

# Pour rélier les fonctions du game avec main et faire passer les parametres
game.set_case_definition(
    laby.list_walls_coord,
    laby.list_floors_coord,
    laby.position_departure_coord,
    laby.position_guard_coord
)
game.init_game_structure()
