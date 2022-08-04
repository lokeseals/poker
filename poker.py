import random
import turtle

turtle.hideturtle()

card_val = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
suit = ["♥","♦","♠","♣"]

cards = []

for i in card_val:
    for j in suit:

        cards.append(i+j)

random.shuffle(cards)

class Card(turtle.Turtle):

    def __init__(self, card_val):
        turtle.Turtle.__init__(self, shape="square", visible=True)
        self.shapesize(5)
        self.penup()
        self.color("white")
        self.pencolor("black")
        self.card_val = card_val

        if "♥" in card_val or "♦" in card_val:
            self.pencolor("red")

    def display(self):

        self.write(self.card_val, font=("Arial", 32, "bold"), align="center")

class DealerState():

    def __init__(self):

        self.state = "Pocket"
        self.dealt = []

ds = DealerState()

def space():

    if ds.state == "Pocket":

        pocket1 = cards.pop()
        pocket2 = cards.pop()
        
        ds.dealt.append(pocket1)
        ds.dealt.append(pocket2)

        card = Card(pocket1)
        card.display()

        card2 = Card(pocket2)
        card2.goto(100,0)
        card2.display()

        ds.state = "Flop"

    elif ds.state == "Flop":

        flop1 = cards.pop()
        flop2 = cards.pop()
        flop3 = cards.pop()

        ds.dealt.append(flop1)
        ds.dealt.append(flop2)
        ds.dealt.append(flop3)

        card3 = Card(flop1)
        card3.goto(-200,200)
        card3.display()

        card4 = Card(flop2)
        card4.goto(-100,200)
        card4.display()

        card5 = Card(flop3)
        card5.goto(0,200)
        card5.display()

        ds.state = "Turn"

    elif ds.state == "Turn":

        turn = cards.pop()

        ds.dealt.append(turn)

        card4 = Card(turn)
        card4.goto(100,200)
        card4.display()

        ds.state = "River"

    elif ds.state == "River":

        river = cards.pop()

        ds.dealt.append(river)

        card5 = Card(river)
        card5.goto(200,200)
        card5.display()

        ds.state = "Shuffle"

    elif ds.state == "Shuffle":

        for i in ds.dealt:

            cards.append(i)

        random.shuffle(cards)

        ds.dealt = []

        for j in turtle.turtles():
            j.hideturtle()
            j.clear()

        turtle.turtles().clear()

        ds.state = "Pocket"

def fold():

    for i in ds.dealt:

        cards.append(i)

    random.shuffle(cards)

    ds.dealt = []

    for j in turtle.turtles():
        j.hideturtle()
        j.clear()

    turtle.turtles().clear()

    ds.state = "Pocket"
    

turtle.onkey(space,"space")
turtle.onkey(fold,"f")

turtle.listen()

turtle.mainloop()
