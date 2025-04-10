import pygame, constants
from random import choice
class soccerBall:
    def __init__(self, screen):
        self.xmove = 0
        self.ymove = 0
        self.screen = screen
        self.rectangle = pygame.Rect(0, 0, constants.ballSize, constants.ballSize)
        self.startingPoses = [300, 500, 600, constants.screenXSize - 600, constants.screenXSize - 500, constants.screenXSize - 300]
        self.rectangle.centerx = choice(self.startingPoses)
        self.rectangle.centery = constants.screenYSize / 2
        self.images = (pygame.transform.scale((pygame.image.load("images/ball.png")),(25,25)), pygame.transform.scale(pygame.image.load("images/ballSuper.png"), (25,25)))

    def setMove(self, xy):
        while abs(((xy[0] ** 2) + (xy[1]) ** 2) ** 0.5) > constants.terminalVelocity:
            xy[0] *= 0.99
            xy[1] *= 0.99
        self.xmove, self.ymove = xy[0], xy[1]

    def getMove(self):
        return [self.xmove, self.ymove]
    
    def getRectangle(self):
        return self.rectangle
    
    def getMass(self):
        return constants.ballMass
    
    def reset(self):
        self.setMove([0, 0])
        self.rectangle.x = choice(self.startingPoses)
        self.rectangle.y = constants.screenYSize / 2

    def periodic(self):
        import main
        if main.process[0] == "flinging": self.image = self.images[1]
        else: self.image = self.images[0]
        self.getRectangle().move_ip(self.xmove, self.ymove)
        self.xmove /= constants.speedReductionPerFrame
        self.ymove /= constants.speedReductionPerFrame
        if abs(self.xmove) < constants.minSpeed: self.xmove = 0
        if abs(self.ymove) < constants.minSpeed: self.ymove = 0

    def render(self):
        import main
        try:
            main.screen.blit(self.image, self.rectangle)
        except: main.screen.blit(self.images[0], self.rectangle)
        #pygame.draw.rect(self.screen, "white", self.rectangle)