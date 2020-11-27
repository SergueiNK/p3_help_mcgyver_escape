import pygame
import constants
from heroes import Heroes
from maze import Maze


def init_game_structure(laby, heroe):
    # lancer les modules pygame
    successes, failures = pygame.init()
    print("{0} successes and {1} failures".format(successes, failures))

    # lancement de la boucle pour garder l'ouverture de l'écran
    running = True
    while running:
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
# définir le texte réelle en gras ou non (True/False), la couleur, couleur de marquage

#Partie gagnante
    text1 = font_obj.render('YOU WIN. THE GUARD IS SLEEPING. PLAY AGAIN? Y/N', True, constants.GREEN)
#Partie perdante
    #text2 = self.font_obj.render('YOU LOOSE. DEAD! PLAY AGAIN?.Y/N ', True, constants.RED)

# Définir le centre de texte sur l'écran:

    text1_position = text1.get_rect()
    #text2_position = text2.get_rect()

# Définir le centre du texte

    text1_position.center = (340, 340)
    #text2_position.center = (340, 340)

    SCREEN.blit(text1, text1_position)

    pygame.display.update()
    init_game_structure(laby, heroe)
####


def manag_heroes_move(event, laby, heroe):
    coord_hero_T1 = list(heroe.heroes_position)
    if event.key == pygame.K_UP:
        coord_hero_T1[1] = coord_hero_T1[1] - 45
        # on rentre dans la position du tuple index [1] qui correspond au déplacement sur y
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
        #print(tuple(coord_hero_T1)) #ok
        #print(coord_hero_T1)
        if tuple(coord_hero_T1) == laby.position_guard_coord:
            print(tuple(coord_hero_T1)) #PB D'affichage
            end_game(laby, heroe)
            print(coord_hero_T1)
            #fin de la partie final:
            #si l'inventaire heroe == 3 piéces alors
        elif tuple(coord_hero_T1) == laby.ether_coord:
            print(coord_hero_T1)
            laby.ether_coord = ()
            laby.update_list_floors_coord([laby.ether_coord, heroe.heroes_position, tuple(coord_hero_T1)])

            heroe.heroes_inventory += 1

            print(heroe.heroes_inventory)
        elif tuple(coord_hero_T1) == laby.syringe_coord:
            laby.syringe_coord = ()
            heroe.heroes_inventory += 1
            laby.update_list_floors_coord([heroe.heroes_position, tuple(coord_hero_T1)])
        elif tuple(coord_hero_T1) == laby.plastic_tube_coord:
            laby.plastic_tube_coord = ()
            heroe.heroes_inventory += 1
            laby.update_list_floors_coord([heroe.heroes_position, tuple(coord_hero_T1)])
        else:
            laby.update_list_floors_coord([heroe.heroes_position, tuple(coord_hero_T1)])
            heroe.heroes_position = tuple(coord_hero_T1)
            set_case_definition(laby, heroe)
        #Si coord_hero_T1 est dans la liste objets
            #enleve la coord de l'objet concerné
            #+1 sur inventaire heros
            #laby.update_list_floors_coord([heroe.heroes_position, tuple(coord_hero_T1)])

    #print(coord_hero_T1)

    # update_heroes_inventory(coord_hero_T1)

 # def update_heroes_inventory(laby, hereo):
 #     # Conditions d'ajout à l'inventaire :
 #     # Si les coordonnées de heros sont dans la list d'objets d'inventaire alors rajouter les coordonnées
 #     # de l'heros à l'inventaire et supprimer la coordonnée de l'heroes de l'inventaire d'objet
 #
 #    if coord_hero_T1 in laby.list_items_coord:
 #       heroe.heroes_inventory.append(coord_hero_T1)
 #       laby.list_items_coord.remove(coord_hero_T1)


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

init_game_structure(laby, heroe)

######## Pour afficher le texte avec Pygame
# type et la taille du texte

