# shortestRouteFinder
Given a set of points with distances between them, program finds the shortest route from a vertex to other vertices.

Program finds the shortest distance between a source vertex and other vertices.
Program is pre-fed with a set of points and distances between neighbour points.

How I proceeded with this exercise: 
I had learnt about the logic of Dijkstra’s algorithm in an algorithm class and understood how to implement it with the help of (i) a priority graph and (ii) graph; however, as an implementation of the algorithm in Python was available on  http://interactivepython.org/runestone/static/pythonds/Graphs/DijkstrasAlgorithm.html, I used it as my core programming function.

PROGRAM AIM:
# - takes a graph and source vertex.
# - finds the shortest distance from source vertex to other vertices.
# - prints the shortest distances in terms of the "cost"
# - prints the path from the source vertex to other vertices


WHAT WAS THE CHALLENGE...
1. I wanted to implement Dijkstra's algorithm.
interactivepython has a funtion that (seeminlgy) implements Dijkstra's algorithm using Priority Queue.
However, it was not clear what the function was taking as parameters.
I looked up interactivepython's Graph and Vertex class methods and found out that the parameters probably are a vertex and graph.

2. "How do I pass the "source vertex" to the Dijkstra algo? I am passing the graph which has this vertex, but how do I pass the vertex?"
I created a Graph method which accepts an "id" of a vertex (in the graph) and returns that vertex object. Then I was able to pass this vertex to the Dijkstra algo. 

NOTE:
Program uses the "setDistance" method of Class Vertex to set individual vertice's "dist" parameter 
'''
def setDistance(self,d):
        self.dist = d
'''
TOP LEARNINGS:
1. I used a function for implementing Dijkstra algo from interactivepython and constructed the rest of the program. In doing so I added a method to class Graph: the method returns a vertex object, given a #vertex id. I figured out I needed to create this method!
