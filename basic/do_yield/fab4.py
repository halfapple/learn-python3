#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 斐波那契数列
# F(0)=0，F(1)=1, F(n)=F(n - 1)+F(n - 2)

class Fab(object):
    def __init__(self, mx):
        self.mx = mx
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        r = self.a + self.b
        if r < self.mx:
            self.a = self.b
            self.b = r
            return r
        raise StopIteration


fab = Fab(100)
for i in fab:
    print(i)




