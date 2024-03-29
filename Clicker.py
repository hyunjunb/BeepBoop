# The thing that clicks notes when they reach the line
# WE WANT RED AND GREEN
import pygame

class Clicker:
	time = 0
	limit = 600

	def __init__(self, color, position, key, app, col):
		#red = (255, 58, 44); green = (27, 239, 104)
		#key = the button it should be mapped to
		#pygame.K_LEFT, pygame.K_RIGHT
		self.position = position
		self.key = key
		self.app = app
		self.color = color
		self.col = col
		self.clicked = False
		self.badClick = False
		
	def click(self):	
		for note in self.col.notes:
			if abs(note.ypos - self.position[1]) < 40:
				self.clicked = True
				self.time = 0
				if self.key == pygame.K_LEFT:
					pygame.mixer.music.load('beep.mp3')
					pygame.mixer.music.play(0)
				else:
					pygame.mixer.music.load('boop.mp3')
					pygame.mixer.music.play(0)
				self.col.notes.remove(note)
				break
			else:
				pygame.mixer.music.load('wait.mp3')
				pygame.mixer.music.play(0)
		if self.clicked == False:
			self.badClick = True
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
			self.badClick = False
		elif self.badClick == True:
			pygame.draw.circle(self.app._display_surf, (0,0,0), self.position, 40)
			self.time += 1
			if self.time > self.limit:
				self.badClick = False


