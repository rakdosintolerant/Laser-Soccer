import pygame, constants
from penguins import penguin
from resolveCollisions import resolveCollision

# pygame setup
pygame.init()
screen = pygame.display.set_mode((constants.screenXSize, constants.screenYSize))
clock = pygame.time.Clock()

#variables (should try to have as few of these possible, it's bad practice)
running = True
click = False
spacePressed = False

class soccerBall:
    def __init__(self):
        self.xmove = 0
        self.ymove = 0
        self.rectangle = pygame.Rect(constants.screenXSize / 2, constants.screenYSize / 2, 25, 25)

    def setMove(self, xy):
        self.xmove, self.ymove = xy[0], xy[1]

    def getMove(self):
        return [self.xmove, self.ymove]
    
    def getRectangle(self):
        return self.rectangle
    
    def getMass(self):
        return 0.5

    def periodic(self):
        self.rectangle.move_ip(self.xmove, self.ymove)
        self.xmove /= constants.speedReductionPerFrame
        self.ymove /= constants.speedReductionPerFrame
        if abs(self.xmove) < constants.minSpeed: self.xmove = 0
        if abs(self.ymove) < constants.minSpeed: self.ymove = 0

    def render(self):
        pygame.draw.rect(screen, "white", self.rectangle)

class soccerNet:
    def __init__(self):
        self.leftPost = pygame.Rect(400, 0, 25, 100)
        self.rightPost = pygame.Rect(600, 0, 25, 100)
        self.scoringArea = pygame.Rect(425, 0, 175, 100)

    def render(self):
        pygame.draw.rect(screen, "white", self.leftPost)
        pygame.draw.rect(screen, "white", self.rightPost)
        pygame.draw.rect(screen, "orange", self.scoringArea)

#functions
def resetPenguins(): #returns all penguins to starting position and manner
    for penguin in penguins:
        penguin.reset()

#initializing penguins/other objects
penguin1 = penguin(pygame.Rect(600, 300, constants.penguinSize, constants.penguinSize), 1, screen)
penguin2 = penguin(pygame.Rect(300, 300, constants.penguinSize, constants.penguinSize), 2, screen)
penguin3 = penguin(pygame.Rect(900, 300, constants.penguinSize, constants.penguinSize), 3, screen)
ball = soccerBall()
topWall = pygame.Rect(0, 0, constants.screenXSize, 1)
leftWall = pygame.Rect(0, 0, 1, constants.screenYSize)
rightWall = pygame.Rect(constants.screenXSize - 1, 0, 1, constants.screenYSize)
bottomWall = pygame.Rect(0, constants.screenYSize - 1, constants.screenXSize, 1)
net = soccerNet()
walls = [topWall, leftWall, rightWall, bottomWall]
penguins = [penguin1, penguin2, penguin3]

while running:
    # poll for events
    # use events for buttons and keys and so forth
    for event in pygame.event.get():
        if not penguin1.getFlung():
            if event.type == pygame.MOUSEBUTTONDOWN: #user clicks
                for penguin in penguins:
                    if penguin.getRectangle().collidepoint(pygame.mouse.get_pos()): #check which penguin is being clicked, if any
                        penguin.setClicked(True)
                        click = True
                        pygame.mouse.set_pos(penguin.getRectangle().centerx, penguin.getRectangle().centery) #puts mouse in the center of the penguin
                        pygame.mouse.get_rel() #remembers where the mouse is
            elif event.type == pygame.MOUSEBUTTONUP: #user releases
                for penguin in penguins:
                    if penguin.getClicked(): #if one of the penguins was being manipulated
                        movement = pygame.mouse.get_rel() #mouse movement from when penguin was initially clicked
                        penguin.setMove([movement[0] / constants.speedReduceOnDrag, movement[1] / constants.speedReduceOnDrag]) #penguin's speed will be based on where user dragged the mouse
                        penguin.setClicked(False)
                        click = False
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and not spacePressed: #if space is being pressed (not held down)
        if not click:
            for penguin in penguins: penguin.setFlung(True) #flings the penguins
        spacePressed = True
    else:
        if (not keys[pygame.K_SPACE]) and spacePressed: #if space was released, variable reflects that
            spacePressed = False

    for penguin in penguins: #checks to see if each penguin is colliding and, if so, runs the physics
        if penguin.getRectangle().colliderect(ball.getRectangle()):
            resolveCollision(penguin, ball)
        for otherPenguin in penguins:
            if penguin.getRectangle().colliderect(otherPenguin.getRectangle()) and penguin.id != otherPenguin.id:
                resolveCollision(penguin, otherPenguin)
        for wall in walls:
            if penguin.getRectangle().colliderect(wall): resolveCollision(penguin, wall)
    for wall in walls:
        if ball.getRectangle().colliderect(wall): resolveCollision(ball, wall)
                
    # RENDER YOUR GAME HERE
    for penguin in penguins:
        if penguin.getClicked():
            pygame.draw.line(screen, constants.lineColor, [penguin.getRectangle().centerx, penguin.getRectangle().centery], pygame.mouse.get_pos(), constants.activeLineWidth)
        penguin.periodic()
        penguin.render()
    ball.periodic()
    ball.render()
    net.render()

    if penguin1.getFlung():
        done = True
        for penguin in penguins:
            if penguin.getMove() != [0, 0]: done = False
        if ball.getMove() != [0, 0]: done = False
        if done:
            for penguin in penguins: penguin.setFlung(False)
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(constants.fps)  # limits FPS to 60

pygame.quit()