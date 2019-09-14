# Driver for the game
import pygame
import time
from pygame.locals import *
from Clicker import Clicker
from Column import Column
from Note import Note
 
class App:
    t = .005
    thing = 0
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 640, 400
        self.background_colour = (255,255,255)
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)      
        self._display_surf.fill((255,255,255))
        self.col = Column(int(self.width/3), self)
        self.ol = Column(int(2*self.width/3), self)   

 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.fill(self.background_colour)
        self.col.move()
        self.ol.move()
        self.leftbutton = pygame.draw.circle(self._display_surf, (255, 58, 44), (100, 100), 20)
        time.sleep(self.t)
        pygame.display.flip()
        

    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()