from queue import PriorityQueue as pq

# used as both heuristic and distance function. 
def h(start, end):  
    return((start[0] - end[0])**2 + (start[1] - end[1])**2)**(1/2)

# generates the path form goal since there is only one path reaching the goal it generates from reverse.
def path(previous, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = previous[current]
        path.append(current)
    path.reverse()    # reversing the path since we started from goal.
    return path

def shortest_path(M, start, goal):
    frontier = pq()    # priority queue
    frontier.put(start, 0)
    g = {start: 0}    # distance from start to a node.
    previous = {start: None}
    while not frontier.empty():
        current = frontier.get()    # gets the least priority value, in this case it gets the one with least distance.

        if current == goal:
            continue
        
        for neighbor in M.roads[current]:
            temp = g[current] + h(M.intersections[current], M.intersections[neighbor])
            if neighbor not in g or temp < g[neighbor]:    # temp < g[neighbor] - to select the shortest path and explore min no. of nodes.
                previous[neighbor] = current    # remembering where the neighbor came from.
                g[neighbor] = temp  
                f = temp + h(M.intersections[neighbor], M.intersections[goal])    # f = g + h
                frontier.put(neighbor, f)    # adding neighbor with its total distance as priority.
           
    return path(previous, start, goal)