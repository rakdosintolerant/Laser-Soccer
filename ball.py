import pygame, constants
class soccerBall:
    def __init__(self, screen):
        self.xmove = 0
        self.ymove = 0
        self.screen = screen
        self.rectangle = pygame.Rect(0, 0, constants.ballSize, constants.ballSize)
        self.rectangle.centerx = 300
        self.rectangle.centery = constants.screenYSize / 2

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
        self.rectangle.x = 300
        self.rectangle.y = constants.screenYSize / 2

    def periodic(self):
        self.getRectangle().move_ip(self.xmove, self.ymove)
        self.xmove /= constants.speedReductionPerFrame
        self.ymove /= constants.speedReductionPerFrame
        if abs(self.xmove) < constants.minSpeed: self.xmove = 0
        if abs(self.ymove) < constants.minSpeed: self.ymove = 0

    def render(self):
        pygame.draw.rect(self.screen, "white", self.rectangle)