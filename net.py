import pygame, constants

class soccerNet:
    def __init__(self, top, screen):
        self.top = top
        if top:
            self.leftPost = pygame.Rect(constants.leftPostStartX, 0, constants.postWidth, constants.netHeight)
            self.rightPost = pygame.Rect(constants.rightPostStartX, 0, constants.postWidth, constants.netHeight)
            self.scoringArea = pygame.Rect(constants.scoringAreaStartX, 0, constants.scoringAreaWidth, constants.netHeight)
            self.right = True
        else:
            self.leftPost = pygame.Rect(constants.leftPostStartX, constants.screenYSize - constants.netHeight, constants.postWidth, constants.netHeight)
            self.rightPost = pygame.Rect(constants.rightPostStartX, constants.screenYSize - constants.netHeight, constants.postWidth, constants.netHeight)
            self.scoringArea = pygame.Rect(constants.scoringAreaStartX, constants.screenYSize - constants.netHeight, constants.scoringAreaWidth, constants.netHeight)
            self.right = False
        self.speed = constants.netStartSpeed
        self.screen = screen

    def periodic(self, process):
        if process[0] == "flinging":
            if self.right:
                self.leftPost.move_ip(self.speed, 0)
                self.rightPost.move_ip(self.speed, 0)
                self.scoringArea.move_ip(self.speed, 0)
                if self.rightPost.x > constants.screenXSize - constants.postWidth:
                    self.right = False
            else:
                self.leftPost.move_ip(-self.speed, 0)
                self.rightPost.move_ip(-self.speed, 0)
                self.scoringArea.move_ip(-self.speed, 0)
                if self.leftPost.x < 0:
                    self.right = True

    def getSpeed(self):
        if self.right:
            return self.speed
        else: return 0 - self.speed

    def getLeftPost(self):
        return self.leftPost
    
    def getRightPost(self):
        return self.rightPost
    
    def getScoringArea(self):
        return self.scoringArea
    
    def turn(self, turnValue):
        if turnValue == "noTurn": return
        if abs(turnValue) < self.speed: self.right = not self.right

    def render(self):
        pygame.draw.rect(self.screen, "white", self.leftPost)
        pygame.draw.rect(self.screen, "white", self.rightPost)
        pygame.draw.rect(self.screen, "orange", self.scoringArea)