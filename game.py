import time

import pygame
import constants
from heroes import Heroes
from maze import Maze


def main():
    # Pour créer main Maze
    laby = Maze()
    heroe = Heroes(laby)

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

    set_case_definition(SCREEN, laby, heroe)

    # Conditions génerales False pour la fin de partie. C'est à dire que gyver n'est pas encore arrivée vers le garde
    # et le jeux peut se derouler normalement

    init_game_structure(SCREEN, laby, heroe, False)


def init_game_structure(SCREEN, laby, heroe, close_game):
    # lancer les modules pygame
    successes, failures = pygame.init()
    print("{0} successes and {1} failures".format(successes, failures))

    # lancement de la boucle pour garder l'ouverture de l'écran
    running = True
    while running:
        # si hero sur le gardien (je viens de la fonction end_game)
        if close_game:
            time.sleep(2)
            running = False
            pygame.quit()
        # sinon écoute des evenements
        else:
            # boucle d'ecoute des évenements
            for event in pygame.event.get():

                # si on appuie sur la croix:
                # condition pour quitter le jeux en appuiant sur la croix
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

                # si non si:
                # condition pour la lecture d'appuye sur les touches
                elif event.type == pygame.KEYDOWN:
                    # Définition initiales de coordonnées de gyver
                    if heroe.manag_heroes_move(event.key):
                        end_game(SCREEN, laby, heroe)
                    else:
                        set_case_definition(SCREEN, laby, heroe)
                # mise à jour de l'écran
                pygame.display.update()


def set_case_definition(SCREEN, laby, heroe):

    # affichage d'image par case

    show_departure = pygame.image.load(constants.IMAGE_GYVER).convert_alpha()
    SCREEN.blit(show_departure, heroe.heroes_position)

    show_guard = pygame.image.load(constants.IMAGE_GUARD).convert_alpha()
    SCREEN.blit(show_guard, laby.position_guard_coord)

    show_wall = pygame.image.load(constants.IMAGE_WALL).convert_alpha()
    show_floor = pygame.image.load(constants.IMAGE_FLOOR).convert_alpha()

    # condition d'affichage des objets
    # si les coordonnées de laby.ether_coord ne sont pas nuls alors. Pareil pour les trois autres objets.
    if laby.ether_coord != ():
        show_ether_coord = pygame.image.load(constants.IMAGE_ETHER).convert_alpha()
        SCREEN.blit(show_ether_coord, laby.ether_coord)

    if laby.tube_coord != ():
        show_plastic_tube_coord = pygame.image.load(constants.IMAGE_PLASTIC_TUBE).convert_alpha()
        SCREEN.blit(show_plastic_tube_coord, laby.tube_coord)

    if laby.syringe_coord != ():
        show_syringe_coord = pygame.image.load(constants.IMAGE_SYRINGE).convert_alpha()
        SCREEN.blit(show_syringe_coord, laby.syringe_coord)

    # Dimension prémier tuple est la position et le deuxiéme size. Affichage d'images des mûrs et des chemins.
    for coord in laby.list_walls_coord:
        SCREEN.blit(show_wall, coord)
    for coord in laby.list_floors_coord:
        SCREEN.blit(show_floor, coord)


def end_game(SCREEN, laby, heroe):

    # Fonction de conditions et d'affichage de fin de partie
    # définition de la police et de dimension du texte
    font_obj = pygame.font.Font('freesansbold.ttf', 20)

    # affichage de la condition de la partie gagnante/perdante
    if heroe.heroes_inventory == 3:
        text_words = "YOU WIN. THE GUARD IS SLEEPING."
        color = constants.GREEN
    else:
        text_words = "YOU LOOSE. DEAD!"
        color = constants.RED

    # définir le texte réelle en gras ou non (True/False), la couleur et définition du texte.
    text = font_obj.render(text_words, True, color)
    text_position = text.get_rect()
    text_position.center = (340, 340)
    SCREEN.blit(text, text_position)

    # rafraichissement d'image
    pygame.display.update()

    # Appel de la fonction avec condition True pour la fermeture du jeux
    init_game_structure(SCREEN, laby, heroe, True)


if __name__ == "__main__":
    main()
