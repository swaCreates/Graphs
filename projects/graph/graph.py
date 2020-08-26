"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """

        # if this node is not in our vertices, create a slot for the node
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """

        # find v1 in our vertices, and add v2 to that set of edges
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # make a queue
        # enqueu our starting vertex/node
        q = Queue() # FIFO
        q.enqueue(starting_vertex)

        # make a set to track if we have been here before
        visited = set()

        # while our queue is not empty
        while q.size() > 0:
            # dequeue at the front of the line, this will be our curr_node
            curr_node = q.dequeue()
            # if we haven't visited yet,
            if curr_node not in visited:
                # mark as visited
                print(curr_node)
                visited.add(curr_node)
                # get neighbors
                neighbors = self.get_neighbors(curr_node)
                # for each neighbor, add to queue
                for neighbor in neighbors:
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # make a stack
        # push onto stack
        s = Stack() # LIFO
        s.push(starting_vertex)

        # make a set to track if we have been here before 
        visited = set()

        # while our stack is not empty
        while s.size() > 0:
            # pop off whatever is on top, this will be our curr_node
            curr_node = s.pop()
            # if we haven't visited yet,
            # mark as visited
            if curr_node not in visited:
                print(curr_node)
                visited.add(curr_node)
                # get neighbors
                neighbors = self.get_neighbors(curr_node)
                # for each neighbor, push to stack
                for neighbor in neighbors:
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        pass  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()

        q.enqueue({
            'curr_vertex': starting_vertex,
            'path': [starting_vertex]
        })

        visited = set()

        while q.size() > 0:
            curr_obj = q.dequeue()
            curr_path = curr_obj['path']
            curr_node = curr_obj['curr_vertex']

            # print(curr_node)
            # print(curr_path)

            if curr_node not in visited:
                visited.add(curr_node)

                if curr_node == destination_vertex:
                    return curr_path

                for neighbor in self.get_neighbors(curr_node):

                    new_path = list(curr_path)
                    new_path.append(neighbor)

                    q.enqueue({
                        'curr_vertex': neighbor,
                        'path': new_path
                    })

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        s = Stack()

        s.push({
            'curr_vertex': starting_vertex,
            'path': [starting_vertex]
        })

        visited = set()

        while s.size() > 0:
            curr_obj = s.pop()
            curr_path = curr_obj['path']
            curr_node = curr_obj['curr_vertex']

            # print(curr_node)
            # print(curr_path)

            if curr_node not in visited:
                visited.add(curr_node)

                if curr_node == destination_vertex:
                    return curr_path

                for neighbor in self.get_neighbors(curr_node):

                    new_path = list(curr_path)
                    new_path.append(neighbor)

                    s.push({
                        'curr_vertex': neighbor,
                        'path': new_path
                    })

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
