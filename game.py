import math
import pygame
import numpy as np

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

WIDTH = 300
HEIGHT = 300

class CartGameAI():
	def __init__(self):
		self.n_games = 0
		self.gamme = 0.9
		self.max_epsilon = 80
		self.x = WIDTH/2
		self.v = 0
		self.ff = 0.9
		self.coord_x = np.linspace(0, WIDTH, num=50)
		self.curve = lambda x: HEIGHT/2*(1 + math.sin((2*x/WIDTH - 1/2)*math.pi))
		self.coord_y = np.array(list(map(self.curve, self.coord_x)))
		print(self.coord_x, self.coord_y)
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
		self.clock = pygame.time.Clock()



	def play(self):
		#collect keys pressed
		events = pygame.event.get()
		action=0
		for event in events:
		    if event.type == pygame.KEYDOWN:
		        if event.key == pygame.K_LEFT:
		            action = -5
		        if event.key == pygame.K_RIGHT:
		            action = 5

		#update friction depending on direction of speed
		if self.v > 0:
			self.ff = 0.1
		elif self.v < 0:
			self.ff = -0.1
		else:
			self.ff = 0

		# update values of cart
		self.v = self.v + action -self.ff+math.sin(math.atan(HEIGHT/WIDTH*math.pi*math.cos((2*self.x/WIDTH - 1/2)*math.pi)))*5
		self.x += self.v

		#update ui
		self._update_ui()


	def reset(self):
		#restarts the game
		pass

	def _update_ui(self):

		#fill the screen white
		self.screen.fill(WHITE)
		pygame.draw.lines(self.screen, BLACK, False, list(zip(self.coord_x, self.coord_y)))
		pygame.draw.circle(self.screen, RED, (self.x, self.curve(self.x)), 3)
		pygame.display.update()
		self.clock.tick(20)

if __name__ == "__main__":
	game = CartGameAI()
	while True:
		game.play()