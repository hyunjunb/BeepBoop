# The thing that clicks notes when they reach the line
# WE WANT RED AND GREEN
import pygame

class clicker(pygame.sprite.Sprite, color, position, key):

	def __init__(self, color, position, key):
		#red = (255, 58, 44); green = (27, 239, 104)
		#key = the button it should be mapped to
		#pygame.K_LEFT, pygame.K_RIGHT
		self.button = pygame.draw.circle(screen, color, position, 20)

	def click(self):
		while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit();
			if event.type == pygame.KEYDOWN:
				if event.key == self.key:
					pygame.draw.circle(screen, (27, 239, 104), (100, 100), 40)
					#button is clicked. check for overlap