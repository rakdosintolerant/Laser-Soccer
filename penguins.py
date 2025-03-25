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
spacePressed = False

class penguin:
    def __init__(self, rectangle, num):
        self.rectangle = rectangle
        self.startx = rectangle.x
        self.starty = rectangle.y
        self.num = num
        self.xmove = 0
        self.ymove = 0
        self.flung = False
        self.color = "red"
        self.arrow = [0, 0]
        self.clicked = False
    
    def setMove(self, xy):
        self.xmove = xy[0]
        self.ymove = xy[1]
        self.arrow = pygame.mouse.get_pos()

    def setFlung(self, set):
        self.flung = set

    def setClicked(self, set):
        self.clicked = set
    
    def getMove(self):
        return [self.xmove, self.ymove]
    
    def getFlung(self):
        return self.flung
    
    def getClicked(self):
        return self.clicked
    
    def getRectangle(self):
        return self.rectangle
    
    def getColor(self):
        if self.flung: return "red"
        return "blue"
    
    def render(self):
        pygame.draw.rect(screen, self.getColor(), self.getRectangle())
        if (self.xmove != 0 or self.ymove != 0) and not self.flung: 
            pygame.draw.line(screen, "green", [self.getRectangle().centerx, self.getRectangle().centery], self.arrow)

    def reset(self):
        self.getRectangle().update(self.startx, self.starty, 50, 50)
        self.setFlung(False)
        self.setMove([0, 0])


    def move(self):
        self.getRectangle().move_ip(self.xmove, self.ymove)

def resetPenguins():
    for penguin in penguins:
        penguin.reset()

penguin1 = penguin(pygame.Rect(600, 300, 50, 50), 1)
penguin2 = penguin(pygame.Rect(300, 300, 50, 50), 2)
penguin3 = penguin(pygame.Rect(900, 300, 50, 50), 3)
penguins = [penguin1, penguin2, penguin3]



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: 
            for penguin in penguins:
                if penguin.getRectangle().collidepoint(pygame.mouse.get_pos()):
                    penguin.setClicked(True)
                    click = True
                    pygame.mouse.set_pos(penguin.getRectangle().centerx, penguin.getRectangle().centery)
                    pygame.mouse.get_rel()
                #break
        elif event.type == pygame.MOUSEBUTTONUP: 
            for penguin in penguins:
                if penguin.getClicked():
                    movement = pygame.mouse.get_rel()
                    penguin.setMove([movement[0] / 10, movement[1] / 10])
                    penguin.setClicked(False)
                    click = False
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and not spacePressed: 
        if penguin1.getFlung(): resetPenguins()
        else: 
            if not click:
                for penguin in penguins: penguin.setFlung(True)
        spacePressed = True
    else:
        if (not keys[pygame.K_SPACE]) and spacePressed:
            spacePressed = False

    # RENDER YOUR GAME HERE
    for penguin in penguins:
        if penguin.getClicked():
            pygame.draw.line(screen, "green", [penguin.getRectangle().centerx, penguin.getRectangle().centery], pygame.mouse.get_pos(), 2)
        if penguin.getFlung():
            penguin.move()
        penguin.render()

    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()