from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

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

# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = ['n', 's']

room = player.current_room

s = Stack()
s.push(room)

room_dict = {}
room_directions = {
    'n': '?',
    's': '?',
    'e': '?',
    'w': '?',
}

while s.size() > 0:
    curr_room = s.pop()
    room_dict[0] = room_directions


    # curr_obj = s.pop()
    # curr_room = curr_obj['starting_room']
    # curr_path = curr_obj['path']

# Create Traversal Graph / Adjacency List

# what are my vertices? .....room
# what are my edges? .....directions

# Am I using a Queue(BFS) == if '?' or Stack (DFS) == initial traversal?


"""You know you are done when you have exactly 500 entries (0-499) in your graph and no '?' in the adjacency dictionaries. To do this, you will need to write a traversal algorithm that logs the path into traversal_path as it walks."""

# rooms should be stored as int (key) vertex
# traversal direction should be stored as input (value) edges

# DFS
# push starting room onto stack
# while the stack isn't empty, pop the curr room off stack
# check the room for optional directions
    # add room to visited
    # check for connected room (edges) with ? marks (I think)
    # if moveable go explore
# BFS
    # else if stuck
    # retrace steps until you can find an unexplored route


# Still confused on how I would be using traversal_path
# or
# If I use the room_directions, how would I make changes to that or use that or should I make changes at all







# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
