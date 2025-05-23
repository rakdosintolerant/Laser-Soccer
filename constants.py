#This file houses numbers that are never altered during runtime.
#The purpose is organization and so that, if we need to use these
#numbers somewhere else, we can easily call back to them.
#Whenever you add a number to the code that can fit in this file,
#please add it here, then just use constants.[varName] elsewhere.
import pygame

#pygame constants
screenXSize = 1400
screenYSize = 800
fps = 60

scoreSize = 80
font = "futura"

#net constants
postMass = 10
netHeight = 100
backPostHeight = 10
postWidth = 25
scoringAreaWidth = 600
scoringAreaStartX = screenXSize / 2 - (scoringAreaWidth / 2)
leftPostStartX = scoringAreaStartX - postWidth
rightPostStartX = screenXSize / 2 + (scoringAreaWidth / 2)
netStartSpeed = 1

#penguin constants
flungPenguinColor = "red"
unflungPenguinColor = "blue"
penguinSize = 60
speedReduceOnDrag = 40
penguinMass = 1
leftRightPenguinOffset = 100
middlePenguinStart = screenXSize / 2 - (penguinSize / 2)
rightPenguinStart = middlePenguinStart + leftRightPenguinOffset
leftPenguinStart = middlePenguinStart - leftRightPenguinOffset
redPenguinStart = netHeight
bluePenguinStart = screenYSize - netHeight - penguinSize

#line constants
activeLineWidth = 2
setLineWidth = 1
lineColor = "green"

#ball constants
ballSize = 25
ballMass = 0.5

#wall constants
wallMass = 10
wallThickness = 10
wallImage = pygame.transform.scale(pygame.image.load("images/wallUpdate.png"), (screenXSize, screenYSize))
#wallImage = pygame.image.load("images/wallUpdate.png")
wallRect = pygame.Rect(0, 0, 400, 400)

#physics constants
elasticity = 0.9
speedReductionPerFrame = 1.01
minSpeed = 0.5
terminalVelocity = 20

#opponent constants
targetingMarginOfError = 50
aiPositioningMarginX = 100 #200
aiMinAboveBall = 100
aiMaxAboveBall = 200 #300
maxScreenDist = 300

#general game constants
backGroundColor = {"titleScreen" : [0, 0, 0], "redFling" : [50, 0, 0], "blueFling" : [0, 0, 50], "flinging" : [0, 0, 0]}
#backgroundRect = pygame.Rect(wallThickness, 00, screenXSize - wallThickness, screenYSize)
backgroundRect = pygame.Rect(wallThickness, 00, 600, 400)
backgroundImage = {"titleScreen" : pygame.transform.scale(pygame.image.load("images/flingBackground.png"), (backgroundRect.width, backgroundRect.height)), "flinging" : pygame.transform.scale(pygame.image.load("images/flingBackground.png"), (backgroundRect.width, backgroundRect.height)), "blueFling" : pygame.transform.scale(pygame.image.load("images/blueBackground.png"), (backgroundRect.width, backgroundRect.height)), "redFling" : pygame.transform.scale(pygame.image.load("images/redBackground.png"), (backgroundRect.width, backgroundRect.height))}
#backgroundImage = {"titleScreen" : pygame.image.load("images/flingBackground.png"), "flinging" : pygame.image.load("images/flingBackground.png"), "blueFling" : pygame.image.load("images/blueBackground.png"), "redFling" : pygame.image.load("images/redBackground.png")}
