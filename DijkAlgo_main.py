#DijkAlgo:main
#created: 24.4.17
# Python code to implement Dijkstra's algorithm.
# Main Dijkstra code copied from: http://interactivepython.org/runestone/static/pythonds/Graphs/DijkstrasAlgorithm.html

# PROGRAM AIM:
# - takes a graph and source vertex.
# - finds the shortest distance from source vertex to other vertices.
# - prints the shortest distances in terms of the "cost"
# - prints the path from the source vertex to other vertices


#WHAT WAS THE CHALLENGE...
#1. I wanted to implement Dijkstra's algorithm.
# interactivepython has a funtion that (seeminlgy) implements Dijkstra's algorithm using Priority Queue.
# However, it was not clear what the function was taking as parameters.
# I looked up interactivepython's Graph and Vertex class methods and found out that the parameters probably are a vertex and graph.

#2. "How do I pass the "source vertex" to the Dijkstra algo? I am passing the graph which has this vertex, but how do I pass the vertex?"
#I created a Graph method which accepts an "id" of a vertex (in the graph) and returns that vertex object. Then I was able to pass this vertex to the Dijkstra algo. 

#NOTE:
# Program uses the "setDistance" method of Class Vertex to set individual vertice's "dist" parameter 
'''
def setDistance(self,d):
        self.dist = d
'''
#TOP LEARNINGS:
#1. I used a function for implementing Dijkstra algo from RR and constructed the rest of the program,
# in doing so I added a method to class Graph: the method returns a vertex object, given a vertex id 
#I figured out I needed to create this method!

from refGrAndVer import Graph, Vertex
from refGrAndVerPQ import PriorityQueue

#method takes a graph and source vertex.
#it finds the shortest distance from source vertex to other vertices.
def dijkstra(aGraph,start):
    pq = PriorityQueue()
    start.setDistance(0) #note: 'start' is a vertex, not its id
    pq.buildHeap([(v.getDistance(),v) for v in aGraph])
    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() \
                    + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.setDistance( newDist )
                nextVert.setPred(currentVert)
                pq.decreaseKey(nextVert,newDist)
                nextVert.series.append(currentVert.id) # adi:added 
                nextVert.series.append(currentVert.series) # adi:added 
                # adi:added to the original code

#main
print  ("Program finds the shortest distance between a source vertex and other vertices.")
print  ("Program is pre-fed with a set of points and distances between neighbour points.")
print  (">>>>>>>>>>>>>>>>>>>>")
print  ("The source vertex is 0")              
g = Graph()
for i in range(7):
    g.addVertex(i)

g.addEdge(0,1,5)
g.addEdge(0,4,2)
g.addEdge(1,2,15)
g.addEdge(2,3,25)
g.addEdge(3,4,35)
g.addEdge(4,5,45)
g.addEdge(5,0,55)
g.addEdge(3,6,10)

print ("The entered graph is:")
for v in g:
    for w in v.getConnections(): 
        print("( %s , %s, %s )" % (v.getId(), w.getId(), v.getWeight(w) ))  

vertex0 = g.getVertex(0)

d = dijkstra(g,vertex0)

print ("The shortest distance between vertex 0 and the other vertices is:")
vertexTrail = {} # vertexTrail contains the vertices encountered on the way
for i in range (g.numVertices):
    print(" VERTEX ", i , "-->", g.vertices[i]. getDistance () )
    vertexTrail[i] = (g.vertices[i].series) 

print  (">>>>>>>>>>>>>>>>>>>>")

print ("The path between vertex 0 and the other vertices is givan by the foll dict:")

print ("The foll dictionary has:")
print ("key --> vertex no")
print ("value --> list of the vertices encountered on the way")
print (vertexTrail)

#Output: 

'''
Program finds the shortest distance between a source vertex and other vertices.
Program is pre-fed with a set of points and distances between neighbour points.
>>>>>>>>>>>>>>>>>>>>
The source vertex is 0
The entered graph is:
( 0 , 1, 5 )
( 0 , 4, 2 )
( 1 , 2, 15 )
( 2 , 3, 25 )
( 3 , 6, 10 )
( 3 , 4, 35 )
( 4 , 5, 45 )
( 5 , 0, 55 )
The shortest distance between vertex 0 and the other vertices is:
 VERTEX  0 --> 0
 VERTEX  1 --> 5
 VERTEX  2 --> 20
 VERTEX  3 --> 45
 VERTEX  4 --> 2
 VERTEX  5 --> 47
 VERTEX  6 --> 55
>>>>>>>>>>>>>>>>>>>>
The path between vertex 0 and the other vertices is givan by the foll dict:
The foll dictionary has:
key --> vertex no
value --> list of the vertices encountered on the way
{0: [], 1: [0, []], 2: [1, [0, []]], 3: [2, [1, [0, []]]], 4: [0, []], 5: [4, [0, []]], 6: [3, [2, [1, [0, []]]]]}
'''
