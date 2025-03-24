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

penguin = pygame.Rect(600, 300, 50, 50)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: 
            click = True
            pygame.mouse.set_pos(600, 300)
            pygame.mouse.get_rel()
        elif event.type == pygame.MOUSEBUTTONUP: 
            click = False
            movement = pygame.mouse.get_rel()
            xmove = -movement[0] / 10
            ymove = -movement[1] / 10
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    if click:
        penguin.update(600, 300, 50, 50)
        pygame.draw.rect(screen, "red", penguin)
        pygame.draw.line(screen, "green", [penguin.x, penguin.y], pygame.mouse.get_pos())
    else: 
        penguin.move_ip(xmove, ymove)
        pygame.draw.rect(screen, "blue", penguin)

    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()