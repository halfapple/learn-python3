#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 斐波那契数列
# F(0)=0，F(1)=1, F(n)=F(n - 1)+F(n - 2)

def fab_with_yield(mx):
    x, y, n = 0, 1, 1
    while n < mx:
        yield y
        x, y = y, x + y
        n += 1


def test():
    for i in fab_with_yield(5):
        print(i)


test()




