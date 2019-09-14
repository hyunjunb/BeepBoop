# The thing that clicks notes when they reach the line
# WE WANT RED AND GREEN
import pygame

class Clicker:
	time = 0
	limit = 30

	def __init__(self, color, position, key, app):
		#red = (255, 58, 44); green = (27, 239, 104)
		#key = the button it should be mapped to
		#pygame.K_LEFT, pygame.K_RIGHT
		self.position = position
		self.key = key
		self.app = app
		self.color = color
		self.clicked = False

	def click(self):	
		self.clicked = True
		self.time = 0
		# while True:
		# 	for event in pygame.event.get():
		# 		if event.type == pygame.QUIT:
		# 			pygame.quit()
		# 		elif event.type == pygame.KEYDOWN:
		# 			if event.key == self.key:
		# 				self.clicked = True
		# 				#button is clicked. check for overlap

	def render(self):
		self.button = pygame.draw.circle(self.app._display_surf, self.color, self.position, 40)
		if self.clicked == True:
			pygame.draw.circle(self.app._display_surf, (27, 239, 104), self.position, 40)
			self.time += 1
			if self.time > self.limit:
				self.clicked = False


