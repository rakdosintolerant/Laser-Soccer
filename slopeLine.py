def makeLine(penguin, ball):
                    try:
                        slope = (penguin.getRectangle().centery - ball.getRectangle().centery) / (penguin.getRectangle().centerx - ball.getRectangle().centerx)

                        lineEndPoint = (slope * (0 - penguin.getRectangle().centerx)) + penguin.getRectangle().centery
                        lineStartPoint = (slope * (5000 - penguin.getRectangle().centerx)) + penguin.getRectangle().centery
                        line = [[5000, lineStartPoint], [0, lineEndPoint]]
                    except:
                        if ball.getRectangle().centery > penguin.getRectangle().centery:
                            lineEndPoint = ball.getRectangle().centery + 1000
                        else: lineEndPoint = ball.getRectangle().centery + 1000
                        line = [penguin.getRectangle().center, [penguin.getRectangle().centerx, lineEndPoint]]
                    return line

def getSlope(penguin, ball):
        try:
            slope = (penguin.getRectangle().centery - ball.getRectangle().centery) / (penguin.getRectangle().centerx - ball.getRectangle().centerx)
        except:
            if ball.getRectangle().centery > penguin.getRectangle().centery:
                slope = 10
        else: slope -10

        return slope
