import pygame, constants, random
class powerUp:
    def __init__(self, screen):
        self.screen = screen
        self.rectangle = pygame.Rect(0, 0, constants.powerUpSize, constants.powerUpSize)
        import main
        x = True
        while x:
            self.rectangle.x = random.randint(constants.wallThickness, constants.screenXSize - constants.wallThickness)
            self.rectangle.y = random.randint(constants.netHeight, constants.screenYSize - constants.netHeight)
            x = False
            for penguin in main.penguins:
                if self.rectangle.colliderect(penguin.getRectangle()):
                    x = True

    def getRectangle(self):
        return self.rectangle
    
    def render(self):
        pygame.draw.rect(self.screen, "pink", self.rectangle)

    def acquired(self, team):
        import main
        main.nets[team].setSpeed(4)

