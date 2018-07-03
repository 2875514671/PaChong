# -*- coding: utf-8 -*-
# !/usr/bin/env python

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
pygame.draw.circle(screen, [255, 0, 0], [100, 200], 30, 5)
my_rect = [250, 150, 300, 200]
pygame.draw.rect(screen, [255, 0, 0], my_rect, 5)
pygame.display.flip()
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()