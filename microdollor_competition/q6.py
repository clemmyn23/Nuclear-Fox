#!/usr/bin/python
import sys;
# from pythonds.graphs import PriorityQueue, Graph, Vertex

class Node:
    connected = set();

    def __init__(self, x, y, z, w):
        self.x = x;
        self.y = y;
        self.z = z;
        self.w = w;

class Graph:
    def __init__(self):
        self.nodes = set();
        # self.edges = defaultdict(list)

    def addN(self, node):
        self.nodes.add(node);


def main():
    # line 1
    totalBlocks = dim = int(raw_input());
    totalBlocks = totalBlocks * totalBlocks * totalBlocks;

    # line 2
    line2 = raw_input();
    weights = [int(n) for n in line2.split()]

    g = Graph();

    curr = 0;
    for z in range(0, dim):
        for y in range(0, dim):
            for x in range(0, dim):
                # print Node(x, y, z, weights[curr]);
                g.nodes.add(Node(x, y, z, weights[curr]));
                curr = curr + 1;

    # line 3
    startingCoord = [int(n) for n in raw_input().split()]
    # line 4
    endingCoord = [int(n) for n in raw_input().split()]

    g = Graph();

    print 'total blocks:', totalBlocks;
    print weights;
    print 'starting:', startingCoord;
    print 'ending:', endingCoord;
    print g.nodes;

    # print pathfind();



# def pathfind(graph, start, end):
    # while ()
    #     while ()







if __name__ == "__main__":
    main();
