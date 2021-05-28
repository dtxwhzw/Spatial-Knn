# coding=utf-8

import sys
import random


class Node:
    """
    This class represent each node in a Graph. The Graph is an area in a range.
    """
    def __init__(self,x,y,id=None):
        self.id = id
        self.x = x
        self.y = y

    def __str__(self):
        return "{} {:.6f} {:.6f}".format(self.id, self.x, self.y)

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.__str__())

    def __eq__(self, other):
        return self.id == other.id


class Boundary:
    """
    This class represent the whole area
    (MinX,MinY)----------(MaxX,MinY)
    |                           |
    |                           |
    |                           |
    (MinX,MaxY)----------(MaxX,MaxY)
    """
    def __init__(self,node1,node2):
        self.MinX = min(node1.x,node2.x)
        self.MaxX = max(node1.x,node2.x)
        self.MinY = min(node1.y,node2.y)
        self.MaxY = max(node1.y,node2.y)

    def __str__(self):
        return "{:.6f} {:.6f} {:.6f} {:.6f}".format(self.MinX,self.MaxX,self.MinY,self.MaxY)

    def __repr__(self):
        return self.__str__()

    def checkInside(self,node):
        return self.MinX <= node.x <= self.MaxX and self.MinY <= node.y <= self.MaxY