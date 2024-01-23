import sys
from math import cos, radians, sin
from random import randint as r
from time import sleep as w
from time import time as t

import pygame
from pygame.color import THECOLORS as col

pygame.init()
global screen
screen = pygame.display.set_mode((1000, 600)) #Screen size
pygame.display.set_caption('ROCKET SCIENCE!')  #Title

font = pygame.font.SysFont('couriernew', 20) #Font

scene = 1

fuel = 0 # Fuel
mass = 0 # dry mass
isp = 0  # ISP
maxQ = 0 # maximum fuel consumption
q = 0    # fuel consumption
thr = 0  # throttle

rocket = [] # rocket parts

while True:
  while scene == 1: # VAB (Vertical Assembly Building)
    screen.fill(col["blue"])
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          scene = 2
     
    pass
   
    text = font.render("Building a rocket", True, col["black"])
    screen.blit(text,(100,10))

    pygame.display.flip()
    w(0.1)

  while scene == 2: # Flight
    screen.fill(col["blue"])
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          scene = 1
				if event.key == pygame.K_z:
					if throttle > 0:
						throttle -= 10
				if event.key == pygame.K_x:
					if throttle < 100:
						throttle += 10

    pass

    text = font.render("Fuel: "+str(fuel), True, col["black"])
    screen.blit(text,(100,10))
		text = font.render("Throttle: "+str(throttle)+"%"), True, col["black"])
    screen.blit(text,(100,10))


    pygame.display.flip()
		w(0.1)
