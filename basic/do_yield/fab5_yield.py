#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 斐波那契数列
# F(0)=0，F(1)=1, F(n)=F(n - 1)+F(n - 2)

def fab_with_yield(mx):
    a, b, n = 0, 1, 1
    while n < mx:
        yield b
        a, b = b, a + b
        n += 1


def test():
    for i in fab_with_yield(10):
        print(i)


test()




