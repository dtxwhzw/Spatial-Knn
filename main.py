# coding=utf-8

from Graph import *
from utils import *
from Index import *
import time
import random


def main(k):
    print("="*20)
    print(f"Prediction the {k} nearest neighbors......")
    print("="*20)
    time0 = time.time()
    nodes, boundary = readnodes('data.csv')
    nodesGridIndex = GridIndexForNodes(boundary,100,100,0.001)
    nodesGridIndex.buildIndex(nodes)
    spanX = boundary.MaxX - boundary.MinX
    spanY = boundary.MaxY - boundary.MinY
    pX = boundary.MinX + random.random()*spanX
    pY = boundary.MaxY + random.random()*spanY

    print('x',pX,'y',pY)

    print(f'The top {k} cloest nodes is :')
    print('='*20)
    for node in nodesGridIndex.knn(Node(pX,pY),k):
        print(node)

    print('=' * 20)
    print("The whole process cost : {:.2f} second.".format(time.time()-time0))


if __name__ == '__main__':
    import sys
    k = int(sys.argv[1])

    main(k)