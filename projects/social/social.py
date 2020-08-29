import random

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        # nodes / vertices
        # maps IDs to User objs (lookup tbl for User Objects given IDs) 
        self.users = {}
        # adjacency list / edges
        # maps user_id to a list of other words (who are thier friends)
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def fisher_yates_shuffle(self, l):
        for i in range(0, len(l)):
            random_index = random.randint(i, len(l) - 1)
            l[random_index], l[i] = l[i], l[random_index]

    def populate_graph(self, num_users, avg_friendships):
        # Helps populate graph without manual entering

        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(0, num_users):
            self.add_user(f'User {i + 1}')

        possible_friendships = []
        # Create friendships
        # Generate all possible friendships
        # Avoid duplicate friendships / increment +1 on friend
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                # user_id == friend_id cannot happen
                # if friendship between user_id & friend_id already exists
                # don't add friendship between user_id and friend_id
                possible_friendships.append((user_id, friend_id)) # creating tuple

        # Randomly selected X friends
        # shuffle friends
        self.fisher_yates_shuffle(possible_friendships)

        # the formula of x is numUsers * avgFriendships // 2
        num_friendships = num_users * avg_friendships // 2
        
        for i in range(0, num_friendships):
            friendships = possible_friendships[i]
            self.add_friendship(friendships[0], friendships[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
