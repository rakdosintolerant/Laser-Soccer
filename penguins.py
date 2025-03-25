# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
click = False
movement = [0, 0]
xmove = 0
ymove = 0

class penguin:
    def __init__(self, rectangle, num):
        self.rectangle = rectangle
        self.num = num
        self.xmove = 0
        self.ymove = 0
        self.flung = False
        self.color = "red"
    
    def setMove(self, xy):
        self.xmove = xy[0]
        self.ymove = xy[1]

    def setFlung(self, set):
        self.flung = set
    
    def getMove(self):
        return [self.xmove, self.ymove]
    
    def getFlung(self):
        return self.flung
    
    def getRectangle(self):
        return self.rectangle
    
    def getColor(self):
        if self.flung: return "red"
        return "blue"
    
    def render(self):
        pygame.draw.rect(screen, self.getColor(), self.getRectangle())

    def move(self):
        self.getRectangle().move_ip(self.xmove, self.ymove)
    
penguin1 = penguin(pygame.Rect(600, 300, 50, 50), 1)

flingButton = pygame.Rect(600, 500, 200, 100)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: 
            click = True
            penguin1.getRectangle().update(600, 300, 50, 50)
            pygame.mouse.set_pos(penguin1.getRectangle().centerx, penguin1.getRectangle().centery)
            pygame.mouse.get_rel()
        elif event.type == pygame.MOUSEBUTTONUP: 
            click = False
            movement = pygame.mouse.get_rel()
            penguin1.setMove([movement[0] / 10, movement[1] / 10])
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    if click:
        #pygame.draw.rect(screen, penguin.getColor(), penguin1.getRectangle())
        penguin1.setFlung(False)
        penguin1.render()
        pygame.draw.line(screen, "green", [penguin1.getRectangle().centerx, penguin1.getRectangle().centery], pygame.mouse.get_pos())
    else: 
        penguin1.setFlung(True)
        penguin1.move()
        penguin1.render()

    if penguin1.getFlung():
        penguin1.move()

    pygame.draw.rect(screen, "white", flingButton)
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()