import pygame, constants
from penguins import penguin

# pygame setup
pygame.init()
screen = pygame.display.set_mode((constants.screenXSize, constants.screenYSize))
clock = pygame.time.Clock()

#variables (should try to have as few of these possible, it's bad practice)
running = True
click = False
spacePressed = False

#functions
def resetPenguins(): #returns all penguins to starting position and manner
    for penguin in penguins:
        penguin.reset()

def resolve_collision(peng1, peng2):
        rect1 = peng1.getRectangle()
        rect2 = peng2.getRectangle()
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
            new_v1 = (constants.elasticity * peng2.getMass() * (v2 - v1) + peng1.getMass() * v1 + peng2.getMass() * v2) / (peng1.getMass() + peng2.getMass())
            new_v2 = (constants.elasticity * peng1.getMass() * (v1 - v2) + peng1.getMass() * v1 + peng2.getMass() * v2) / (peng1.getMass() + peng2.getMass())

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
            new_v1 = (constants.elasticity * peng2.getMass() * (v2 - v1) + peng1.getMass() * v1 + peng2.getMass() * v2) / (peng1.getMass() + peng2.getMass())
            new_v2 = (constants.elasticity * peng1.getMass() * (v1 - v2) + peng1.getMass() * v1 + peng2.getMass() * v2) / (peng1.getMass() + peng2.getMass())
            
            peng1.setMove([peng1.getMove()[0], new_v1])
            peng2.setMove([peng2.getMove()[0], new_v2])

#initializing penguins/other objects
penguin1 = penguin(pygame.Rect(600, 300, constants.penguinSize, constants.penguinSize), 1, screen)
penguin2 = penguin(pygame.Rect(300, 300, constants.penguinSize, constants.penguinSize), 2, screen)
penguin3 = penguin(pygame.Rect(900, 300, constants.penguinSize, constants.penguinSize), 3, screen)
penguins = [penguin1, penguin2, penguin3]

while running:
    # poll for events
    # use events for buttons and keys and so forth
    for event in pygame.event.get():
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
        if penguin1.getFlung(): resetPenguins() #thus, space resets the penguins
        else: 
            if not click:
                for penguin in penguins: penguin.setFlung(True) #flings the penguins
        spacePressed = True
    else:
        if (not keys[pygame.K_SPACE]) and spacePressed: #if space was released, variable reflects that
            spacePressed = False

    for penguin in penguins: #checks to see if each penguin is colliding and, if so, runs the physics
        for otherPenguin in penguins:
            if penguin.getRectangle().colliderect(otherPenguin.getRectangle()) and penguin.id != otherPenguin.id:
                resolve_collision(penguin, otherPenguin)
                
    # RENDER YOUR GAME HERE
    for penguin in penguins:
        if penguin.getClicked():
            pygame.draw.line(screen, constants.lineColor, [penguin.getRectangle().centerx, penguin.getRectangle().centery], pygame.mouse.get_pos(), constants.activeLineWidth)
        if penguin.getFlung():
            penguin.move()
        penguin.render()

    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(constants.fps)  # limits FPS to 60

pygame.quit()