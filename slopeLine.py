def makeLine(penguin, ball):
                    try:
                        #slope = (ball.getRectangle().centery - penguin.getRectangle().centery) / (ball.getRectangle().centerx - penguin.getRectangle().centerx)
                        slope = (penguin.getRectangle().centery - ball.getRectangle().centery) / (penguin.getRectangle().centerx - ball.getRectangle().centerx)

                        lineEndPoint = (slope * (0 - penguin.getRectangle().centerx)) + penguin.getRectangle().centery
                        lineStartPoint = (slope * (1000 - penguin.getRectangle().centerx)) + penguin.getRectangle().centery
                        line = [[1000, lineStartPoint], [0, lineEndPoint]]
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
                slope = 9999
        else: slope -9999

        return slope
