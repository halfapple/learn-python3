#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 斐波那契数列
# F(0)=0，F(1)=1, F(n)=F(n - 1)+F(n - 2)


def fab_data(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fab_data(n-1) + fab_data(n-2)


def test():

    for i in range(10):
        print(fab_data(i)),


test()
