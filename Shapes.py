__author__ = 'Mandar'
import pygame
import numpy as np
import math as m
from pygame import gfxdraw
import Vertices
import copy


class Creates(object):
    def __init__(self):
        pass

    #Using Bressenham's
    def line(self, surface, X1, Y1, X2, Y2, color):
        x1 = copy.copy(X1)
        y1= copy.copy (Y1)
        x2 = copy.copy(X2)
        y2 = copy.copy(Y2)
        gfxdraw.pixel(surface, x1, y1, color)
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        if (x2 > x1):
            xinc = 1
        else:
            xinc = -1
        if (y2 > y1):
            yinc = 1
        else:
            yinc = -1
        x1t = x1
        y1t = y1
        if (dx > dy):
            p = 2 * dy - dx
            k = 0
            while k <= dx:
                x1t += xinc
                if p < 0:
                    p += 2 * dy
                else:
                    y1t += yinc
                    p += 2 * dy - 2 * dx
                gfxdraw.pixel(surface, x1t, y1t, color)
                k += 1
        else:
            p = 2 * dx - dy
            k = 0
            while k <= dy:
                y1t += yinc
                if p < 0:
                    p += 2 * dx
                else:
                    x1t += xinc
                    p += 2 * dx - 2 * dy
                gfxdraw.pixel(surface, x1t, y1t, color)
                k += 1



