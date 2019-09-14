# RNG for which column
# RNG for spawn rate
from Note import Note


class Column:
    def __init__(self, center, app):
        self.app = app
        self.center = center
        self.notes = []
        note = Note(self.app, self.center)
        self.notes.append(note)

    def move(self):
        for note in self.notes:
            note.move()

    def newNote(self):
        note = Note(self.app, self.center)
        self.notes.append(note)
        