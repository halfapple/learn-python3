#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def test1():
	for x in [1, 2, 3, 4, 5]:
		print(x)


def test2():
	# 首先获得Iterator对象:
	it = iter([1, 2, 3, 4, 5])
	# 循环:
	while True:
		try:
			# 获得下一个值:
			x = next(it)
			print(x)
		except StopIteration:
			# 遇到StopIteration就退出循环
			break


test1()

test2()
