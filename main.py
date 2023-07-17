import numpy
import matplotlib.pyplot as plot
from tkinter import *
import random

def calculateScore(guess, probability):
    out = ""
    output.delete(0.0, END)
    score = 100
    score -= (abs(int(guess) - probability))
    return score

def click():
    guess = user_guess.get()
    output.insert(END, calculateScore(guess, probability))

def coinToss():
    rng = random.randint(1, 20)
    if (rng % 4 == 0):
        fair = True
    else:
        fair = False
    if not fair:
        rng = random.randint(1, 20)
        if (rng % 2 == 0):
            range_lower = True
        else:
            range_lower = False
        if not range_lower:
            probability = random.randint(60, 80)
        else:
            probability = random.randint(20, 40)
    else:
        probability = 50
    
    heads_dist = numpy.array(0)
    heads = 0
    for i in range(1,1000):
        for j in range(1,30):
            comparison = random.randint(1, 100)
            if comparison <= probability:
                heads += 1
        heads_dist = numpy.insert(heads_dist, 0, heads)
        heads = 0

    plot.hist(heads_dist, color='lightgreen', ec='black', range=(0,30))
    plot.savefig("plot.png")

    return probability


#seed rng
random.seed()
#configure window
window = Tk()
window.title("Coin toss guessing game")
window.resizable(1,1)
#preliminary GUI text
Label(window, text = "I am going to generate a plot for you. It is a plot of the # of times a coin landed on heads in my trials. I may or may not decide to be fair with you. Guess what my probability of landing on heads is.", font = "none 18", wraplength=650, justify="left").grid(row = 0, column = 0, sticky = W)
#plot histogram
probability = coinToss()
plot = PhotoImage(file="plot.png")
plot_label = Label(window, image = plot)
plot_label.grid(row = 1, column = 0, sticky = W)
#user input section
Label(window, text="Your guess (integer 1 to 100): ", font="none 16").grid(row = 2, column = 0, sticky = W)
user_guess = Entry(window, width = 5)
user_guess.grid(row = 3, column = 0, sticky = W)
Button(window, command = click, text = "Submit guess").grid(row = 4, column = 0, sticky = W)
#score section
Label(window, text="I will tell you your score based on how close your guess was to my actual probability. 100 = spot on.", font = "none 18", justify="left", wraplength="650").grid(row = 5, column = 0, sticky = W)
Label(window, text="Your score is:", font="none 16").grid(row = 6, column = 0, sticky = W)
output = Text(window, width = 5, height = 2)
output.grid(row = 7, column = 0, sticky = W)
#init
window.mainloop()

