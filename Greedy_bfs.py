import heapq

# Define the graph of cities and their connections (edges) along with the distances
graph = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101}
}

def heuristic(node, goal):
    # Define the heuristic function for (straight-line distance)
    heuristics = {
        'Arad': 366,
        'Zerind': 374,
        'Oradea': 380,
        'Sibiu': 253,
        'Timisoara': 329,
        'Lugoj': 244,
        'Mehadia': 241,
        'Drobeta': 242,
        'Craiova': 160,
        'Rimnicu Vilcea': 193,
        'Fagaras': 176,
        'Pitesti': 100,
        'Bucharest': 0
    }
    return heuristics[node]

def gbfs(graph, start, goal):
    #node track of the cities to explore based on value
    open_list = []

    # Create a dictionary to store the parent city of each node(city)
    parents = {start: None}

    # Add the start node to explore (open the list) with its value
    heapq.heappush(open_list, (heuristic(start, goal), start))

    while open_list:
        # Pop the node with the lowest value from the open list
        current_node = heapq.heappop(open_list)[1]

        # Check if the current node is the goal 
        if current_node == goal:
            path = []
            while current_node:
                path.append(current_node)
                current_node = parents[current_node]
            path.reverse()
            return path

        # Explore the neighbors of the current node
        for neighbor in graph[current_node]:
            
            # Check if the neighbor has already been visited
            if neighbor in parents:
                continue

            # Set the parent of the neighbor
            parents[neighbor] = current_node

            # Add the neighbor to the open list with its heuristic value
            heapq.heappush(open_list, (heuristic(neighbor, goal), neighbor))

    # No path found
    return None

# Take user input for the start and goal cities
start_city = input("Enter the start city: ")
goal_city = input("Enter the goal city: ")

# Find the shortest path between the start and goal cities
path = gbfs(graph, start_city, goal_city)
if path:
    print("Shortest path:", path)
    total_distance = sum(graph[path[i]][path[i+1]] for i in range(len(path)-1))
    print("Total distance:", total_distance)
else:
    print("No path found.")


