# The thing that clicks notes when they reach the line
# WE WANT RED AND GREEN
import pygame

class Clicker:

	def __init__(self, color, position, key, app):
		#red = (255, 58, 44); green = (27, 239, 104)
		#key = the button it should be mapped to
		#pygame.K_LEFT, pygame.K_RIGHT
		self.position = position
		self.key = key
		self.app = app
		self.color = color

	def click(self):
		self.button = pygame.draw.circle(self.app._display_surf, self.color, self.position, 20)
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit();
				elif event.type == pygame.KEYDOWN:
					if event.key == self.key:
						pygame.draw.circle(screen, (27, 239, 104), position, 40)
						#button is clicked. check for overlap