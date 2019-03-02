import game
# import gameAI
from pygame import *
import pygame
import pygbutton

pygame.init()


def game_intro():
    intro = True
    btPlay = pygbutton.PygButton((game.width / 4, game.height / 1.25, 100, 50), 'Play')
    btQuit = pygbutton.PygButton((game.width * 3/4, game.height / 1.25, 100, 50), 'Quit')

    while intro:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                game.Exit()
            if 'click' in btPlay.handleEvent(e):
                game.game_loop()
            if 'click' in btQuit.handleEvent(e):
                game.Exit()

        game.screen.fill(game.white)
        pygame.font.init()

        menu = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = game.text_objects("Flappy Bird", menu)
        TextRect.center = ((game.width / 2), (game.height / 3))
        game.screen.blit(TextSurf, TextRect)

        by = pygame.font.Font('freesansbold.ttf', 30)
        TextSurfBy, TextRectBy = game.text_objects("By Sergi Castro (2018)", by)
        TextRectBy.center = ((game.width * 3/4), (game.height * 0.45))
        game.screen.blit(TextSurfBy, TextRectBy)

        btPlay.draw(game.screen)
        btQuit.draw(game.screen)
        display.update()
        game.clock.tick(15)


def game_over():
    over = True
    btPlay = pygbutton .PygButton((game.width / 4, game.height / 1.25, 100, 50), 'Replay')
    btMenu = pygbutton .PygButton((game.width / 2, game.height / 1.25, 100, 50), 'Menu')
    btQuit = pygbutton.PygButton((game.width * 3/4, game.height / 1.25, 100, 50), 'Quit')

    while over:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                game.Exit()
            if 'click' in btPlay.handleEvent(e):
                game.game_loop()
            if 'click' in btQuit.handleEvent(e):
                game.Exit()
            if 'click' in btMenu.handleEvent(e):
                game_intro()

        game.screen.fill(game.white)
        pygame.font.init()
        gameOverFont = pygame.font.SysFont('freesansbold.ttf', 100)
        gameover, gameoverRect = game.text_objects('Game over', gameOverFont)
        gameoverRect.center = (game.width/2, game.height / 2)
        game.screen.blit(gameover, gameoverRect)

        btPlay.draw(game.screen)
        btMenu.draw(game.screen)
        btQuit.draw(game.screen)

        display.update()
        game.clock.tick(15)


if __name__ == "__main__":
    game_intro()
