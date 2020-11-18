import pygame
import constants

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


def init_game_structure():
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
        # mise à jour de l'écran
        pygame.display.update()


def set_case_definition(walls_coord, floors_coord, departure_coord, guard_coord):

    # fonction d'attribution de cases

    show_departure = pygame.image.load(constants.IMAGE_GYVER).convert_alpha()
    SCREEN.blit(show_departure, departure_coord)

    show_guard = pygame.image.load(constants.IMAGE_GUARD).convert_alpha()
    SCREEN.blit(show_guard, guard_coord)

    show_wall = pygame.image.load(constants.IMAGE_WALL).convert_alpha()
    show_floor = pygame.image.load(constants.IMAGE_FLOOR).convert_alpha()

    # Dimension prémier tuple est la position et le deuxiéme size
    for coord in walls_coord:
        SCREEN.blit(show_wall, coord)
    for coord in floors_coord:
        SCREEN.blit(show_floor, coord)


