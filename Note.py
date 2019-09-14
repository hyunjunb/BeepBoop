# The things that fall
# WE WANT YELLOW
import pygame

class Note:

    def __init__(self, app, center):
        self.time = 0
        self.app = app
        self.ypos = 0
        self.center = center
        self.note = pygame.draw.circle(app._display_surf, (242,235,47), (center, self.ypos), 40, 0)
        
    def move(self):
        self.time += 1
        if self.time > 1:
            self.time = 0
            self.ypos += 1
        pygame.draw.circle(self.app._display_surf, (242,235,47), (self.center, self.ypos), 40, 0)