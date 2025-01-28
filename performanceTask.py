#imports
import random
import time
#variables
deck = []
playerHand = []
playerBalance = 500
currBet = 0
playerBet = 0
opps = []
action = ""
playing = True
currOpps = []
board = []
pot = 0
gameOn = True
playing = True
winner = 1
names = ["Bernie Sanders", "Winston Churchill", "Cheickna Traore", "Joe Rogan", "XXXTentacion", "Player 456", "Seong Gi-Hun", "James Charles", "Elon Musk", "El Kuhn", "Lil Colfax", "Pink Floyd", "John Wilkes Boothe", "John Locke", "Yeezy", "Haley Welch", "Mahatma Ghandi", "Mike Tyson", "Donald Trump", "Joe Biden", "Kamala Harris", "Ben Shapiro", "Barack Obama", "Omar Hussaini", "Peter Hum", "Luh Cas", "George Washington", "Stevie Wonder", "Michael Jackson", "Drake", "Kanye West", "Anthony Fauci", "Dream", "Ninja w/out a low taper fade", "Ninja w/ a low taper fade", "Chopped Chin", "I bought a property in Egypt", "Patrick Sasser", "Rosa Parks", "Lizzo", "Martin Luther King Jr.", "Frank Sinatra", "Logan Paul and Jake Paul", "Kendrick L. Duckworth", "Kurt Cobain", "OJ Simpson", "Courtney Love", "Patrick Mahomes", "The Denver Broncos", "Michelle Obama", "Pennywise the Clown", "DJ Khaled"]
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
    def getnumAI(self):
        return self.numOpp
    def dealHand(self, deck):
        self.hand.append(deck.pop())
        self.hand.append(deck.pop())
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
    def bet(self, currBet):
        chance = 5
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
            elif self.balance > currBet: self.setBetAndAction(["raise", currBet + (self.getBalance() // random.randint(6, chance+6))])
            else: self.setBetAndAction(["fold", self.betRn])
        elif rating < 5:
            if choice: self.setBetAndAction(["fold", 0])
            elif random.randint(0, chance) > 0: self.setBetAndAction(["call", currBet])
            elif self.balance > currBet: self.setBetAndAction(["raise", currBet + (self.getBalance() // (4*random.randint(6, chance+6)))])
            else: self.setBetAndAction(["fold", self.betRn])
        else:
            if fear > 1:
                if choice: self.setBetAndAction(["fold", 0])
                elif random.randint(0, chance) > 0: self.setBetAndAction(["call", currBet])
                elif self.balance > currBet: self.setBetAndAction(["raise", (self.getBalance() // (4*random.randint(6, chance+6)))])
                else: self.setBetAndAction(["fold", self.betRn])
            elif fear < 0.1:
                if choice: self.setBetAndAction(["call", currBet])
                elif random.randint(0, chance) > 0 and self.balance > currBet: self.setBetAndAction(["raise", currBet + (self.getBalance() // (2*random.randint(6, chance+6)))])
                else: self.setBetAndAction(["fold", self.betRn])
            else:
                if choice: self.setBetAndAction(["call", currBet])
                elif random.randint(0, chance) > 0 and self.balance > currBet: self.setBetAndAction(["raise", currBet + (self.getBalance() // (2*random.randint(6, chance+6)))])
                else: self.setBetAndAction(["fold", self.betRn])
    def setBetAndAction(self, actions):
        self.action = actions[0]
        self.betRn = actions[1]
    def actionToString(self):
        if self.action == "raise":
            return self.name + " raises to " + str(self.betRn) + "!"
        if self.action == "call": return self.name + " calls for " + str(self.betRn) + "!"
        return self.name + " folds!"

def makeDeck():
    deck = []
    suits = ["♠", "♥", "♦", "♣"]
    nums = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    for i in suits:
        for n in nums: deck.append(n + i)
    random.shuffle(deck)
    return deck

def flop():
    global board
    global deck
    for i in [0, 1, 2]: board.append(deck.pop())
    print("Flop!")
    time.sleep(1)
    print("BOARD: ", board[0], board[1], board[2])

def turn():
    global board
    global deck
    board.append(deck.pop())
    print("Turn!")
    time.sleep(1)
    print("BOARD: ", board[0], board[1], board[2], board[3])
    
def river():
    global board
    global deck
    board.append(deck.pop())
    print("River!")
    time.sleep(1)
    print("BOARD: ", board[0], board[1], board[2], board[3], board[4])

def whoWins():
    global currOpps
    for i in currOpps:
        calcHand(i.getHand())

def calcHand(hand):
    global board
    totalBoard = board
    handMine = []
    nums = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    suits = ["♠", "♥", "♦", "♣"]
    numsDict = {"2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9, "T" : 10, "J" : 11, "Q" : 12, "K" : 13, "A" : 14}
    handsDict = {"high card" : 0, "pair" : 1, "two pair" : 2, "three of a kind" : 3, "straight" : 4, "flush" : 5, "full house" : 6, "four of a kind" : 7, "straight flush" : 8, "royal flush" : 9}
    for i in hand: totalBoard.append[i]
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
        x = 0
        for n in range(i, i+5):
            if n in numsInBoard: 
                straightC += 1
                x = n
        if straightC == 5: handMine.append(["straight", x])
    for i in suits:
        if suitsInBoard.count(i) >= 5: handMine.append(["flush", i])
    if not handMine:
        best = 0
        for i in numsInBoard:
            if i > best: i = best
        handMine.append(["high card", best])
    bestHand = ["high card", 2]
    for i in handMine:
        if handsDict[i[0]] > handsDict[bestHand[0]]: 
            bestHand = i
        elif handsDict[i[0]] == handsDict[bestHand[0]] and i[0] != "flush" and i[1] > bestHand[1]: bestHand = i
    


    
    
    
    
    



def playerBetting():
    global action
    global playerBet
    global currBet
    global playerHand
    global playerBalance
    global pot
    while True:
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

def roundOfBetting():
    global currBet
    global action
    global currOpps
    global playerBet
    global pot
    global gameOn
    global winner
    global playing
    playerBetting()
    if action == "F": playing = False
    for i in currOpps:
        i.bet(currBet)
        if i.getBet() > currBet: currBet = i.getBet()
        if i.getAction() == "fold": 
            pot += i.getBet()
            currOpps.pop(currOpps.index(i))
        print(i.actionToString(), i.getHand())
    while True:
        checkBets = 0
        for r in currOpps:
            if r.getBet() != currBet: checkBets = 1
            if playerBet != currBet: checkBets = 1
        if checkBets == 0: break
        if playing:
            playerBetting()
            if action == "F": playing = False
        for i in currOpps:
            checkBets = 0
            for r in currOpps:
                if r.getBet() != currBet: checkBets = 1
            if playerBet != currBet: checkBets = 1
            if checkBets == 0: break
            i.bet(currBet)
            if i.getBet() > currBet: currBet = i.getBet()
            if i.getAction() == "fold": 
                pot += i.getBet()
                currOpps.pop(currOpps.index(i))
            print(i.actionToString(), i.getHand())
        checkBets = 0
        if len(currOpps) == 0:
            gameOn = False
            winner = False
        elif len(currOpps) == 1 and playing == False:
            gameOn = False
            winner = currOpps[0]
        for r in currOpps:
            if r.getBet() != currBet: checkBets = 1
        if playerBet != currBet: checkBets = 1
        if checkBets == 0: break

deck = makeDeck()
playerHand.append(deck.pop())
playerHand.append(deck.pop())
for i in range(7):
    opps.append(opponent(i))
    opps[i].dealHand(deck)
currOpps = opps

roundOfBetting()
for i in currOpps:
    pot += i.getBet()
    i.setBetAndAction(["call", 0])
if not gameOn:
    if not winner:
        playerBalance += pot
    else:
        i.addBalance(pot)
currBet = 0
flop()

roundOfBetting()

turn()

roundOfBetting()

river()

roundOfBetting()

whoWins()