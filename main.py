import pygame, constants, random
from penguins import penguin
from ball import soccerBall
from net import soccerNet
from resolveCollisions import resolveCollision
from resolveCollisions import resolveNetCollision
# pygame setup
pygame.init()
screen = pygame.display.set_mode((constants.screenXSize, constants.screenYSize))
clock = pygame.time.Clock()

#variables (should try to have as few of these possible, it's bad practice)
redScore = 0
blueScore = 0
running = True
click = False
spacePressed = False
process = ["blueFling", False] #blueFling, redFling, or flinging
redScoreFont = pygame.font.Font(None, 50)
blueScoreFont = pygame.font.Font(None, 50)
redScoreText = redScoreFont.render(str(redScore), True, "yellow")
blueScoreText = blueScoreFont.render(str(blueScore), True, "yellow")
redScoreTextPos = redScoreText.get_rect(x=10, y=10)
blueScoreTextPos = blueScoreText.get_rect(x=10, y=constants.screenYSize - 10 - 50)

#functions
def resetPenguins(): #returns all penguins to starting position and manner
    for penguin in penguins:
        penguin.reset()

def nextStep(): #this could be coded better if you want to fix it Noah
    #if it aint broke don't fix it - Noah
    global process
    if process[0] == "blueFling":
        if process[1]: process[0] = "flinging"
        else: process[0] = "redFling"
    elif process[0] == "redFling": 
        if process[1]: process[0] = "blueFling"
        else: process[0] = "flinging"
    elif process[0] == "flinging": 
        if process[1]: process[0] = "blueFling"
        else: process[0] = "redFling"
        process[1] = not process[1]
    if process[0] == "flinging":
        for penguin in penguins: penguin.setFlung(True)

def score(scored):
    global blueScore, redScore, redScoreText, blueScoreText
    ball.reset()
    if scored == 0: blueScore += 1
    else: redScore += 1
    redScoreText = redScoreFont.render(str(redScore), True, "yellow")
    blueScoreText = blueScoreFont.render(str(blueScore), True, "yellow")
    for penguin in penguins: penguin.reset()
    for net in nets: net.reset()
    nextStep()

#initializing penguins/other objects
redPenguin1 = penguin(pygame.Rect(constants.leftPenguinStart, constants.redPenguinStart, constants.penguinSize, constants.penguinSize), 1, 1, screen)
redPenguin2 = penguin(pygame.Rect(constants.middlePenguinStart, constants.redPenguinStart, constants.penguinSize, constants.penguinSize), 2, 1, screen)
redPenguin3 = penguin(pygame.Rect(constants.rightPenguinStart, constants.redPenguinStart, constants.penguinSize, constants.penguinSize), 3, 1, screen)

bluePenguin1 = penguin(pygame.Rect(constants.leftPenguinStart, constants.bluePenguinStart, constants.penguinSize, constants.penguinSize), 4, 2, screen)
bluePenguin2 = penguin(pygame.Rect(constants.middlePenguinStart, constants.bluePenguinStart, constants.penguinSize, constants.penguinSize), 5, 2, screen)
bluePenguin3 = penguin(pygame.Rect(constants.rightPenguinStart, constants.bluePenguinStart, constants.penguinSize, constants.penguinSize), 6, 2, screen)
ball = soccerBall(screen)
topWall = pygame.Rect(0, 0, constants.screenXSize, constants.netHeight)
leftWall = pygame.Rect(0, 0, constants.wallThickness, constants.screenYSize)
rightWall = pygame.Rect(constants.screenXSize - constants.wallThickness, 0, constants.wallThickness, constants.screenYSize)
bottomWall = pygame.Rect(0, constants.screenYSize - constants.netHeight, constants.screenXSize, constants.netHeight)
topNet = soccerNet(True, screen)
bottomNet = soccerNet(False, screen)
walls = [topWall, leftWall, rightWall, bottomWall]
redPenguins = [redPenguin1, redPenguin2, redPenguin3]
bluePenguins = [bluePenguin1, bluePenguin2, bluePenguin3]
penguins = [redPenguin1, redPenguin2, redPenguin3, bluePenguin1, bluePenguin2, bluePenguin3]
nets = [topNet, bottomNet]

