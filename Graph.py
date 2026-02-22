from collections import deque

# Graph BFS 
# It uses Adjacency List
graph = {
    "Africa": ["Bangladesh", "Colombo", "Dublin"],
    "Bangladesh": ["Egypt", "France"],
    "Colombo": ["Germany"],
    "Dublin": ["Hong Kong", "India"],
    "Egypt": ["Japan"],
    "France": ["Kuala Lumpur"],
    "Hong Kong": ["Laos", "Mexico"],
    "India": ["Netherlands"],
    "Germany": [],
    "Japan": [],
    "Kuala Lumpur": [],
    "Laos": [],
    "Mexico": [],
    "Netherlands": []
}


def bfs_graph(search, found):
    q = deque([(search, [search])])     #(node at present, path which had taken so far)
    visited = set([search])             #Creating a set to keep track of the visited nodes
    steps = 0                           #How many nodes expanded

    while q:                            #Loop starts here until queue is NOT empty
        now, path = q.popleft()         #FIFO: Pop the first element from the queue
        steps += 1                      #Increment the steps count for each node visited

        print(f"Step {steps}: Visiting {now}")

        if now == found:                                 #If the current node is the destination, print the path and steps taken
            print("\nDestination Reached")
            print("Shortest Path:", " → ".join(path))
            print("Total Steps:", steps)
            return

        for g in graph[now]:                               #Checks all the elements of the current node
            if g not in visited:                           #Avoids visiting the same node again
                visited.add(g)                             #If visited, add it to the visited set
                q.append((g, path + [g]))                  #Adds the new node to the queue with the updated path

    print("\nThe Destination was entered was Not Found")


#Getting Inputs from the User 
start = input("Enter starting country: ")
end = input("Enter destination country: ")

if start in graph:
    bfs_graph(start, end)
else:
    print("Enter the valid starting country")