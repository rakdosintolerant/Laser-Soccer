#This file houses numbers that are never altered during runtime.
#The purpose is organization and so that, if we need to use these
#numbers somewhere else, we can easily call back to them.
#Whenever you add a number to the code that can fit in this file,
#please add it here, then just use constants.[varName] elsewhere.

#pygame constants
screenXSize = 1280
screenYSize = 720
fps = 60

#general game constants
backGroundColor = {"redFling" : [50, 0, 0], "blueFling" : [0, 0, 50], "flinging" : [0, 0, 0]}

#penguin constants
flungPenguinColor = "red"
unflungPenguinColor = "blue"
penguinSize = 50
speedReduceOnDrag = 10
penguinMass = 1

#line constants
activeLineWidth = 2
setLineWidth = 1
lineColor = "green"

#wall constants
wallMass = 10

#net constants
postMass = 10

#physics constants
elasticity = 0.9
speedReductionPerFrame = 1.05
minSpeed = 0.01