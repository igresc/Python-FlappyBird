import pygame
from random import randint
import sketch
from math import *

pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Flappy Bird")

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

clock = pygame.time.Clock()
pygame.font.init()


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def Exit():
    pygame.quit()
    quit()


class Bird:
    def __init__(self):
        self.x = 64
        self.y = int(height / 2)
        self.radius = 20
        self.gravity = 0.6
        self.velocity = 0
        self.lift = -10

    def show(self):
        screen.fill(black)
        pygame.draw.circle(screen, white, [int(self.x), int(self.y)], self.radius)

    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity

        if self.y + self.radius > height:
            self.y = height - self.radius
            self.velocity = 0
        elif self.y - self.radius < 0:
            self.y = self.radius
            self.velocity = 0

    def up(self):
        self.velocity = self.lift


class Pipe:
    def __init__(self):
        self.spacing = 175
        self.top = randint(height/6, 3/4 * height)
        self.bottom = self.top + self.spacing
        self.x = width
        self.w = 30
        self.speed = 3

    def show(self):
        self.topRect = pygame.Rect(self.x, 0, self.w, self.top)
        self.bottomRect = pygame.Rect(self.x, self.bottom, self.w, height-self.bottom)
        pygame.draw.rect(screen, green, self.topRect)
        pygame.draw.rect(screen, green, self.bottomRect)

    def update(self):
        self.x -= self.speed

    def hit(self, bird):
        distTop = sqrt((self.x - bird.x)**2 + (bird.y - self.top)**2)
        distTop2 = sqrt((self.x + self.w - bird.x)**2 + (bird.y - self.top)**2)

        distBottom = sqrt((self.x - bird.x)**2 + (bird.y - self.bottom)**2)
        distBottom2 = sqrt((self.x + self.w - bird.x)**2 + (bird.y - self.bottom)**2)

        if bird.y <= self.top or bird.y >= self.bottom:
            distToLine = abs(bird.x - self.x)
            if distToLine <= bird.radius:
                return True
        if distTop <= bird.radius or distTop2 <= bird.radius or distBottom <= bird.radius or distBottom2 <= bird.radius:
            return True


def game_loop():
    bird = Bird()

    pipes = [Pipe(), Pipe(), Pipe()]
    pipes[1].x = width + width / 3
    pipes[2].x = width + 2 * width / 3
    # pipes[3].x = width/2

    score = 0
    run = True

    while True:
        for e in pygame.event.get():
            # print(e)
            if e.type == pygame.QUIT:
                Exit()
            elif pygame.key.get_pressed()[pygame.K_SPACE]:
                bird.up()
            elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
                # run = True
                # pipes[0].x = width
                # pipes[1].x = width + width / 3
                # pipes[2].x = width + 2 * width / 3
                # score = 0
                sketch.game_intro()

        if run:
            bird.show()
            bird.update()
            for i in range(len(pipes)):
                if pipes[i].x < -pipes[i].w:
                    pipes.remove(pipes[i])
                    pipes.append(Pipe())
                    score += 1
                else:
                    pipes[i].show()
                    pipes[i].update()

                if pipes[i].hit(bird):
                    run = False

                # position = pygame.font.SysFont('freesansbold.ttf', 20)\
                #     .render("(x, y): " + str(pipes[i].x) + ", " + str(pipes[i].top), True, white)
                # screen.blit(position, (pipes[i].x + pipes[i].w, pipes[i].top))
                #
                # positionbird = pygame.font.SysFont('freesansbold.ttf', 20)\
                #     .render("(x, y): " + str(bird.x) + ", " + str(bird.y), True, white)
                # screen.blit(positionbird, (bird.x, bird.y))

            scoreMax = 0
            try:
                with open("record.txt", "r") as f:
                    for i in f:
                        scoreMax = i
            except:
                with open("record.txt", "w") as f:
                    f.write(str(score))

            scoreText = pygame.font.SysFont('freesansbold.ttf', 30)
            scoreF = scoreText.render("Score: " + str(score), True, white)
            MaxScore = scoreText.render("Max Score: " + str(scoreMax), True, white)
            screen.blit(scoreF, (0, 0))

            screen.blit(MaxScore, (0, 50))

        elif not run:
            if int(scoreMax) < score:
                    with open("record.txt", "w") as f:
                            f.write(str(score))

            sketch.game_over()

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    game_loop()