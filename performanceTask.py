#imports
import random
import time
import os
#variables
deck = []
playerHand = []
playersPrint = []
playerBalance = 500
currBet = 0
playerBet = 0
opps = []
action = ""
currOpps = []
board = []
pot = 0
gameOn = True
playing = True
winner = 1
names = ["Bernie Sanders", "Winston Churchill", "What's a Father", "Cheickna Traore", "Joe Rogan", "XXXTentacion", "Player 456", "Seong Gi-Hun", "James Charles", "Elon Musk", "El Kuhn", "Lil Colfax", "Pink Floyd", "John Wilkes Boothe", "John Locke", "Yeezy", "Haley Welch", "Mahatma Ghandi", "Mike Tyson", "Donald Trump", "Joe Biden", "Kamala Harris", "Ben Shapiro", "Barack Obama", "Omar Hussaini", "Peter Hum", "Luh Cas", "George Washington", "Stevie Wonder", "Michael Jackson", "Drake", "Kanye West", "Anthony Fauci", "Dream", "Ninja w/out a low taper fade", "Ninja w/ a low taper fade", "Chopped Chin", "I bought a property in Egypt", "Patrick Sasser", "Rosa Parks", "Lizzo", "Martin Luther King Jr.", "Frank Sinatra", "Logan Paul and Jake Paul", "Kendrick L. Duckworth", "Kurt Cobain", "OJ Simpson", "Courtney Love", "Patrick Mahomes", "The Denver Broncos", "Michelle Obama", "Pennywise the Clown", "DJ Khaled"]
#classes and functions
class opponent:
    def __init__(self, numOpp):
        self.name = random.choice(names)
        names.pop(names.index(self.name))
        self.numOpp = numOpp
        self.hand = []
        self.balance = 500
        self.type = random.choice([0, 1, 2, 3])
        self.betRn = 0
        self.action = ""
        self.handRevealed = False
    def reset(self):
        self.hand = []
        self.betRn = 0
        self.action = ""
        self.handRevealed = False
    def getnumAI(self):
        return self.numOpp
    def __str__(self):
        if self.betRn > 0:
            if self.handRevealed: return self.getNameAndBalance() + f" ({self.betRn}) " + " ".join(self.hand)
            return self.getNameAndBalance() + f" ({self.betRn})"
        if self.handRevealed: return self.getNameAndBalance() + " ".join(self.hand)
        return self.getNameAndBalance()
    def getNameAndBalance(self):
        return self.name + f" ({self.balance})"
    def dealHand(self, deck):
        self.hand.append(deck.pop())
        self.hand.append(deck.pop())
    def revealHand(self):
        self.handRevealed = True
        return f"{self.name} has {self.hand[0]} {self.hand[1]}" 
    def getHand(self):
        return self.hand
    def getType(self):
        return self.type
    def getBalance(self):
        return self.balance
    def getName(self):
        return self.name
    def getBet(self):
        return self.betRn
    def getAction(self):
        return self.action
    def addBalance(self, winnings):
        self.balance += winnings
        print(self.name, f"wins a pot of {winnings} with a {calcHand(self.hand)[0]}! They now have {self.balance}.")
    def removeBalance(self, losings):
        self.balance -= losings
    def bet(self, currBet):
        #self.setBetAndAction(["call", currBet])
        #return
        chance = 18
        rating = rateHand(self.getHand())
        fear = currBet / self.getBalance()
        if self.getType() == 0:
            rating *= 2
            fear /= 2
            chance += 1
        elif self.getType() == 1:
            rating -= 4
            fear * 1.1
        elif self.getType() == 2:
            rating *= 3
            fear += 1
        elif self.getType() == 3:
            chance = 2
        choice = random.randint(0, chance) > 1
        if rating > 20:
            if choice: self.setBetAndAction(["call", currBet])
            elif self.balance > currBet: self.setBetAndAction(["raise", currBet + (self.getBalance() // 3 // random.randint(6, chance+6))])
            else: self.setBetAndAction(["fold", self.betRn])
        elif rating < 5:
            if choice: self.setBetAndAction(["fold", 0])
            elif random.randint(0, chance) > 0: self.setBetAndAction(["call", currBet])
            elif self.balance > currBet: self.setBetAndAction(["raise", currBet + (self.getBalance() // 6 // (4*random.randint(6, chance+6)))])
            else: self.setBetAndAction(["fold", self.betRn])
        else:
            if fear > 1:
                if choice: self.setBetAndAction(["fold", 0])
                elif random.randint(0, chance) > 0: self.setBetAndAction(["call", currBet])
                elif self.balance > currBet: self.setBetAndAction(["raise", (self.getBalance() // 6 // (4*random.randint(6, chance+6)))])
                else: self.setBetAndAction(["fold", self.betRn])
            elif fear < 0.1:
                if choice: self.setBetAndAction(["call", currBet])
                elif random.randint(0, chance) > 0 and self.balance > currBet: self.setBetAndAction(["raise", currBet + (self.getBalance() // 4 // (2*random.randint(6, chance+6)))])
                else: self.setBetAndAction(["fold", self.betRn])
            else:
                if choice: self.setBetAndAction(["call", currBet])
                elif random.randint(0, chance) > 0 and self.balance > currBet: self.setBetAndAction(["raise", currBet + (self.getBalance() // 4 // (2*random.randint(6, chance+6)))])
                else: self.setBetAndAction(["fold", self.betRn])
    def setBetAndAction(self, actions):
        self.action = actions[0]
        self.betRn = actions[1]
    def actionToString(self):
        if self.action == "raise":
            return self.getNameAndBalance() + " raises to " + str(self.betRn) + "!"
        if self.action == "call": return self.getNameAndBalance() + " calls for " + str(self.betRn) + "!"
        return self.getNameAndBalance() + " folds!"

def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

def makeDeck():
    deck = []
    suits = ["♠", "♥", "♦", "♣"]
    nums = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    #nums = ["2", "3", "4", "5", "6", "6", "8", "9", "T", "J", "Q", "K", "A"]
    for i in suits:
        for n in nums: deck.append(n + i)
    random.shuffle(deck)
    return deck

def flop():
    global board
    global deck
    for i in [0, 1, 2]: board.append(deck.pop())
    #board.append("2♣")
    #board.append("3♣")
    #board.append("4♣")
    print("Flop!")
    time.sleep(1)
    print("BOARD: ", board[0], board[1], board[2])

def turn():
    global board
    global deck
    board.append(deck.pop())
    #board.append("5♣")
    print("Turn!")
    time.sleep(1)
    print("BOARD: ", board[0], board[1], board[2], board[3])
    
def river():
    global board
    global deck
    board.append(deck.pop())
    #board.append("6♣")
    print("River!")
    time.sleep(1)
    print("BOARD: ", board[0], board[1], board[2], board[3], board[4])

def whoWins():
    global currOpps, playerHand, playing
    input()
    winners = [False, False]
    winners.pop()
    if playing:
        bestHand = playerHand
    else:
        bestHand = False
    for i in currOpps:
        print("the handvshand is ", handVsHand(i.getHand(), bestHand))
        if not handVsHand(i.getHand(), bestHand):
            winners.append(i)
        else: 
            bestHand = handVsHand(i.getHand(), bestHand)
            if i.getHand() == bestHand: winners = [i]
    if (winners[0]) or (len(winners) > 1): return winners
    return False

def handVsHand(hand1, hand2):
    global board
    if not hand2: return hand1
    print("hand 1,", hand1, "hand 2,", hand2)
    numsDict = {"2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9, "T" : 10, "J" : 11, "Q" : 12, "K" : 13, "A" : 14}
    numsDict2 = {2 : "2", 3 : "3", 4 : "4", 5 : "5", 6 : "6", 7 : "7", 8 : "8", 9 : "9", 10 : "T", 11 : "J", 12 : "Q", 13 : "K", 14 : "A"}
    if rateHandonBoard(calcHand(hand1), calcHand(hand2)): 
            if rateHandonBoard(calcHand(hand1), calcHand(hand2)) == calcHand(hand1): return hand1
            return hand2
    fullHand1 = hand1.copy()
    fullHand2 = hand2.copy()
    for i in board:
        fullHand1.append(i)
        fullHand2.append(i)
    while len(fullHand1) > 2:
        numsInFullHand1 = []
        numsInFullHand2 = []
        for i in fullHand1: 
            numsInFullHand1.append(numsDict[i[0]])
        print("fullHand1: ", fullHand1, "numsInFullHand1: ", numsInFullHand1)
        for i in fullHand2:
            numsInFullHand2.append(numsDict[i[0]])
        print("fullHand2: ", fullHand2, "numsInFullHand2: ", numsInFullHand2)
        tiedHand = calcHand(hand1)
        if tiedHand[0] == "high card":
            fullHand1.pop(numsInFullHand1.index(tiedHand[1]))
            fullHand2.pop(numsInFullHand2.index(tiedHand[1]))
        elif tiedHand[0] == "pair":
            for i in [0, 1]:
                fullHand1.pop(numsInFullHand1.index(tiedHand[1]))
                fullHand2.pop(numsInFullHand2.index(tiedHand[1]))
        elif tiedHand[0] == "two pair":
            for i in [0, 1]:
                fullHand1.pop(numsInFullHand1.index(tiedHand[1]))
                fullHand2.pop(numsInFullHand2.index(tiedHand[1]))
        elif tiedHand[0] == "three of a kind":
            for i in [0, 1, 2]:
                fullHand1.pop(numsInFullHand1.index(tiedHand[1]))
                fullHand2.pop(numsInFullHand2.index(tiedHand[1]))
        elif tiedHand[0] == "full house":
            for i in [0, 1, 2]:
                fullHand1.pop(numsInFullHand1.index(tiedHand[1]))
                fullHand2.pop(numsInFullHand2.index(tiedHand[1]))
        elif tiedHand[0] == "four of a kind":
            for i in [0, 1, 2, 3]:
                fullHand1.pop(numsInFullHand1.index(tiedHand[1]))
                fullHand2.pop(numsInFullHand2.index(tiedHand[1]))
        elif tiedHand[0] == "flush":
            fullHand1[0] = fullHand1[0][0] + "♠"
            fullHand2[0] = fullHand2[0][0] + "♠"
            fullHand1[1] = fullHand1[0][0] + "♥"
            fullHand2[1] = fullHand2[0][0] + "♥"
            fullHand1[2] = fullHand1[0][0] + "♦"
            fullHand2[2] = fullHand2[0][0] + "♦"
            fullHand1[3] = fullHand1[0][0] + "♣"
            fullHand2[3] = fullHand1[0][0] + "♣"
        elif tiedHand[0] == "straight" or tiedHand[0] == "straight flush" or tiedHand[0] == "royal flush":
            return False
        if rateHandonBoard(calcHand(hand1), calcHand(hand2)): 
            if rateHandonBoard(calcHand(hand1), calcHand(hand2)) == calcHand(hand1): return hand1
            return hand2
    return False
    


def calcHand(hand):
    global board
    if len(hand) == 2:
        totalBoard = []
        for i in board: totalBoard.append(i)
        for i in hand: totalBoard.append(i)
        print("len was 2")
    else:
        totalBoard = hand.copy()
        print("was copiued")
    print(totalBoard)
    handMine = []
    nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    suits = ["♠", "♥", "♦", "♣"]
    numsDict = {"2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9, "T" : 10, "J" : 11, "Q" : 12, "K" : 13, "A" : 14}
    handsDict = {"high card" : 0, "pair" : 1, "two pair" : 2, "three of a kind" : 3, "straight" : 4, "flush" : 5, "full house" : 6, "four of a kind" : 7, "straight flush" : 8, "royal flush" : 9}
    
    numsInBoard = []
    suitsInBoard = []
    for i in totalBoard: 
        numsInBoard.append(numsDict[i[0]])
        suitsInBoard.append(i[1])
    for i in nums:
        if numsInBoard.count(i) == 2: handMine.append(["pair", i])
        elif numsInBoard.count(i) == 3: handMine.append(["three of a kind", i])
        elif numsInBoard.count(i) == 4: handMine.append(["four of a kind", i])
    straightC = 0
    for i in numsInBoard:
        straightC = 0
        x = 0
        rightSuit = ["unassigned", 0]
        for n in range(i, i+5):
            if n in numsInBoard:
                straightC += 1
                x = n
                if rightSuit[0] == "unnasigned" or rightSuit[0] == suitsInBoard[numsInBoard.index(n)]: 
                    rightSuit[0] = suitsInBoard[numsInBoard.index(n)]
                    rightSuit[1] += 1
        if straightC == 5 and rightSuit[1] == 5 and x == 14: handMine.append(["royal flush", x])
        elif straightC == 5 and rightSuit[1] == 5: handMine.append(["straight flush", x])
        elif straightC == 5: handMine.append(["straight", x])
    for i in suits:
        if suitsInBoard.count(i) >= 5: handMine.append(["flush", i])
    if handMine:
        check = []
        for i in handMine: check.append(i[0])
        if "three of a kind" in check and "pair" in check: handMine.append(["full house", handMine[check.index("three of a kind")][1]])
        if check.count("pair") >= 2:
            if handMine[check.index("pair")][1] > handMine[check.index("pair", check.index("pair")+1)][1]:
                handMine.append(["two pair", handMine[check.index("pair")][1]])
            else:
                handMine.append(["two pair", handMine[check.index("pair", check.index("pair")+1)][1]])
    if not handMine:
        best = 0
        for i in numsInBoard:
            if i > best: best = i
        handMine.append(["high card", best])
    bestHand = ["high card", 2]
    for i in handMine:
        if handsDict[i[0]] > handsDict[bestHand[0]]: 
            bestHand = i
        elif handsDict[i[0]] == handsDict[bestHand[0]] and i[0] != "flush" and i[1] > bestHand[1]: bestHand = i
    return bestHand

def rateHandonBoard(hand1, hand2):
    handsDict = {"high card" : 0, "pair" : 1, "two pair" : 2, "three of a kind" : 3, "straight" : 4, "flush" : 5, "full house" : 6, "four of a kind" : 7, "straight flush" : 8, "royal flush" : 9}

    if handsDict[hand1[0]] > handsDict[hand2[0]]:
        return hand1
    elif handsDict[hand1[0]] < handsDict[hand2[0]]:
        return hand2
    elif hand1[0] != "flush":
        if hand1[1] > hand2[1]: return hand1
        elif hand2[1] > hand1[1]: return hand2
        else: return False
    else: return False

def playerBetting():
    global action, playerBet, currBet, playerHand, playerBalance, pot, currOpps
    while True:
        printPlayers()
        print(playerHand)
        action = input("Press R to raise, C to check/call, or F to fold.")
        while action != "R" and action != "C" and action != "F":
            action = input("That was not a valid action.")
        if action == "R":
            playerBet = playerRaise()
            if playerBet: break
        if action == "C":
            playerBet = currBet
            if currBet == 0: 
                print("You checked.")
            else:
                print(f"You called a bet of {currBet}.")
            break
        if action == "F":
            print("You folded.")
            break
    playerBet = int(playerBet)
    if action == "R": currBet = playerBet
    playerBalance -= playerBet
    pot += playerBet

def playerRaise():
    global playerBalance
    bet = input(f"You have ${playerBalance}. How much would you like to raise?")
    if isInt(bet):
        if not bet == "0":
            if int(bet) <= playerBalance:
                if int(bet) > currBet: return bet
                else: print("You must add to the bet of the player before you.")
            else: print("You can't bet more than you have.")
        else: print("You can't bet nothing.")
    else: print("You need to bet a numeric value.")
    return False

def isInt(num):
    try:
        int(num)
        return True
    except ValueError: return False

def rateHand(hand):
    cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    rating = 0
    rating += cards.index(hand[0][0])
    rating += cards.index(hand[1][0])
    if hand[0][0] == hand[1][0]: rating *= 2
    if hand[0][1] == hand[1][1]: rating += 6
    if cards.index(hand[0][0]) + 1 == cards.index(hand[1][0]): rating += 8
    elif cards.index(hand[0][0]) - 1 == cards.index(hand[1][0]): rating += 6
    elif cards.index(hand[0][0]) + 2 == cards.index(hand[1][0]): rating += 4
    elif cards.index(hand[0][0]) - 2 == cards.index(hand[1][0]): rating += 4
    elif cards.index(hand[0][0]) + 3 == cards.index(hand[1][0]): rating += 2
    elif cards.index(hand[0][0]) - 3 == cards.index(hand[1][0]): rating += 2
    return rating

def printPlayers():
    clear_screen()
    global playersPrint, board, pot, currBet, playerHand, playerBalance
    for i in playersPrint: print(i)
    if board: print("BOARD: ", board)
    else: print("BOARD is empty")
    print("POT: ", pot)
    print("CURRENT BET: ", currBet)
    print("YOUR HAND: ", playerHand)
    print("YOUR BALANCE: ", playerBalance)
    time.sleep(0.1)

def roundOfBetting():
    global currBet, action, currOpps, opps, playerBet, pot, gameOn, winner, playing
    if playing:
        playerBetting()
        if action == "F": playing = False
    for i in opps:
        if i in currOpps:
            i.bet(currBet)
            if i.getBet() > currBet: currBet = i.getBet()
            playersPrint[currOpps.index(i)] = (i.actionToString(), i.getHand())
            printPlayers()
            if i.getAction() == "fold": 
                pot += i.getBet()
                currOpps.pop(currOpps.index(i))
            resetPlayersPrint()
    while True:
        checkBets = 0
        for r in currOpps:
            if r.getBet() != currBet: checkBets = 1
            if playing: 
                if playerBet != currBet: checkBets = 1
        if checkBets == 0: break
        if playing:
            playerBetting()
            if action == "F": playing = False
        for i in opps:
            checkBets = 0
            for r in currOpps:
                if r.getBet() != currBet: checkBets = 1
            if playing:
                if playerBet != currBet: checkBets = 1
            if checkBets == 0: break
            if i in currOpps:
                i.bet(currBet)
                if i.getBet() > currBet: currBet = i.getBet()
                playersPrint[currOpps.index(i)] = (i.actionToString(), i.getHand())
                printPlayers()
                if i.getAction() == "fold": 
                    pot += i.getBet()
                    currOpps.pop(currOpps.index(i))
                resetPlayersPrint()
        checkBets = 0
        if len(currOpps) == 0:
            gameOn = False
            winner = False
            break
        elif len(currOpps) == 1 and playing == False:
            gameOn = False
            winner = currOpps[0]
            break
        for r in currOpps:
            if r.getBet() != currBet: checkBets = 1
        if playing:
            if playerBet != currBet: checkBets = 1
        if checkBets == 0: break

def resetPlayersPrint():
    global playersPrint
    global currOpps
    playersPrint = []
    for i in currOpps:
        playersPrint.append(str(i))

def resetBets():
    global currOpps, gameOn, winner, playerBalance, pot, currBet
    for i in currOpps:
        pot += i.getBet()
        i.removeBalance(i.getBet())
        i.setBetAndAction(["call", 0])
    if not gameOn:
        if not winner:
            playerBalance += pot
        else:
            i.addBalance(pot)
    currBet = 0

def round():
    global currOpps, deck, playerHand, pot, playerBalance, currBet, playerBet, action, board, gameOn, playing, playersPrint
    deck = []
    playerHand = []
    playersPrint = []
    currBet = 0
    playerBet = 0
    action = ""
    currOpps = []
    board = []
    pot = 0
    gameOn = True
    playing = True
    deck = makeDeck()
    playerHand.append(deck.pop())
    playerHand.append(deck.pop())
    for i in opps:
        i.reset()
        i.dealHand(deck)
        currOpps.append(i)

    resetPlayersPrint()

    roundOfBetting()

    resetBets()

    resetPlayersPrint()
        
    flop()

    roundOfBetting()

    resetBets()

    resetPlayersPrint()

    turn()

    roundOfBetting()

    resetBets()

    resetPlayersPrint()

    river()

    roundOfBetting()

    resetBets()

    resetPlayersPrint()

    for i in currOpps:
        playersPrint[currOpps.index(i)] = i.revealHand()
        printPlayers()
        resetPlayersPrint()

    winner = whoWins()
    pot = pot // len(winner)
    if len(winner) > 1:
        print("There is a split pot because of a tie!")
        for i in winner:
            if i:
                i.addBalance(pot)
            else: 
                playerBalance += pot
                print(f"You win ${pot} with a {calcHand(playerHand)[0]}! You now have {playerBalance}.")
    elif winner:
        winner[0].addBalance(pot)
    else:
        playerBalance += pot
        print(f"You win ${pot} with a {calcHand(playerHand)[0]}! You now have {playerBalance}.")
    input()

for i in range(7):
    opps.append(opponent(i))
while playerBalance > 0: round()