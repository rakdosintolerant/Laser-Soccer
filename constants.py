#This file houses numbers that are never altered during runtime.
#The purpose is organization and so that, if we need to use these
#numbers somewhere else, we can easily call back to them.
#Whenever you add a number to the code that can fit in this file,
#please add it here, then just use constants.[varName] elsewhere.

#pygame constants
screenXSize = 1280
screenYSize = 720
fps = 60

#penguin constants
flungPenguinColor = "red"
unflungPenguinColor = "blue"
elasticity = 0.9
penguinSize = 50
speedReduceOnDrag = 10
penguinMass = 1

#line constants
activeLineWidth = 2
setLineWidth = 1
lineColor = "green"
