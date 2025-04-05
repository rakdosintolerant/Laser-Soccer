import constants
def resolveCollision(peng1, peng2):
        rect1 = peng1.getRectangle()
        try:
            rect2 = peng2.getRectangle()
            wall = False
        except:
            rect2 = peng2
            wall = True

        if not rect1.colliderect(rect2):
            return
        # Calculate overlap in both axes
        overlap_x = min(rect1.right - rect2.left, rect2.right - rect1.left)
        overlap_y = min(rect1.bottom - rect2.top, rect2.bottom - rect1.top)
        
        if True:
            if overlap_x < overlap_y:
                # Horizontal collision
                if rect1.centerx < rect2.centerx:
                    # Rect1 is to the left of rect2
                    rect1.x = rect2.left - rect1.width
                    if wall and (peng1.getMove()[0] <= 0): 
                        return
                else:
                    # Rect1 is to the right of rect2
                    rect1.x = rect2.right
                    if wall and (peng1.getMove()[0] >= 0): 
                        return
            else:
                # Vertical collision
                if rect1.centery < rect2.centery:
                    # Rect1 is above rect2
                    rect1.y = rect2.top - rect1.height
                    if wall and (peng1.getMove()[1] <= 0): 
                        return
                else:
                    # Rect1 is below rect2
                    rect1.y = rect2.bottom  
                    if wall and (peng1.getMove()[1] >= 0): 
                        return

            new_v1 = 0
            # Calculate velocities along the collision normal
            v1 = peng1.getMove()[0]
            if wall: v2 = 0
            else: v2 = peng2.getMove()[0]
            
            # Calculate new velocities using conservation of momentum and energy
            if wall:
                if rect2.width == constants.wallThickness:
                    new_v1 = (constants.elasticity * constants.wallMass * (v2 - v1) + peng1.getMass() * v1 + constants.wallMass * v2) / (peng1.getMass() + constants.wallMass)
                else: new_v1 = -(constants.elasticity * constants.wallMass * (v2 - v1) + peng1.getMass() * v1 + constants.wallMass * v2) / (peng1.getMass() + constants.wallMass)
            else:
                new_v1 = (constants.elasticity * peng2.getMass() * (v2 - v1) + peng1.getMass() * v1 + peng2.getMass() * v2) / (peng1.getMass() + peng2.getMass())
                new_v2 = (constants.elasticity * peng1.getMass() * (v1 - v2) + peng1.getMass() * v1 + peng2.getMass() * v2) / (peng1.getMass() + peng2.getMass())

            peng1.setMove([new_v1, peng1.getMove()[1]])
            if not wall: peng2.setMove([new_v2, peng2.getMove()[1]])
            
            # Calculate velocities along the collision normal
            v1 = peng1.getMove()[1]
            if wall: v2 = 0
            else: v2 = peng2.getMove()[1]
            
            # Calculate new velocities using conservation of momentum and energy
            if wall:
                if rect2.height == constants.netHeight:
                    new_v1 = (constants.elasticity * constants.wallMass * (v2 - v1) + peng1.getMass() * v1 + constants.wallMass * v2) / (peng1.getMass() + constants.wallMass)
                else: new_v1 = -(constants.elasticity * constants.wallMass * (v2 - v1) + peng1.getMass() * v1 + constants.wallMass * v2) / (peng1.getMass() + constants.wallMass)
            else:
                new_v1 = (constants.elasticity * peng2.getMass() * (v2 - v1) + peng1.getMass() * v1 + peng2.getMass() * v2) / (peng1.getMass() + peng2.getMass())
                new_v2 = (constants.elasticity * peng1.getMass() * (v1 - v2) + peng1.getMass() * v1 + peng2.getMass() * v2) / (peng1.getMass() + peng2.getMass())

            peng1.setMove([peng1.getMove()[0], new_v1])
            if not wall: peng2.setMove([peng2.getMove()[0], new_v2])

            # Determine the axis of least penetration
            # if wall:
            #     if rect2.y == constants.screenYSize: peng1.setMove([-v1, peng1.getMove()[1]])
            #     else: peng1.setMove([peng1.getMove()[0], -v2])      



def resolveNetCollision(peng1, post1, postSpeed):
        rect1 = peng1.getRectangle()
        rect2 = post1

        if not rect1.colliderect(rect2): return "noTurn"
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
            v2 = postSpeed
            
            # Calculate new velocities using conservation of momentum and energy
            new_v1 = (constants.elasticity * constants.postMass * (v2 - v1) + peng1.getMass() * v1 + constants.postMass * v2) / (peng1.getMass() + constants.postMass)
            new_v2 = (constants.elasticity * peng1.getMass() * (v1 - v2) + peng1.getMass() * v1 + constants.postMass * v2) / (peng1.getMass() + constants.postMass)

            if rect1.y > constants.screenYSize / 2: peng1.setMove([new_v1, peng1.getMove()[1] - 5])
            else: peng1.setMove([new_v1, peng1.getMove()[1] + 5])
            return new_v2
            
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
            v2 = 0
            
            # Calculate new velocities using conservation of momentum and energy
            new_v1 = (constants.elasticity * constants.postMass * (v2 - v1) + peng1.getMass() * v1 + constants.postMass * v2) / (peng1.getMass() + constants.postMass)
            new_v2 = (constants.elasticity * peng1.getMass() * (v1 - v2) + peng1.getMass() * v1 + constants.postMass * v2) / (peng1.getMass() + constants.postMass)
            
            peng1.setMove([peng1.getMove()[0], new_v1])
            return "noTurn"