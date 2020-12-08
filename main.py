from heroes import Heroes
from maze import Maze
import game

laby = Maze()
heroe = Heroes (laby)

game.init_game_structure(laby.list_walls_coord,
                         laby.list_floors_coord,
                         laby.position_guard_coord,
                         laby.ether_coord,
                         laby.plastic_tube_coord,
                         laby.syringe_coord,
                         laby.update_list_floors_coord
                        )

game.set_case_definition(laby.list_walls_coord,
                         laby.list_floors_coord,
                         laby.position_guard_coord,
                         laby.ether_coord,
                         laby.plastic_tube_coord,
                         laby.syringe_coord,
                        )

game.end_game(laby.list_walls_coord,
              laby.list_floors_coord,
              laby.position_guard_coord,
              laby.ether_coord,
              laby.plastic_tube_coord,
              laby.syringe_coord,
              laby.update_list_floors_coord
              )

game.manag_heroes_move(laby.list_walls_coord,
                       laby.list_floors_coord,
                       laby.position_guard_coord,
                       laby.ether_coord,
                       laby.plastic_tube_coord,
                       laby.syringe_coord,
                       laby.update_list_floors_coord
                       )

game.init_game_structure(laby.list_walls_coord,
                         laby.list_floors_coord,
                         laby.position_guard_coord,
                         laby.ether_coord,
                         laby.plastic_tube_coord,
                         laby.syringe_coord,
                         laby.update_list_floors_coord
                         )


