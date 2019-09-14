# Driver for the game
import pygame
import time
from pygame.locals import *
from Clicker import Clicker
from Column import Column
from Note import Note
from TwoCols import TwoCols
 
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
        self.twoCols = TwoCols(self)
        self._running = True
        self.leftbutton = Clicker((255, 58, 44),(int(self.width/3), int(5*self.height/6)), pygame.K_z, self, self.twoCols.col1)
        self.rightbutton = Clicker((255, 58, 44),(int(2*self.width/3), int(5*self.height/6)), pygame.K_z, self, self.twoCols.col2)
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.leftbutton.click()
            if event.key == pygame.K_RIGHT:
                self.rightbutton.click()
            if event.key == pygame.K_ESCAPE:
                self._running = False           

    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.fill(self.background_colour)
        self.twoCols.move()
        self.leftbutton.render()
        self.rightbutton.render()
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