# coding=utf-8

from Graph import *
import numpy as np
import sys
import pandas as pd


def calDistance(node1,node2):
    node1 = np.array([node1.x, node1.y])
    node2 = np.array([node2.x, node2.y])
    distance = np.sqrt(np.sum((node1-node2) ** 2))
    return distance


def isInLineBounds(node1,node2,node3):
    boundary = Boundary(node1,node2)
    return boundary.checkInside(node3)


def pointProjection(node1,node2,node3):
    ax,ay,bx,by,cx,cy = node1.x,node1.y,node2.x,node2.y,node3.x,node3.y

    res = (bx - ax ) ** 2 + (by - ay) ** 2
    if res == 0:
        return Node(ax,ay)

    r = ((ay-cy)*(ay-by) - (ax-cx)*(bx-ax)) / res

    newx = ax + r*(bx-ax)
    newy = ay + r*(by-ay)
    newpoint = Node(newx,newy)

    if not isInLineBounds(node1,node2,node3):
        disStart = calDistance(newpoint,node1)
        disEnd = calDistance(newpoint,node2)

        if disStart < disEnd:
            newpoint = Node(ax,ay)
        else:
            newpoint = Node(bx,by)

    return newpoint


def takeFirst(item):
    return item[0]


def readnodes(filename):
    file = pd.read_csv(filename)
    nodes = list()

    print("There are {} points in the dataset.".format(file.shape[0]))

    maxX,minX,maxY,minY = -sys.maxsize, sys.maxsize, -sys.maxsize, sys.maxsize

    for index,line in file.iterrows():
        node = Node(line['x'], line['y'])

        node.id = int(line['row_id'])

        minX = min(node.x, minX)
        minY = min(node.y, minY)
        maxX = max(node.x, maxX)
        maxY = max(node.y, maxY)

        nodes.append(node)

    boundary = Boundary(Node(minX, minY), Node(maxX, maxY))

    return nodes, boundary

