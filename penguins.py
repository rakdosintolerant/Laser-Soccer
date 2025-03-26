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
collided = False

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
        self.mass = 1
    
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
    
    def getMass(self):
        return self.mass
    
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

# Function to check and resolve collisions
def check_collision(peng1, peng2):
        rect1 = peng1.getRectangle()
        rect2 = peng2.getRectangle()
    # Check if rectangles are colliding
        # Calculate overlap in both axes
        overlap_x = min(rect1.right - rect2.left, rect2.right - rect1.left)
        overlap_y = min(rect1.bottom - rect2.top, rect2.bottom - rect1.top)
        
        # Determine the axis of least penetration
        if overlap_x < overlap_y:
            # Horizontal collision
            if rect1.centerx < rect2.centerx:
                # Rect1 is to the left of rect2
                rect1.x = rect2.left - rect1.width
            else:
                # Rect1 is to the right of rect2
                rect1.x = rect2.right
            
            # Calculate velocities along the collision normal
            v1 = peng1.getMove()[0]
            v2 = peng2.getMove()[0]
            
            # Calculate new velocities using conservation of momentum and energy
            new_v1 = (.9 * peng2.getMass() * (v2 - v1) + peng1.getMass() * v1 + peng2.getMass() * v2) / (peng1.getMass() + peng2.getMass())
            new_v2 = (.9 * peng1.getMass() * (v1 - v2) + peng1.getMass() * v1 + peng2.getMass() * v2) / (peng1.getMass() + peng2.getMass())

            peng1.setMove([new_v1, peng1.getMove()[1]])
            peng2.setMove([new_v2, peng2.getMove()[1]])
            #rect1.vel_x = new_v1
            #rect2.vel_x = new_v2
            
        else:
            # Vertical collision
            if rect1.centery < rect2.centery:
                # Rect1 is above rect2
                rect1.y = rect2.top - rect1.height
            else:
                # Rect1 is below rect2
                rect1.y = rect2.bottom
            
            # Calculate velocities along the collision normal
            v1 = peng1.getMove()[1]
            v2 = peng2.getMove()[1]
            
            # Calculate new velocities using conservation of momentum and energy
            new_v1 = (.9 * peng2.getMass() * (v2 - v1) + peng1.getMass() * v1 + peng2.getMass() * v2) / (peng1.getMass() + peng2.getMass())
            new_v2 = (.9 * peng1.getMass() * (v1 - v2) + peng1.getMass() * v1 + peng2.getMass() * v2) / (peng1.getMass() + peng2.getMass())
            
            peng1.setMove([peng1.getMove()[0], new_v1])
            peng2.setMove([peng2.getMove()[0], new_v2])
            #rect1.vel_y = new_v1
            #rect2.vel_y = new_v2

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

    for penguin in penguins:
        for otherPenguin in penguins:
            if penguin.getRectangle().colliderect(otherPenguin.getRectangle()) and penguin.id != otherPenguin.id:
                check_collision(penguin, otherPenguin)
                
        #penguin1.setMove([penguin1.getMove()[0] + penguin2.getMove()[0], penguin1.getMove()[1] + penguin2.getMove()[1]])
        #penguin2.setMove([penguin2.getMove()[0] - penguin1.getMove()[0], penguin2.getMove()[1] - penguin1.getMove()[1]])
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