#   1000i Game Card
# by Mehrzad Moghaddas
#----------------------

class Card:
    suits = ['Junk', 'Club', 'Diamond', 'Heart', 'Speads', 'Joker']
    ranks = ['Junk', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace', 'Black', 'Red']

    def __init__ (self,suit=0,rank=0):
        self.suit=suit
        self.rank=rank

    def __str__ (self):
        return self.ranks[self.rank] + ' of ' + self.suits[self.suit]

    def __cmp__(self, other,blackjoker=0):
        # Joker Compare
        if self.suit==5 :
            if self.rank==14:#black joker
                return 1
            elif self.rank==15 & blackjoker==1: #red JOker
                return 1
            elif self.rank==15 & blackjoker==0: #black joker not played!
                return -1

        # compare same suit
        if self.suit==other.suit :
            if self.rank > other.rank :
                return 1

        #compare diffrent suit
        if self.suit!=other.suit & self.suit==4 : #first card's type is spades
            return 1
        elif self.suit!=other.suit & other.suit==4 : #second card's type is Spades
            return -1
        elif self.suit != 4 & other.suit!=4 :
            return 1

class Deck():
    def __str__(self):
        for card in self.cards:
            print card

    def __init__(self):
        self.cards=[]
        for suit in range(1,5):
            for rank in range (1,14):
                self.cards.append(Card(suit,rank))
        #Add Joker to Cards !
        self.cards[0]=Card(5,14)#remove 2 of clubs and add Black Joker
        self.cards[13]=Card(5,15)#remove 2 of diamonds and add RedJoker

    def shuffle(self):
        import random
        nCards=len(self.cards)
        for i in range(nCards):
            j=random.randrange(i,nCards)
            self.cards[i],self.cards[j]=self.cards[j],self.cards[i]
class Player:
    def __init__(self,name="",team=""):
        self.name=name
        self.team=team
class Team:
    pass  
class Gmae:
    def __init__(self,MAX_SCORE=1000):
        self.MAX_SCORE=MAX_SCORE
        self.ScoreA=0
        self.ScoreB=0
    def __str__(self):
        return "Team A Score= "+str(self.ScoreA)+ " Team B score= "+str(self.ScoreB)
    def GAME_OVER(self):
        if self.ScoreA>=self.MAX_SCORE or self.ScoreB>=self.MAX_SCORE :
            return 1
        else:
            return 0
    def add_Score(self,TA_Score,TB_Score):
        self.ScoreA+=TA_Score
        self.ScoreB+=TB_Score

deck=Deck()

print deck





