# handles the note generate for the two columns

import pygame
from Column import Column
from Note import Note
import random


class TwoCols:
    thing = 0
    nextTime = 0
    def __init__(self, app):
        self.app = app
        self.col1 = Column(int(self.app.width/3), self.app)
        self.col2 = Column(int(2*self.app.width/3), self.app)

    def move(self):
        self.col1.move()
        self.col2.move()
        if self.nextTime == 0:
            self.nextTime = self.thing + random.randint(50, 300)
        
        self.thing += 1
        if self.thing == self.nextTime:
            self.generateNewNotes()
            self.nextTime = 0

    def generateNewNotes(self):
        if random.randint(1,2) == 1:
            self.col1.newNote()
        else:
            self.col2.newNote()

        


