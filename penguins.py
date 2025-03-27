import pygame, constants

#separate file so that main.py isn't as large
#we can separate bulky classes and functions into their own files for organization
class penguin:

    #initialization
    def __init__(self, rectangle, num, screen):
        #define variables for the penguin
        self.rectangle = rectangle
        self.startx = rectangle.x
        self.starty = rectangle.y
        self.screen = screen
        self.num = num
        self.xmove = 0
        self.ymove = 0
        self.flung = False
        self.color = "red"
        self.arrow = [0, 0]
        self.clicked = False
        self.mass = constants.penguinMass

    #Setters to change penguin variables

    #set's movement in x and y, doesn't actually make it move
    def setMove(self, xy):
        self.xmove = xy[0]
        self.ymove = xy[1]
        self.arrow = pygame.mouse.get_pos()

    #this makes the penguin move (with some logic in main)
    def setFlung(self, set):
        self.flung = set

    def setClicked(self, set):
        self.clicked = set
    
    #Getters

    def getMove(self):
        return [self.xmove, self.ymove]
    
    def getMass(self):
        return self.mass
    
    #this means you can just call penguin.id instead of getId(), idk if I like it or not
    @property
    def id(self):
        return self.num
    
    def getFlung(self):
        return self.flung
    
    def getClicked(self):
        return self.clicked
    
    def getRectangle(self):
        return self.rectangle
    
    def getColor(self):
        if self.flung: return constants.flungPenguinColor
        return constants.unflungPenguinColor
    
    #functions that do things

    #renders both the penguin and its corresponding line
    def render(self):
        pygame.draw.rect(self.screen, self.getColor(), self.getRectangle())
        if (self.xmove != 0 or self.ymove != 0) and not self.flung: 
            pygame.draw.line(self.screen, constants.lineColor, [self.getRectangle().centerx, self.getRectangle().centery], self.arrow, constants.setLineWidth)

    #puts the penguin back to its start and changes variables back
    def reset(self):
        self.getRectangle().update(self.startx, self.starty, constants.penguinSize, constants.penguinSize)
        self.setFlung(False)
        self.setMove([0, 0])

    #periodic is a term I know from FRC that means the function runs every frame
    def periodic(self):
        if self.flung:
            self.getRectangle().move_ip(self.xmove, self.ymove)
            self.xmove /= constants.speedReductionPerFrame
            self.ymove /= constants.speedReductionPerFrame
            if abs(self.xmove) < constants.minSpeed: self.xmove = 0
            if abs(self.ymove) < constants.minSpeed: self.ymove = 0
        
