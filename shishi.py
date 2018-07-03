# -*- coding: utf-8 -*-
# !/usr/bin/env python

for i in range(ord('x'),ord('z') + 1):
	for j in range(ord('x'),ord('z') + 1):

		if i != j:

			for k in range(ord('x'),ord('z') + 1):

				if (i != k) and (j != k):

					if (i != ord('x')) and (k != ord('x')) and (k != ord('z')):

						print("order is a -- %s b -- %s c--%s" % (chr(i),chr(j),chr(k)))


import itertools
for i in itertools.permutations('xyz'):
	if i[0] != 'x' and i[2] != 'x' and i[2] != 'z':
		print('a vs %s, b vs %s, c vs %s' % (i[0], i[1], i[2]))
		
		
