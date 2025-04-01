#This file houses numbers that are never altered during runtime.
#The purpose is organization and so that, if we need to use these
#numbers somewhere else, we can easily call back to them.
#Whenever you add a number to the code that can fit in this file,
#please add it here, then just use constants.[varName] elsewhere.

#pygame constants
screenXSize = 1400
screenYSize = 800
fps = 60

#general game constants
backGroundColor = {"redFling" : [50, 0, 0], "blueFling" : [0, 0, 50], "flinging" : [0, 0, 0]}

#net constants
postMass = 10
netHeight = 100
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
leftRightPenguinOffset = 300
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

#physics constants
elasticity = 0.9
speedReductionPerFrame = 1.01
minSpeed = 0.5
