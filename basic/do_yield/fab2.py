#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 斐波那契数列
# F(0)=0，F(1)=1, F(n)=F(n - 1)+F(n - 2)


class FabIterator:
    def __init__(self, fb):
        self.a = fb.a
        self.b = fb.b

    def __next__(self):
        r = self.a + self.b
        self.a = self.b
        self.b = r
        return r


class Fab:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return FabIterator(self)


fab = Fab()
for i in fab:
    if i > 100:
        break
    print(i)




