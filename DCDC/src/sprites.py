import pygame

pygame.init()

window = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("Window")

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)

moveX, moveY = 0, 0

clock = pygame.time.Clock()


class Sprite:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.diverFemale = pygame.image.load("assets/Diver Female.png")
        self.diverMale = pygame.image.load("assets/Diver Male.png")
        self.gender = 0
        self.bubbles = pygame.image.load("assets/bubbles.png")

    def update(self):
        # collision

        self.render()

    def render(self):
        if self.gender == 0:
            window.blit(self.diverFemale, (self.x, self.y))
            window.blit(self.bubbles, (self.x + self.width, self.y + self.height))

        else:
            window.blit(self.diverMale, (self.x, self.y))
            window.blit(self.bubbles, (self.x + self.width, self.y + self.height))


player = Sprite(100, 150)

gameLoop = True

while gameLoop:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            gameLoop = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                moveX = -10

            if event.key == pygame.K_RIGHT:
                moveX = 10

            if event.key == pygame.K_UP:
                moveY = -10

            if event.key == pygame.K_DOWN:
                moveY = 10

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                moveX = 0

            if event.key == pygame.K_RIGHT:
                moveX = 0

            if event.key == pygame.K_UP:
                moveY = 0

            if event.key == pygame.K_DOWN:
                moveY = 0

    window.fill(blue)

    player.x += moveX

    player.y += moveY

    player.update()

    clock.tick(60)

    pygame.display.flip()

pygame.quit()
