# using DFT
# will require a Stack data structure

# steps for solving problems with graphs:
    # what are our nodes/vertices?
    # what are our edges?


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
    
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex):
        return self.vertices[vertex]

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

def graph_builder(ancestors):
    graph = Graph()

    # for pair in ancestors:
    #     parent = pair[0]
    #     child = pair[1]

    for parent, child in ancestors:
        graph.add_vertex(parent)
        graph.add_vertex(child)
        graph.add_edge(child, parent)
    
    return graph

def earliest_ancestor(ancestors, starting_node):
    graph = graph_builder(ancestors)

    s = Stack()
    s.push([starting_node])

    visited = set()

    longest_path = [starting_node] # may be 1 or the beginning node
    earliest_node = -1

    while s.size() > 0:
        path = s.pop()
        curr_node = path[-1] # start from last node in path

    # if path is longer, or path is equal but the id is smaller
        if (len(path) > len(longest_path)) or (len(path) == len(longest_path) and curr_node < earliest_node):
            longest_path = path
            earliest_node = longest_path[-1] # start from last node in path

        if curr_node not in visited:
            visited.add(curr_node)

            neighbors = graph.get_neighbors(curr_node)

            for neighbor in neighbors:
                new_path = path.copy()
                new_path.append(neighbor)
                s.push(new_path)
            
    return earliest_node