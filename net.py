import pygame, constants

class soccerNet:
    def __init__(self, team, screen):
        self.team = team
        if team == 0:
            self.leftPost = pygame.Rect(constants.leftPostStartX, 0, constants.postWidth, constants.netHeight)
            self.rightPost = pygame.Rect(constants.rightPostStartX, 0, constants.postWidth, constants.netHeight)
            self.backPost = pygame.Rect(constants.scoringAreaStartX, 0, constants.scoringAreaWidth, constants.backPostHeight)
            self.scoringArea = pygame.Rect(constants.scoringAreaStartX, 0, constants.scoringAreaWidth, constants.netHeight)
            self.image = pygame.transform.scale(pygame.image.load("images/redNetFixed.png"), (constants.scoringAreaWidth + 50, constants.netHeight))
            self.right = True
        else:
            self.leftPost = pygame.Rect(constants.leftPostStartX, constants.screenYSize - constants.netHeight, constants.postWidth, constants.netHeight)
            self.rightPost = pygame.Rect(constants.rightPostStartX, constants.screenYSize - constants.netHeight, constants.postWidth, constants.netHeight)
            self.backPost = pygame.Rect(constants.scoringAreaStartX, constants.screenYSize - constants.backPostHeight, constants.scoringAreaWidth, constants.backPostHeight)
            self.scoringArea = pygame.Rect(constants.scoringAreaStartX, constants.screenYSize - constants.netHeight, constants.scoringAreaWidth, constants.netHeight)
            self.right = False
            self.image = pygame.transform.scale(pygame.image.load("images/blueNet.png"), (constants.scoringAreaWidth + 50, constants.screenYSize - constants.netHeight))

        self.speed = constants.netStartSpeed
        self.screen = screen

    def periodic(self, process):
        if process[0] == "flinging":
            if self.right:
                self.leftPost.move_ip(self.speed, 0)
                self.rightPost.move_ip(self.speed, 0)
                self.backPost.move_ip(self.speed, 0)
                self.scoringArea.move_ip(self.speed, 0)
                if self.rightPost.x > constants.screenXSize - constants.postWidth:
                    self.right = False
            else:
                self.leftPost.move_ip(-self.speed, 0)
                self.rightPost.move_ip(-self.speed, 0)
                self.backPost.move_ip(-self.speed, 0)
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
    
    def getBackPost(self):
        return self.backPost
    
    def getScoringArea(self):
        return self.scoringArea
    
    def getTeam(self):
        return self.team
    
    def reset(self):
        self.leftPost.x = constants.leftPostStartX
        self.rightPost.x = constants.rightPostStartX
        self.backPost.x = constants.scoringAreaStartX
        self.scoringArea.x = constants.scoringAreaStartX
    
    def turn(self, turnValue):
        if turnValue == "noTurn": return
        if abs(turnValue) < self.speed: self.right = not self.right

    def render(self):
        pygame.draw.rect(self.screen, "white", self.leftPost)
        pygame.draw.rect(self.screen, "white", self.rightPost)
        pygame.draw.rect(self.screen, "orange", self.scoringArea)
        pygame.draw.rect(self.screen, "white", self.backPost)
        self.screen.blit(self.image, self.leftPost)