while running:
    # poll for events
    # use events for buttons and keys and so forth
    for event in pygame.event.get():
        if process[0] == "blueFling":
            if event.type == pygame.MOUSEBUTTONDOWN: #user clicks
                for penguin in bluePenguins:
                    if penguin.getRectangle().collidepoint(pygame.mouse.get_pos()): #check which penguin is being clicked, if any
                        penguin.setClicked(True)
                        click = True
                        pygame.mouse.set_pos(penguin.getRectangle().centerx, penguin.getRectangle().centery) #puts mouse in the center of the penguin
                        pygame.mouse.get_rel() #remembers where the mouse is
            elif event.type == pygame.MOUSEBUTTONUP: #user releases
                for penguin in bluePenguins:
                    if penguin.getClicked(): #if one of the penguins was being manipulated
                        movement = pygame.mouse.get_rel() #mouse movement from when penguin was initially clicked
                        penguin.setMove([movement[0] / constants.speedReduceOnDrag, movement[1] / constants.speedReduceOnDrag]) #penguin's speed will be based on where user dragged the mouse
                        penguin.setClicked(False)
                        click = False
        elif process[0] == "redFling":
            for penguin in redPenguins:
                if penguin.getRectangle().centery + 100 < ball.getRectangle().centery:
                    penguin.setMove([(random.randint(ball.getRectangle().centerx - constants.targetingMarginOfError, ball.getRectangle().centerx + constants.targetingMarginOfError) - penguin.getRectangle().centerx) / constants.speedReduceOnDrag, (random.randint(ball.getRectangle().centery - constants.targetingMarginOfError, ball.getRectangle().centery + constants.targetingMarginOfError) - penguin.getRectangle().centery) / constants.speedReduceOnDrag])
                else:
                    if random.choice([True, False]):
                        penguin.setMove([(random.randint(ball.getRectangle().centerx - constants.targetingMarginOfError, ball.getRectangle().centerx + constants.targetingMarginOfError) - penguin.getRectangle().centerx)  - 300 / constants.speedReduceOnDrag, (random.randint(ball.getRectangle().centery - constants.targetingMarginOfError, ball.getRectangle().centery + constants.targetingMarginOfError) - penguin.getRectangle().centery) - 200 / constants.speedReduceOnDrag])
                    else: penguin.setMove([(random.randint(ball.getRectangle().centerx - constants.targetingMarginOfError, ball.getRectangle().centerx + constants.targetingMarginOfError) - penguin.getRectangle().centerx)  + 300 / constants.speedReduceOnDrag, (random.randint(ball.getRectangle().centery - constants.targetingMarginOfError, ball.getRectangle().centery + constants.targetingMarginOfError) - penguin.getRectangle().centery) - 200 / constants.speedReduceOnDrag])



            nextStep()
            # if event.type == pygame.MOUSEBUTTONDOWN: #user clicks
            #     for penguin in redPenguins:
            #         if penguin.getRectangle().collidepoint(pygame.mouse.get_pos()): #check which penguin is being clicked, if any
            #             penguin.setClicked(True)
            #             click = True
            #             pygame.mouse.set_pos(penguin.getRectangle().centerx, penguin.getRectangle().centery) #puts mouse in the center of the penguin
            #             pygame.mouse.get_rel() #remembers where the mouse is
            # elif event.type == pygame.MOUSEBUTTONUP: #user releases
            #     for penguin in redPenguins:
            #         if penguin.getClicked(): #if one of the penguins was being manipulated
            #             movement = pygame.mouse.get_rel() #mouse movement from when penguin was initially clicked
            #             penguin.setMove([movement[0] / constants.speedReduceOnDrag, movement[1] / constants.speedReduceOnDrag]) #penguin's speed will be based on where user dragged the mouse
            #             penguin.setClicked(False)
            #             click = False
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    screen.fill(constants.backGroundColor[process[0]])
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and not spacePressed: #if space is being pressed (not held down)
        if not click:
            nextStep()
        spacePressed = True
    else:
        if (not keys[pygame.K_SPACE]) and spacePressed: #if space was released, variable reflects that
            spacePressed = False

    for net in nets:
        if ball.getRectangle().colliderect(net.getScoringArea()): score(net.getTeam())
        
    for penguin in penguins: #checks to see if each penguin is colliding and, if so, runs the physics
        for net in nets:
            net.turn(resolveNetCollision(penguin, net.getLeftPost(), net.getSpeed()))
            net.turn(resolveNetCollision(penguin, net.getRightPost(), net.getSpeed()))
            resolveNetCollision(penguin, net.getBackPost(), net.getSpeed())
        resolveCollision(penguin, ball)
        for otherPenguin in penguins:
            if penguin.id != otherPenguin.id: resolveCollision(penguin, otherPenguin)
        for wall in walls:
            if not penguin.getRectangle().colliderect(topNet.getScoringArea()) and not penguin.getRectangle().colliderect(bottomNet.getScoringArea()): resolveCollision(penguin, wall)
    for net in nets:
        net.turn(resolveNetCollision(ball, net.getLeftPost(), net.getSpeed()))
        net.turn(resolveNetCollision(ball, net.getRightPost(), net.getSpeed()))
    for wall in walls:
        resolveCollision(ball, wall)
    
    
    # RENDER YOUR GAME HERE
    for wall in walls: pygame.draw.rect(screen, "white", wall)
    for net in nets:
        net.periodic(process)
        net.render()
    for penguin in penguins:
        if penguin.getClicked():
            pygame.draw.line(screen, constants.lineColor, [penguin.getRectangle().centerx, penguin.getRectangle().centery], pygame.mouse.get_pos(), constants.activeLineWidth)
        penguin.periodic()
        penguin.render()
    ball.periodic()
    ball.render()
    screen.blit(redScoreText, redScoreTextPos)
    screen.blit(blueScoreText, blueScoreTextPos)

    if process[0] == "flinging":
        done = True
        for penguin in penguins:
            if penguin.getMove() != [0, 0]: done = False
        if ball.getMove() != [0, 0]: done = False
        if done:
            nextStep()
            for penguin in penguins: penguin.setFlung(False)
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(constants.fps)  # limits FPS to 60

pygame.quit()
