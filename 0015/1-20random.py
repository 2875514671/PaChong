# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
编写一个小程序，生成1到20之间的5个随机整数的列表，并打印出来
"""

import random

l = []
x = 1

while x < 6:
	s = random.randint(1, 20)
	# print(s)
	l.append(s)
	x += 1
print(l)