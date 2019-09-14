# The things that fall
# WE WANT YELLOW
import pygame


class Note:

    def __init__(self, app, center):
        self.app = app
        self.ypos = 0
        self.center = center
        self.note = pygame.draw.circle(app._display_surf, (0,0,255), (center, 200), 40, 0)
        
    def move(self):
        pygame.draw.circle(self.app._display_surf, (0,0,255), (self.center, self.ypos), 40, 0)
        self.ypos += 1



        


