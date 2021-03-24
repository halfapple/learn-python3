#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 文件太大，会导致不可预测的内存

def read_file(fpath):
    BLOCK_SIZE = 1024
    with open(fpath, 'rb') as f:
        while True:
            block = f.read(BLOCK_SIZE)
            if block:
                yield block
            else:
                return
