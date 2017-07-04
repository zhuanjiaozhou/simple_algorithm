#!/usr/bin/env python
# -*- coding: utf-8 -*-

## python 递归输出n * n 的二维数组
a = [[x for x in range(8)] for x in range(8)]

def PrintSpiralArray(L,x,y):
    if x < y:
        j = x
        while j < y:
            print(L[x][j], end="    ")
            j +=1
        j = x
        while j < y:
            print(L[j][y], end="    ")
            j +=1
        j = y
        while j > x:
            print(L[y][j], end="    ")
            j -= 1
        j = y
        while j > x:
            print(L[j][x], end="    ")
            j -= 1
    elif x == y:
        print(L[x][y])
    else:
        return ;
    PrintSpiralArray(L,x + 1, y - 1)


PrintSpiralArray(a,0,7)
