# Paul Sanders
# 9/15/18


# OOP experiment and graphical graphs (lol)
# created class Vertex and Graph (which contains verticies)
# created input interface for .csv adj. matricies
# simple graphing utility
import numpy as np
from graphics import *
from math import *

WIDTH = 500
HEIGHT = 500

R = 200


class Vertex:
    def __init__(self, vertex):
        self.name = vertex
        self.neighbors = []

    def add_neighbor(self, neighbor):
        if isinstance(neighbor, Vertex):
            if neighbor.name not in self.neighbors:
                self.neighbors.append(neighbor.name)
                neighbor.neighbors.append(self.name)
                self.neighbors = sorted(self.neighbors)
                neighbor.neighbors = sorted(neighbor.neighbors)
        else:
            return False

    def add_neighbors(self, neighbors):
        for neighbor in neighbors:
            if isinstance(neighbor, Vertex):
                if neighbor.name not in self.neighbors:
                    self.neighbors.append(neighbor.name)
                    neighbor.neighbors.append(self.name)
                    self.neighbors = sorted(self.neighbors)
                    neighbor.neighbors = sorted(neighbor.neighbors)
            else:
                return False

    def repr(self):
        return str(self.neighbors)


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex):
            self.vertices[vertex.name] = vertex.neighbors

    def add_vertices(self, vertices):
        for vertex in vertices:
            if isinstance(vertex, Vertex):
                self.vertices[vertex.name] = vertex.neighbors

    def add_edge(self, vertex_start, vertex_end):
        if isinstance(vertex_start, Vertex) and isinstance(vertex_end, Vertex):
            vertex_start.add_neighbor(vertex_end)
            if isinstance(vertex_start, Vertex) and isinstance(vertex_end, Vertex):
                self.vertices[vertex_start.name] = vertex_start.neighbors
                self.vertices[vertex_end.name] = vertex_end.neighbors

    def add_edges(self, edges):
        for edge in edges:
            self.add_edge(edge[0], edge[1])

    def adjacencyList(self):
        if len(self.vertices) >= 1:
            return [str(key) + ":" + str(self.vertices[key]) for key in self.vertices.keys()]
        else:
            return dict()


def graph(g):
    """ Function to print a graph as adjacency list and adjacency matrix. """
    return str(g.adjacencyList()) + '\n' + '\n'
###########################################################################


def importGraph(filename):
    with open(filename, "r") as f:
        counter = 0
        g = Graph()
        for line in f.readlines():
            edge_list = line.rstrip().split(',')
            print(edge_list)
            v = Vertex(counter)
            v.neighbors = [i for i, x in enumerate(edge_list) if x is "1"]
            counter += 1
            g.add_vertex(v)
    f.close()
    return g

# displays the graph, where each vertex cooresponds to the vertex of a regular polygon of size n


def displayGraph(graph):

    win = GraphWin('Graph', WIDTH, HEIGHT)
    midpoint = Point(WIDTH / 2, HEIGHT / 2)
    midpoint.setFill('red')
    midpoint.draw(win)

    counter = 0
    points = {}
    n = len(graph.vertices.keys())
    for i in graph.vertices.keys():  # prints the verticies of graph
        p = Point(R * cos(2 * pi * counter / n) + midpoint.getX(),
                  R * sin(2 * pi * counter / n) + midpoint.getY())
        p.draw(win)
        label = Text(p, i)
        label.setTextColor('black')
        points[label.getText()] = label
        # label.draw(win)
        counter += 1

    vertex = graph.vertices.keys()  # prints edges of graph
    print(points)

    for v in vertex:
        for e in graph.vertices[v]:
            if e in vertex:
                edge = Line(points[v].getAnchor(), points[e].getAnchor())
                edge.setOutline('red')
                edge.draw(win)

    for p in points.items():
        p[1].draw(win)

    win.getMouse()
    win.close()


###########################################################################
# main

def main():
    filename = ".\\g.csv"
    g = importGraph(filename)
    displayGraph(g)
    print(g.adjacencyList())


main()

###########################################################################
# the testing grounds
#a = Vertex('A')
#b = Vertex('B')
#c = Vertex('C')
#d = Vertex('D')
#e = Vertex('E')

#a.add_neighbors([b, c, e])
#b.add_neighbors([a, c])
#c.add_neighbors([b, d, a, e])
# d.add_neighbor(c)
#e.add_neighbors([a, c])


#g = Graph()
# print(graph(g))
# print("\n")
#g.add_vertices([a, b, c, d, e])
#g.add_edge(b, d)
# print("\n")
# print(graph(g))
