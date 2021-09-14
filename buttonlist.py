from graphics import *
from game import Button

def getStart(winSize):
    s_button = Button(Point(winSize/2 - 100, winSize/2 - 100), Point(winSize/2 + 100, winSize/2 + 100))
    s_button.setOutline("white")
    s_button.setFill("white")
    s_button.setText("START", 20)
    s_button.setTextColor("Black")
    return s_button
