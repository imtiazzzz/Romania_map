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

def astar(graph, start, goal):
    #node track of the cities to explore based on value
    open_list = []
    #set to store the cities that have been explored already to avoid revisiting them.
    closed_list = set()

    # Create a dictionary to store the cost to reach each node
    g = {start: 0}

    # Create a dictionary to store the parent of each node(city)
    parents = {start: None}

    # Calculate the initial value for the start node
    h = heuristic(start, goal)

    # Calculate the initial final value for the start node
    f = g[start] + h

    # Add to the start node to the open list
    heapq.heappush(open_list, (f, start))

    while open_list:
        # Pop the node with the lowest final value from the open list
        current_node = heapq.heappop(open_list)[1]

        # Check if the current node is the goal
        if current_node == goal:
            path = []
            while current_node:
                path.append(current_node)
                current_node = parents[current_node]
            path.reverse()
            return path

        # Add the current node to the closed list(skip)
        closed_list.add(current_node)

        # Explore the neighbors of the current node
        for neighbor, distance in graph[current_node].items():
            # Calculate the tentative goal value for the neighbor
            tentative_g = g[current_node] + distance

            # Check if the neighbor is already in the closed list and the tentative goal value is higher
            if neighbor in closed_list and tentative_g >= g.get(neighbor, float('inf')):
                continue

            # Check if the neighbor is not in the open list or the tentative goal value is lower
            if tentative_g < g.get(neighbor, float('inf')):
                # Update the goal value and parent of the neighbor
                g[neighbor] = tentative_g
                parents[neighbor] = current_node

                # Calculate the heuristic value and final value for the neighbor
                h = heuristic(neighbor, goal)
                f = tentative_g + h

                # Add the neighbor to the open list with its heuristic value
                heapq.heappush(open_list, (f, neighbor))

    # No path found
    return None

# Take user input for the start and goal cities
start_city = input("Enter the start city: ")
goal_city = input("Enter the goal city: ")

# Find the shortest path between the start and goal cities
path = astar(graph, start_city, goal_city)
if path:
    print("Shortest path:", path)
    total_distance = sum(graph[path[i]][path[i+1]] for i in range(len(path)-1))
    print("Total distance:", total_distance)
else:
    print("No path found.")

