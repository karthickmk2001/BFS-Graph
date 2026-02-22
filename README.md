It uses Adjacency List to represent a Graph
The algorithm gives the shortest path

FLOW:

1. begin the queue with start node.

2. Create Visited set, for not revisiting the nodes

3. While the queue is not empty:
   a) FIFO - Removes the first node
   b) Check to see it is the destination.
   c) If yes then print the path and terminate.
   d) If not then add its unvisited neighbors to its queue.

4. If the queue becomes empty, the destination does not exist.
