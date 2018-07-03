# -*- coding: utf-8 -*-
# !/usr/bin/env python

import pygame
import sys
import math

pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
plotPoints = []
for x in range(0, 640):
	y = int(math.sin(x/640.0 * 4 * math.pi) * 200 + 240)
	plotPoints.append([x, y])
pygame.draw.lines(screen, [0, 0, 0], False, plotPoints, 1)


while True:
	pygame.display.flip()
	pygame.time.delay(30)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	