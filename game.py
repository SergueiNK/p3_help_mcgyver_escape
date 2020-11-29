import time

import pygame
import constants
from heroes import Heroes
from maze import Maze


def init_game_structure(laby, heroe, close_game):
    # lancer les modules pygame
    successes, failures = pygame.init()
    print("{0} successes and {1} failures".format(successes, failures))

    # lancement de la boucle pour garder l'ouverture de l'écran
    running = True
    while running:
        if close_game:
            #time 1s sans rien faire pour lire
            time.sleep(1)
            running = False
            pygame.quit()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    manag_heroes_move(event, laby, heroe)

            # mise à jour de l'écran
            pygame.display.update()


def set_case_definition(laby, heroe):

    # fonction d'attribution de cases

    show_departure = pygame.image.load(constants.IMAGE_GYVER).convert_alpha()
    SCREEN.blit(show_departure, heroe.heroes_position)

    show_guard = pygame.image.load(constants.IMAGE_GUARD).convert_alpha()
    SCREEN.blit(show_guard, laby.position_guard_coord)

    show_wall = pygame.image.load(constants.IMAGE_WALL).convert_alpha()
    show_floor = pygame.image.load(constants.IMAGE_FLOOR).convert_alpha()

    if laby.ether_coord != ():
        show_ether_coord = pygame.image.load(constants.IMAGE_ETHER).convert_alpha()
        SCREEN.blit(show_ether_coord, laby.ether_coord)

    if laby.plastic_tube_coord != ():
        show_plastic_tube_coord = pygame.image.load(constants.IMAGE_PLASTIC_TUBE).convert_alpha()
        SCREEN.blit(show_plastic_tube_coord, laby.plastic_tube_coord)

    if laby.syringe_coord != ():
        show_syringe_coord = pygame.image.load(constants.IMAGE_SYRINGE).convert_alpha()
        SCREEN.blit(show_syringe_coord, laby.syringe_coord)

    # Dimension prémier tuple est la position et le deuxiéme size
    for coord in laby.list_walls_coord:
        SCREEN.blit(show_wall, coord)
    for coord in laby.list_floors_coord:
        SCREEN.blit(show_floor, coord)


def end_game(laby, heroe):

    #print('show notification')
    font_obj = pygame.font.Font('freesansbold.ttf', 32)

    if heroe.heroes_inventory == 3:
        text_words = "YOU WIN. THE GUARD IS SLEEPING. PLAY AGAIN? Y/N"
        close_game = True
        color = constants.GREEN
    else:
        text_words = "YOU LOOSE. DEAD! PLAY AGAIN?.Y/N"
        close_game = False
        color = constants.RED

    text = font_obj.render(text_words, True, color)
    text_position = text.get_rect()
    text_position.center = (340, 340)
    SCREEN.blit(text, text_position)

    pygame.display.update()
    init_game_structure(laby, heroe, close_game)

# définir le texte réelle en gras ou non (True/False), la couleur, couleur de marquage




def manag_heroes_move(event, laby, heroe):
    coord_hero_T1 = list(heroe.heroes_position)
    if event.key == pygame.K_UP:
        coord_hero_T1[1] = coord_hero_T1[1] - 45
        # on rentre dans la position du tuple index [1] qui correspond aSCREEN.blit(show_floor, coord)u déplacement sur y
    elif event.key == pygame.K_LEFT:
        coord_hero_T1[0] = coord_hero_T1[0] - 45
        # on rentre dans la position du tuple index [0] qui correspond au déplacement sur x
    elif event.key == pygame.K_DOWN:
        coord_hero_T1[1] = coord_hero_T1[1] + 45
    elif event.key == pygame.K_RIGHT:
        # Modifier le tuple pour avoir la futur position
        coord_hero_T1[0] = coord_hero_T1[0] + 45

    if tuple(coord_hero_T1) not in laby.list_walls_coord:
        # fin de la partie version simplifié
        if tuple(coord_hero_T1) == laby.position_guard_coord:
            end_game(laby, heroe)
            #fin de la partie final:
            #si l'inventaire heroe == 3 piéces alors
        elif tuple(coord_hero_T1) == laby.ether_coord:
            #ether devient un floor
            laby.update_list_floors_coord([laby.ether_coord])
            laby.ether_coord = ()
            heroe.heroes_inventory += 1
        elif tuple(coord_hero_T1) == laby.syringe_coord:
            laby.update_list_floors_coord([laby.syringe_coord])
            laby.syringe_coord = ()
            heroe.heroes_inventory += 1
        elif tuple(coord_hero_T1) == laby.plastic_tube_coord:
            laby.update_list_floors_coord([laby.plastic_tube_coord])
            laby.plastic_tube_coord = ()
            heroe.heroes_inventory += 1

        laby.update_list_floors_coord([heroe.heroes_position, tuple(coord_hero_T1)])
        heroe.heroes_position = tuple(coord_hero_T1)
        set_case_definition(laby, heroe)


# # # # # # # # #
#     MAIN
# # # # # # # # #
# Initialisation du Pygame
pygame.init()

# configuration d'un nom pour la fenêtre Pygame
pygame.display.set_caption('Help McGyver escape')

# Programm update ( speed of udate depend of pc's power)
# Frames per second
CLOCK_UPDATES = pygame.time.Clock()
CLOCK_UPDATES.tick(constants.FPS)

# Définition des paramétres d'écran
SCREEN = pygame.display.set_mode(constants.SCREEN_SIZE, pygame.RESIZABLE)
SCREEN.fill(constants.BACKGROUND_COLOUR)

# Pour créer main Maze
laby = Maze()
heroe = Heroes(laby)

set_case_definition(laby, heroe)

init_game_structure(laby, heroe, False)

######## Pour afficher le texte avec Pygame
# type et la taille du texte

