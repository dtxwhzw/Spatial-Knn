# coding=utf-8

from Graph import *
from utils import *


class GridIndex:
    def __int__(self,boundary,num_columns,num_rows,core_size):
        self.num_columns = num_columns
        self.num_rows = num_rows
        self.boundary = boundary
        self.coreSize = core_size
        self.width = boundary.MaxX-boundary.MinX
        self.height = boundary.MaxY-boundary.MinY
        self.grid_width = self.width/num_columns
        self.grid_height = self.height/num_rows

    def getGridIndex(self,node):
        return int((node.x - self.boundary.MinX)/self.grid_width), int((self.boundary.MaxY-node.y)/self.grid_height)

    def findCoveringGrids(self,node1,node2):
        x1,y1 = self.getGridIndex(node1)
        x2,y2 = self.getGridIndex(node2)

        minX, maxX, minY, maxY = min(x1, x2), max(x1, x2), min(y1, y2), max(y1, y2)

        maxX = self.num_columns-1 if maxX > self.num_columns-1 else maxX
        maxY = self.num_rows-1 if maxY > self.num_rows-1 else maxY
        minX = 0 if minX < 0 else minX
        minY = 0 if minY < 0 else minY

        spanX = abs(maxX-minX) + 1
        spanY = abs(maxY-minY) + 1

        return [(minY+j)*self.num_columns + (minX+i) for j in range(spanY) for i in range(spanX)]


class GridIndexForNodes(GridIndex):
    def __init__(self,boundary,num_columns,num_rows,core_size):
        super(GridIndexForNodes,self).__int__(boundary,num_columns,num_rows,core_size)
        self.grids = [[] for _ in range(self.num_columns * self.num_rows)]

    def buildIndex(self, nodes):
        for node in nodes:
            x, y = self.getGridIndex(node)
            if x < 0:
                x = 0
            elif x > self.num_columns -1:
                x = self.num_columns -1
            if y < 0:
                y = 0
            elif y > self.num_rows-1:
                y = self.num_rows-1

            index = y * self.num_columns + x

            self.grids[index].append(node)

    def knn(self, node, k):
        centerX = node.x
        centerY = node.y

        node1 = Node(centerX-self.coreSize,centerY-self.coreSize)
        node2 = Node(centerX+self.coreSize,centerY+self.coreSize)

        res = list()
        for index in self.findCoveringGrids(node1,node2):
            res += [(calDistance(node,neighbor), neighbor) for neighbor in self.grids[index]]

        res.sort(key=takeFirst)
        return res[:k]