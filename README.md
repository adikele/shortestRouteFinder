# shortestRouteFinder
How to run this program:
You need an IDE that runs Python 3 to run this program. 
Download the three python files and store them in one folder. Run the DijkAlgo_main.py file.

What the program does:
Given a set of points with distances between them, program finds the shortest route from a vertex (a so-called "source" vertex) to other vertices. The set of points and distances between neighbour points are pre-fed in this program. The program displays the shortest distances in terms of the "cost" and also displays the path from the source vertex to the other vertices.

How I proceeded with this task: 
I had learnt about the logic of Dijkstra’s algorithm in an algorithm class and understood how to implement it with the help of (i) a priority graph and (ii) graph.
I used the code provided in the following reference as the skeleton for my program:  http://interactivepython.org/runestone/static/pythonds/Graphs/DijkstrasAlgorithm.html

What was the challenge:
1. The interactivepython.org has a funtion that implements Dijkstra's algorithm using Priority Queue.
However, it was not clear what the function was taking as parameters.
I looked up interactivepython's Graph and Vertex class methods and found out that the parameters are a vertex and a graph.

2. How do I pass the "source vertex" to the Dijkstra algo? I am passing the graph which has this vertex, but how do I pass the vertex?
I created a Graph method which accepts an "id" of a vertex (in the graph) and returns that vertex object. Then I was able to pass this vertex to the Dijkstra's algorithm. 

Top Learnings:
1. I used a function for implementing Dijkstra's algorithm from interactivepython and constructed the rest of the program. In doing so I added a method to class Graph: the method returns a vertex object, given a vertex id. 
