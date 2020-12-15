#!/usr/bin/python3.9
# -*-coding:utf-8 -
"""Program "Help MacGyver to escape!"""

import time
import pygame
import constants
from heroes import Heroes
from maze import Maze


class Game:
    """
    class Game who defined the display and end of game

    Methods: main, init_game_structure, set_case_definition,
            end_game
    
    """

    def main(self):
        """
        Create the main Maze
        Initial display initialization

        """
        laby = Maze()
        heroe = Heroes(laby)

        """Pygame initialisation"""
        pygame.init()

        """Configuring a name for the Pygame window"""
        pygame.display.set_caption('Help McGyver escape')

        """
         Program update (speed of update depend of pc's power)
         Frames per second
        """
        clock_updates = pygame.time.Clock()
        clock_updates.tick(constants.fps)

        """Screen setting"""
        screen = pygame.display.set_mode(constants.screen_size, pygame.RESIZABLE)
        screen.fill(constants.background_colour)
        self.set_case_definition(screen, laby, heroe)

        """ 
        Booleans False = the game continues.
        The hero are not yet arrived to guardian
        """
        self.init_game_structure(screen, laby, heroe, False)

    def init_game_structure(self, screen, laby, heroe, close_game):
        """
        Main pygame game loop
        """

        """Launch pygame modules"""
        successes, failures = pygame.init()
        print("{0} successes and {1} failures".format(successes, failures))

        """launch of the loop to keep the screen open"""
        running = True
        while running:
            """if hero on the guardian (I come from the end_game function)"""
            if close_game:
                time.sleep(3)
                running = False
                pygame.quit()
            else:
                """events listening loop"""
                for event in pygame.event.get():
                    """Press the cross to quit the game"""
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()
                    elif event.type == pygame.KEYDOWN:
                        """Loop of display and end game"""
                        if heroe.manag_heroes_move(event.key):
                            self.end_game(screen, laby, heroe)
                        else:
                            self.set_case_definition(screen, laby, heroe)
            """Screen display update"""
            pygame.display.update()

    @staticmethod
    def set_case_definition(screen, laby, heroe):
        """
        Display of all images.
        """
        show_departure = pygame.image.load(constants.image_gyver).convert_alpha()
        screen.blit(show_departure, heroe.heroes_position)

        show_guard = pygame.image.load(constants.image_guard).convert_alpha()
        screen.blit(show_guard, laby.position_guard_coord)

        show_wall = pygame.image.load(constants.image_wall).convert_alpha()
        show_floor = pygame.image.load(constants.image_floor).convert_alpha()

        """Conditions of items' images display"""
        if laby.ether_coord != ():
            show_ether_coord = pygame.image.load(constants.image_ether).convert_alpha()
            screen.blit(show_ether_coord, laby.ether_coord)

        if laby.tube_coord != ():
            show_plastic_tube_coord = pygame.image.load(constants.image_plastic_tube).convert_alpha()
            screen.blit(show_plastic_tube_coord, laby.tube_coord)

        if laby.syringe_coord != ():
            show_syringe_coord = pygame.image.load(constants.image_syringe).convert_alpha()
            screen.blit(show_syringe_coord, laby.syringe_coord)

        "Walls and floors display images"
        for coord in laby.list_walls_coord:
            screen.blit(show_wall, coord)
        for coord in laby.list_floors_coord:
            screen.blit(show_floor, coord)

    def end_game(self, screen, laby, heroe):
        """The conditions of end game"""

        """Definition of the font and the size of the text"""
        font_obj = pygame.font.Font('freesansbold.ttf', 20)

        """Display and condition of the winning/losing game"""
        if heroe.heroes_inventory == 3:
            text_words = "YOU WIN. THE GUARD IS SLEEPING."
            color = constants.green
        else:
            text_words = "YOU LOOSE. DEAD!"
            color = constants.red

        """Defined the text position, bold and color"""
        text = font_obj.render(text_words, True, color)
        text_position = text.get_rect()
        text_position.center = (340, 340)
        screen.blit(text, text_position)

        """Image refresh"""
        pygame.display.update()

        """Call the function if true closed game"""
        self.init_game_structure(screen, laby, heroe, True)


if __name__ == "__main__":
    Game().main()