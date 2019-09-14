# RNG for which column
# RNG for spawn rate
from Note import Note


class Column:
    def __init__(self, center, app):
        self.app = app
        self.center = center
        self.notes = []

    def move(self):
        for note in self.notes:
            if note.ypos > self.app.height:
                self.notes.remove(note)
            else:
                note.move()

    def newNote(self):
        note = Note(self.app, self.center)
        self.notes.append(note)
        